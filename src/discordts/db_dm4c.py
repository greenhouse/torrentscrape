print('GO db_dm4c.py -> starting IMPORTs')
from discordts import *
from utilities import *



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

filename = 'db_dm4c.py'
logenter(filename, "\n IMPORTs complete:- STARTING -> file '%s' . . . " % filename, simpleprint=False, tprint=True)

#db_connect
dbUser = sites.dbUser
dbPw = sites.dbPw
dbName = sites.dbName

db = None
cur = None

strErrCursor = "global var cur == None, returning -1"
strErrConn = "FAILED to connect to db"

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
        db = pymysql.connect(host='127.0.0.1',
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
def getColsStrFromQueryDict(dbQueryDict):
    funcname = '(%s) getColsStrFromQueryDict' % filename
    logenter(funcname, 'dbQueryDict: %s' % dbQueryDict, simpleprint=False, tprint=False)

    query = None
    strCols = ""
    index = 0
    for key, value in dbQueryDict.items():
        strCols += key
        if index < len(dbQueryDict)-1:
            strCols += ", "
        else:
            strCols += ""
        
        query = strCols
        index += 1

    logexit(funcname, " >> QUERY COLS: '%s'" % query, simpleprint=True, tprint=False)
    return query

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

def getSetWhereStrFromQueryDict(dbQueryDict, delimiter=','):
    funcname = '(%s) getSetWhereStrFromQueryDict' % filename
    logenter(funcname, 'dbQueryDict: %s' % dbQueryDict, simpleprint=False, tprint=False)

    #query = None
    #strSeq = ""
    query = strSeq = ""
    index = 0
    for key, value in dbQueryDict.items():
        if index < len(dbQueryDict)-1:
            strSeq += f"{key} = '{value}' {delimiter} "
        else:
            strSeq += f"{key} = '{value}'"

        query = strSeq
        index += 1

    logexit(funcname, " >> QUERY Set/Where: '%s'" % query, simpleprint=True, tprint=False)
    return query

def appendWhereStr(strWhere, strWhereAppend):
    return strWhereAppend if strWhere == None or strWhere == '' else strWhere + f', {strWhereAppend}'

def getProcValsTupleFromQueryDict(dbQueryDict):
    funcname = '(%s) getProcValsTupleFromQueryDict' % filename
    logenter(funcname, 'dbQueryDict: %s' % dbQueryDict, simpleprint=False, tprint=False)

    tupleVals = ()
    index = 0
    for key, value in dbQueryDict.items():
        tupleVals = tupleVals + (value,)
        index += 1

    logexit(funcname, f" >> TUPLE VALS: {tupleVals}", simpleprint=True, tprint=False)
    return tupleVals

#====================================================#
##              proc statement support              ##
#====================================================#
def procCallMemberServerJoin(dbQueryDict):
    funcname = f'({filename}) procCallMemberServerJoin'
    logenter(funcname, f'dbQueryDict: {dbQueryDict}', simpleprint=False, tprint=False)

    ############# open db connection ###############
    global cur
    if open_database_connection() < 0:
        return -1

    if cur == None:
        logerror(funcname, strErrCursor, strErrConn, simpleprint=False)
        return -1

    strVals = getInsertValsStrFromQueryDict(dbQueryDict)

    ## perform db query ##
    try:
        player_id = cur.execute(f"call MemberServerJoin({strVals});")
        loginfo(funcname, f' >> MemberServerJoin RESULT id: {player_id}; QUERY dbQueryDict: {dbQueryDict};', simpleprint=True)
    except Exception as e: # ref: https://docs.python.org/2/tutorial/errors.html
        strE_0 = f"Exception hit... \nFAILED to call MemberServerJoin({strVals}); dbQueryDict: {dbQueryDict}; \nreturning -1"
        strE_1 = f"\n __Exception__: \n{e}\n __Exception__"
        logerror(funcname, strE_0, strE_1, simpleprint=False)
        player_id = -1
    finally:
        ############# close db connection ###############
        close_database_connection()

        return player_id

def procCallMemberServerRemove(dbQueryDict):
    funcname = f'({filename}) procCallMemberServerRemove'
    logenter(funcname, f'dbQueryDict: {dbQueryDict}', simpleprint=False, tprint=False)

    ############# open db connection ###############
    global cur
    if open_database_connection() < 0:
        return -1

    if cur == None:
        logerror(funcname, strErrCursor, strErrConn, simpleprint=False)
        return -1

    strVals = getInsertValsStrFromQueryDict(dbQueryDict)

    ## perform db query ##
    try:
        player_id = cur.execute(f"call MemberServerRemove({strVals});")
        loginfo(funcname, f' >> MemberServerRemove RESULT id: {player_id}; QUERY dbQueryDict: {dbQueryDict};', simpleprint=True)
    except Exception as e: # ref: https://docs.python.org/2/tutorial/errors.html
        strE_0 = f"Exception hit... \nFAILED to call MemberServerRemove({strVals}); dbQueryDict: {dbQueryDict}; \nreturning -1"
        strE_1 = f"\n __Exception__: \n{e}\n __Exception__"
        logerror(funcname, strE_0, strE_1, simpleprint=False)
        player_id = -1
    finally:
        ############# close db connection ###############
        close_database_connection()

        return player_id

def procCallMemberMsgReceived(dbQueryDict):
    funcname = f'({filename}) procCallMemberMsgReceived'
    logenter(funcname, f'dbQueryDict: {dbQueryDict}', simpleprint=False, tprint=False)

    ############# open db connection ###############
    global cur
    if open_database_connection() < 0:
        return -1

    if cur == None:
        logerror(funcname, strErrCursor, strErrConn, simpleprint=False)
        return -1

    strVals = getInsertValsStrFromQueryDict(dbQueryDict)

    ## perform db query ##
    try:
        player_id = cur.execute(f"call MemberMsgReceived({strVals});")
        loginfo(funcname, f' >> MemberMsgReceived RESULT id: {player_id};', simpleprint=True)
    except Exception as e: # ref: https://docs.python.org/2/tutorial/errors.html
        strE_0 = f"Exception hit... \nFAILED to call MemberMsgReceived({strVals}); dbQueryDict: {dbQueryDict}; \nreturning -1"
        strE_1 = f"\n __Exception__: \n{e}\n __Exception__"
        logerror(funcname, strE_0, strE_1, simpleprint=False)
        player_id = -1
    finally:
        ############# close db connection ###############
        close_database_connection()

        return player_id

def procCallMemberGetBalanceDHT(dbQueryDict):
    funcname = f'({filename}) procCallMemberGetBalanceDHT'
    logenter(funcname, f'dbQueryDict: {dbQueryDict}', simpleprint=False, tprint=False)

    ############# open db connection ###############
    global cur
    if open_database_connection() < 0:
        return -1

    if cur == None:
        logerror(funcname, strErrCursor, strErrConn, simpleprint=False)
        return -1

    strVals = getInsertValsStrFromQueryDict(dbQueryDict)

    ## perform db query ##
    try:
        rowCnt = cur.execute(f"call MemberGetBalanceDHT({strVals});")
        rows = cur.fetchall()
        balance = -1 if rowCnt == 0 else rows[0][cColPlayerBalance]
        loginfo(funcname, f' >> MemberGetBalanceDHT RESULT balance: {balance}; QUERY dbQueryDict: {dbQueryDict};', simpleprint=True)
    except Exception as e: # ref: https://docs.python.org/2/tutorial/errors.html
        strE_0 = f"Exception hit... \nFAILED to call MemberGetBalanceDHT({strVals}); dbQueryDict: {dbQueryDict}; \nreturning -1"
        strE_1 = f"\n __Exception__: \n{e}\n __Exception__"
        logerror(funcname, strE_0, strE_1, simpleprint=False)
        balance = -1
    finally:
        ############# close db connection ###############
        close_database_connection()

        return balance

def procCallMemberDepositRequest(dbQueryDict):
    funcname = f'({filename}) procCallMemberDepositRequest'
    logenter(funcname, f'dbQueryDict: {dbQueryDict}', simpleprint=False, tprint=False)

    ############# open db connection ###############
    global cur
    if open_database_connection() < 0:
        return -1

    if cur == None:
        logerror(funcname, strErrCursor, strErrConn, simpleprint=False)
        return -1

    args = getProcValsTupleFromQueryDict(dbQueryDict)

    ## perform db query ##
    try:
        procArgs = cur.callproc(f"MemberDepositRequest", args)
        rowCnt = cur.execute(f"select @_MemberDepositRequest_7;")
        rows = cur.fetchall()
        player_trans_curr_id = -1 if rowCnt == 0 else rows[0]['@_MemberDepositRequest_7']
        loginfo(funcname, f' >> MemberDepositRequest RESULT id: {player_trans_curr_id}; procArgs: {procArgs}', simpleprint=True)
    except Exception as e: # ref: https://docs.python.org/2/tutorial/errors.html
        strE_0 = f"Exception hit... \nFAILED to call MemberDepositRequest({args}); dbQueryDict: {dbQueryDict}; \nreturning -1"
        strE_1 = f"\n __Exception__: \n{e}\n __Exception__"
        logerror(funcname, strE_0, strE_1, simpleprint=False)
        player_trans_curr_id = -1
    finally:
        ############# close db connection ###############
        close_database_connection()

        return player_trans_curr_id

def procCallMemberRegisterEmail(dbQueryDict):
    funcname = f'({filename}) procCallMemberRegisterEmail'
    logenter(funcname, f'dbQueryDict: {dbQueryDict}', simpleprint=False, tprint=False)

    ############# open db connection ###############
    global cur
    if open_database_connection() < 0:
        return -1

    if cur == None:
        logerror(funcname, strErrCursor, strErrConn, simpleprint=False)
        return -1

    args = getProcValsTupleFromQueryDict(dbQueryDict)

    ## perform db query ##
    try:
        procArgs = cur.callproc(f"MemberRegisterEmail", args)
        result = 1
        loginfo(funcname, f' >> MemberRegisterEmail RESULT procArgs: {procArgs}', simpleprint=True)
    except Exception as e: # ref: https://docs.python.org/2/tutorial/errors.html
        strE_0 = f"Exception hit... \nFAILED to call MemberDepositRequest({args}); dbQueryDict: {dbQueryDict}; \nreturning -1"
        strE_1 = f"\n __Exception__: \n{e}\n __Exception__"
        logerror(funcname, strE_0, strE_1, simpleprint=False)
        result = -1
    finally:
        ############# close db connection ###############
        close_database_connection()

        return result

#====================================================#
##              proc statement support              ##
#====================================================#
def procGetPlayerIDFrom(discord_id_tag):
    funcname = '(%s) procGetPlayerIDFrom' % filename
    logenter(funcname, 'discord_id_tag: %s' % (discord_id_tag), simpleprint=False, tprint=True)

    global cur
    if cur == None:
        logerror(funcname, strErrCursor, strErrConn, simpleprint=False)
        return -1

    if discord_id_tag == None:
        logerror(funcname, 'discord_id_tag == None; returning -1', simpleprint=False)
        return -1

    #resultCnt = cur.execute(f"select GetPlayerIDFrom_DiscIdTag('{discord_id_tag}');")
    #player_id = -1 if resultCnt == 0 else cur.fetchone()['id']
    player_id = cur.execute(f"select GetPlayerIDFrom_DiscIdTag('{discord_id_tag}');")
    return player_id


#====================================================#
##              select statement support            ##
#====================================================#
def selectFromTableWithDbQueryDict(table, selectDict, dbWhereQueryDict={}, discord_id_tag=None):
    funcname = '(%s) selectFromTableWithDbQueryDict' % filename
    logenter(funcname, 'table: %s; selectDict: %s; dbWhereQueryDict: %s; discord_id_tag: %s' % (table, selectDict, dbWhereQueryDict, discord_id_tag), simpleprint=False, tprint=False)

    ############# open db connection ###############
    global cur
    if open_database_connection() < 0:
        return -1

    if cur == None:
        logerror(funcname, strErrCursor, strErrConn, simpleprint=False)
        return -1

    strCols = getColsStrFromQueryDict(selectDict)
    strWhere = getSetWhereStrFromQueryDict(dbWhereQueryDict, delimiter='or')

    ## perform db query ##
    try:
        strQuery = f"select {strCols} from {table};"
        if discord_id_tag is not None:
            player_id = procGetPlayerIDFrom(discord_id_tag)
            strWhere = appendWhereStr(strWhere, f"{cColPlayerId} = '{player_id}'")
            strQuery = f"select {strCols} from {table} where {strWhere};"

        rowCnt = cur.execute(strQuery)
        rows = -1 if rowCnt == 0 else cur.fetchall()
        loginfo(funcname, ' >> SELECT RESULT rows: %s; QUERY table: %s; selectDict: %s; dbWhereQueryDict: %s; discord_id_tag: %s' % (rows,table,selectDict,dbWhereQueryDict,discord_id_tag), simpleprint=True)
    except Exception as e: # ref: https://docs.python.org/2/tutorial/errors.html
        strE_0 = "Exception hit... \nFAILED to select from table: %s; cols: %s; strWhere: %s; \nreturning -1" % (table, strCols, strWhere)
        strE_1 = "\n __Exception__: \n%s\n __Exception__" % e
        logerror(funcname, strE_0, strE_1, simpleprint=False)
        result = -1
    finally:
        ############# close db connection ###############
        close_database_connection()

        return rows


#====================================================#
##              insert statement support            ##
#====================================================#
def insertIntoTableWithDbQueryDict(table, dbQueryDict, discord_id_tag=None):
    funcname = '(%s) insertIntoTableWithDbQueryDict' % filename
    logenter(funcname, 'table: %s; dbQueryDict: %s; discord_id_tag: %s' % (table, dbQueryDict, discord_id_tag), simpleprint=False, tprint=True)

    ############# open db connection ###############
    global cur
    if open_database_connection() < 0:
        return -1

    if cur == None:
        logerror(funcname, strErrCursor, strErrConn, simpleprint=False)
        return -1

    strCols = getColsStrFromQueryDict(dbQueryDict)
    strVals = getInsertValsStrFromQueryDict(dbQueryDict)

    ## perform db query ##
    try:
        if discord_id_tag is not None:
            player_id = procGetPlayerIDFrom(discord_id_tag)
#            if table == cTblePlayer and player_id > 0:
#                #TODO: call update statement instead of insert
            strCols += f", {cCol_player_id}"
            strVals += f", '{player_id}'"

        strQuery = f"insert into {table} ({strCols}) VALUES ({strVals});"
        cur.execute(strQuery)
        id_of_new_row = cur.lastrowid
        loginfo(funcname, ' >> INSERT RESULT id: %s; QUERY table: %s; dbQueryDict: %s; discord_id_tag: %s' % (id_of_new_row,table,dbQueryDict,discord_id_tag), simpleprint=True)
    except Exception as e: # ref: https://docs.python.org/2/tutorial/errors.html
        strE_0 = "Exception hit... \nFAILED to insert into table: %s; cols: %s; vals: %s; \nreturning -1" % (table, strCols, strVals)
        strE_1 = "\n __Exception__: \n%s\n __Exception__" % e
        logerror(funcname, strE_0, strE_1, simpleprint=False)
        id_of_new_row = -1
    finally:
        ############# close db connection ###############
        close_database_connection()

        return id_of_new_row


#====================================================#
##              update statement support            ##
#====================================================#
def updateTableWithDbQueryDict(table, dbSetQueryDict, dbWhereQueryDict):
    funcname = '(%s) updateTableWithDbQueryDict' % filename
    logenter(funcname, 'table: %s; dbSetQueryDict: %s; dbWhereQueryDict: %s;' % (table, dbSetQueryDict, dbWhereQueryDict), simpleprint=False, tprint=True)

    ############# open db connection ###############
    global cur
    if open_database_connection() < 0:
        return -1

    if cur == None:
        logerror(funcname, strErrCursor, strErrConn, simpleprint=False)
        return -1

    strSet = getSetWhereStrFromQueryDict(dbSetQueryDict, delimiter=',')
    strWhere = getSetWhereStrFromQueryDict(dbWhereQueryDict, delimiter='or')

    #update player set discord_id_name = 'updatedName', description = 'hello world descr' where discord_id_full = 'temp37#3333' or discord_id_tag = '#4444';
    ## perform db query ##
    try:
        strQuery = f"update {table} set {strSet} where {strWhere};"
        cur.execute(strQuery)
        id_of_new_row = cur.lastrowid
        loginfo(funcname, ' >> UPDATE RESULT id: %s' % id_of_new_row, simpleprint=True)
    except Exception as e: # ref: https://docs.python.org/2/tutorial/errors.html
        strE_0 = "Exception hit... \nFAILED to update table: %s; set: %s; where: %s; \nreturning -1" % (table, strSet, strWhere)
        strE_1 = "\n __Exception__: \n%s\n __Exception__" % e
        logerror(funcname, strE_0, strE_1, simpleprint=False)
        id_of_new_row = -1
    finally:
        ############# close db connection ###############
        close_database_connection()

        return id_of_new_row

#====================================================#
#====================================================#




loginfo(filename, "\n CLASSES & FUNCTIONS initialized:- STARTING -> additional '%s' run scripts (if applicable) . . . \n\n" % filename, simpleprint=True)


print('\n')
print('#======================================================================#')
loginfo(filename, "\n  DONE Executing additional '%s' run scripts ... \n" % filename, simpleprint=True)


