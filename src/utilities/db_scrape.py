print('GO db_scrape.py -> starting IMPORTs')
import sites #required: sites/__init__.py
from utilities import *
import json
from flask import Response
from re import *

'''
# https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
# https://docs.sqlalchemy.org/en/13/dialects/mysql.html#module-sqlalchemy.dialects.mysql.pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
# https://pymysql.readthedocs.io/en/latest/user/examples.html
#NOTE: '$ pip3' == '$ python3.6 -m pip'
    $ python3 -m pip install PyMySQL
    $ python3.7 -m pip install PyMySQL
'''
import pymysql.cursors

filename = 'db_scrape.py'
logenter(filename, "\n IMPORTs complete:- STARTING -> file '%s' . . . " % filename, simpleprint=False, tprint=True)

#db_connect from sites/__init__.py
dbUser = sites.dbUser
dbPw = sites.dbPw
dbName = sites.dbName
dbHost = sites.dbHost

db = None
cur = None

strErrCursor = "global var cur == None, returning -1"
strErrConn = "FAILED to connect to db"

def JSONResponse(dict):
    return Response( json.dumps(dict), mimetype="application/json" )

#====================================================#
##              db connection support               ##
#====================================================#
def open_database_connection():
    funcname = '(%s) open_database_connection' % filename
    logenter(funcname, simpleprint=False, tprint=False)

    # Connect to DB #
    try:
        global db, cur

        # legacy manual db connection #
        db = pymysql.connect(host=dbHost,
                             user=dbUser,
                             password=dbPw,
                             db=dbName,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        cur = db.cursor()

        if cur == None:
            logerror(funcname, "database cursor received (cur) == None; returning None", "FAILED to connect to db", simpleprint=False)
            return -1

        loginfo(funcname, ' >> CONNECTED >> to db successfully!', simpleprint=True)
    except:
        logerror(funcname, "exception hit", "FAILED to connect to db", simpleprint=False)
        return -1
    finally:
        return 0

def close_database_connection():
    funcname = '(%s) close_database_connection' % filename
    logenter(funcname, simpleprint=False, tprint=False)
    
    global db, cur
    if db == None:
        logerror(funcname, "global var db == None; returning", "FAILED to close db connection", simpleprint=False)
        return

    db.commit()
    db.close()

    db = None
    cur = None
    loginfo(funcname, ' >> CLOSED >> db successfully!', simpleprint=True)


#====================================================#
##              dict query support                  ##
#====================================================#
def getInsertValsStrFromQueryDict(dbQueryDict):
    funcname = '(%s) getInsertValsStrFromQueryDict' % filename
    logenter(funcname, 'dbQueryDict: %s' % dbQueryDict, simpleprint=False, tprint=False)

    query = None
    strVals = "'"
    index = 0
    for key, value in dbQueryDict.items():
        strVals += str(value)
        if index < len(dbQueryDict)-1:
            strVals += "', '"
        else:
            strVals += "'"

        query = strVals
        index += 1

    logexit(funcname, " >> QUERY VALS: '%s'" % query, simpleprint=True, tprint=False)
    return query

def getProcValsTupleFromQueryDict(dbQueryDict):
    funcname = '(%s) getProcValsTupleFromQueryDict' % filename
    logenter(funcname, 'dbQueryDict: %s' % dbQueryDict, simpleprint=False, tprint=True)

    tupleVals = ()
    index = 0
    for key, value in dbQueryDict.items():
        tupleVals = tupleVals + (value,)
        index += 1

    logexit(funcname, f" >> TUPLE VALS: {tupleVals}", simpleprint=True, tprint=True)
    return tupleVals

## parse database query row into json dict ##
# @descr: parses a database query row, into a json
# @expects: db query row dictionary and keys to parse
# @requires: row, keys
# @returns: dictionary with db query string return as a json
def getJsonDictFromDBQueryRowWithKeys(row, keys):
    funcname = '(%s) getJsonDictFromDBQueryRowWithKeys' % filename
    logenter(funcname, simpleprint=False, tprint=True)

    jsonDict = {}
    for key in keys:
        #loginfo(logfuncname, '\n\n key: %s\n\n' % key, '')
        if key not in row:
            #loginfo(logfuncname, '\n\n key: %s NOT IN row: %s\n\n' % (key, row), '')
            continue

        if match('dt_*', key) is not None:
            try:
                #convert dt to seconds since 1970
                # note: needed because JSONResponse() parsing issues
                jsonDict[key] = jsonTimestampFromDBQueryTimestamp(row[key])

            except Exception as e:
                logerror(logfuncname, "\n\n!EXCEPTION HIT!\n\n e: '%s';\n\n in 'jsonDict[key] = jsonTimestampFromDBQueryTimestamp(row[key])'\n\n" % e, " falling back to 'jsonDict[key] = row[key]' instead")
                jsonDict[key] = row[key]
        else:
            jsonDict[key] = row[key]

    #loginfo(logfuncname, '\njsonDict: %s\n' % jsonDict, '')
    return jsonDict

#====================================================#
##              proc statement support              ##
#====================================================#
def procCallAdminCreateScrapeInstance(tup_scrape_inst, infoHashTupArr):
    funcname = f'({filename}) procCallAdminCreateScrapeInstance(tup_scrape_inst, infoHashTupArr)'
    logenter(funcname, 'tup_scrape_inst & infoHashTupArr: . . . ', simpleprint=False, tprint=True)
    #print(*[f" [{i}] {': '.join(map(str,str(v)))}" for i,v in enumerate(list(tup_scrape_inst))], sep='\n', end='\n\n')
    #print(*[f" [{i}] {': '.join(map(str,v))}" for i,v in enumerate(infoHashTupArr)], sep='\n', end='\n\n')

    ############# open db connection ###############
    global cur
    if open_database_connection() < 0:
        return -1

    if cur == None:
        logerror(funcname, strErrCursor, strErrConn, simpleprint=False)
        return -1

    args = tup_scrape_inst

    ## perform db query ##
    try:
        procArgs = cur.callproc(f"InsertScrapeInstance", tup_scrape_inst)
        rowCnt = cur.execute(f"select @_InsertScrapeInstance_3;")
        rows = cur.fetchall()
        scrape_inst_id = -1 if rowCnt == 0 else rows[0]['@_InsertScrapeInstance_3']
        scrape_inst_id = (scrape_inst_id,)
        loginfo(funcname, f' >> InsertScrapeInstance RESULT procArgs: {procArgs}', simpleprint=True)
        for idx, tup in enumerate(infoHashTupArr):
            tup = (*scrape_inst_id, idx, *tup)
            procArgs = cur.callproc(f"InsertTorrentRecord", tup)
            rowCnt = cur.execute(f"select @_InsertTorrentRecord_10;")
            rows = cur.fetchall()
            ins_torrent_id = -1 if rowCnt == 0 else rows[0]['@_InsertTorrentRecord_10']
            loginfo(funcname, f' >> InsertTorrentRecord RESULT procArgs: . . . ', simpleprint=True)
        result = 1
    except Exception as e: # ref: https://docs.python.org/2/tutorial/errors.html
        strE_0 = f"Exception hit... \nFAILED to call AdminCreateScrapeInstance({tup_scrape_inst}); \n\ninfoHashTupArr: {infoHashTupArr}; \n\nreturning -1"
        strE_1 = f"\n __Exception__: \n{e}\n __Exception__"
        logerror(funcname, strE_0, strE_1, simpleprint=False)
        result = -1
    finally:
        ############# close db connection ###############
        close_database_connection()

        return result

def procCallGetLatestScrape():
    funcname = f'({filename}) procCallGetLatestScrape()'
    logenter(funcname, simpleprint=False, tprint=True)

    ############# open db connection ###############
    global cur
    if open_database_connection() < 0:
        return -1

    if cur == None:
        logerror(funcname, strErrCursor, strErrConn, simpleprint=False)
        return -1

    ## perform db query ##
    try:
        procArgs = cur.callproc(f"GetLatestTorrentScrape", ())
        loginfo(funcname, f' >> GetLatestTorrentScrape RESULT procArgs: {procArgs}', simpleprint=True)
        rowCnt = cur.execute(f"call GetLatestTorrentScrape();")
        rows = cur.fetchall()
        loginfo(funcname, f' >> GetLatestTorrentScrape RESULT rowCnt: {rowCnt}; procArgs: {procArgs};', simpleprint=True)
        #print(f'Printing... rows', *rows, sep='\n ')
        result = rows
    except Exception as e: # ref: https://docs.python.org/2/tutorial/errors.html
        strE_0 = f"Exception hit... \nFAILED to call GetLatestTorrentScrape(); \n\nprocArgs: {procArgs}; \n\nreturning -1"
        strE_1 = f"\n __Exception__: \n{e}\n __Exception__"
        logerror(funcname, strE_0, strE_1, simpleprint=False)
        result = -1
    finally:
        ############# close db connection ###############
        close_database_connection()

        return result

#====================================================#
#====================================================#

loginfo(filename, "\n CLASSES & FUNCTIONS initialized:- STARTING -> additional '%s' run scripts (if applicable) . . . \n\n" % filename, simpleprint=True)


print('\n')
print('#======================================================================#')
loginfo(filename, "\n  DONE Executing additional '%s' run scripts ... \n" % filename, simpleprint=True)


