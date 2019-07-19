print('GO torrent.py -> starting IMPORTs')
from sites import *
from utilities import *
import time # new
from flask import request, redirect,Response

filename = 'torrent.py'
logenter(filename, "\n IMPORTs complete:- STARTING -> file '%s' . . . " % filename, simpleprint=False, tprint=True)



#=======================================================================#
## test function ##                                                     #
def test():                                                             #
    loginfo(filename, "request_agents.%s.py test we did it!" % filename)#
    return "request_agents.%s.py test we did it!" % filename            #
#=======================================================================#

#============================================#
## torrentscrape database helpers      ##
#============================================#

#=======================================================================#
## GET last scrape ##
#
# @endpoint: GET|POST /api/get/scrape/last
# <none>
#
# @params required: <none>
#         optional: <none>
# @descr:
#   note: ...
#   1) validate required params & set local vars                          #
#   2) get settings db tbl entries                                        #
#   3) prepare return json model                                          #
# @returnjson:
#  {'ERROR':<vErr>,
#   'MSG':'<err/status msg>',
#   'PAYLOAD':{'error':<vErr>, 'torrent_arr':[sel_keys_tbl_torrent, ...],
#              'auth_token':<new auth_token>}}
#
#        sel_keys_tbl_torrent  = ['id',
#                                 'fk_scrape_inst_id',
#                                 'scrape_idx',
#                                 'scrape_pg_num',
#                                 'info_hash',
#                                 'seed_cnt',
#                                 'leech_cnt',
#                                 'file_size',
#                                 'scrape_href_title',
#                                 'scrape_href',
#                                 'mag_link',
#                                 'dt_created',
#                                 'dt_updated']
#=======================================================================#
def getLatestScrape(request):
    funcname = '(%s) getLatestScrape' % filename
    logenter(funcname, simpleprint=False, tprint=False)
    
    # note: utilizing additional dict here (instead of just request.form/args)
    #   because we want to be secure the params passed to the database are only the keys we want
    reqParamsImmutDict = request.form

    #=======================================================================#
    # 1) validate required params & set local vars                          #
    #=======================================================================#
    # <none>

    #=======================================================================#
    # 2) get settings db tbl                                                #
    #=======================================================================#
    selrows = procCallGetLatestScrape()
    
    #loginfo(funcname, '\n\nselrows: %s\n\n' % selrows, '')
    if selrows == -1: # validate db errors #
        err_resp_db = {'ERROR':vErrDb, 'MSG':kErrDb, 'PAYLOAD':{'error':vErrDb}}
        return JSONResponse (err_resp_db)

    #=======================================================================#
    # 3) prepare return json model                                          #
    #=======================================================================#
    l = []
    for row in selrows:
        jsonRow = getJsonDictFromDBQueryRowWithKeys(row, sel_keys_tbl_torrent)
        l.append (jsonRow) # append this json return list entry #

    payloaddict = {'error':vErrNone,'torrent_arr':l,'auth_token':"TODO ; )"}
    #logexit(funcname, 'return error:0', '\npayloaddict: %s\n' % payloaddict)
    logexit(funcname, 'return error:0', 'payloaddict: <print disabled>\n')
    return JSONResponse ({'ERROR':vErrNone,'MSG':'get latest successfully!','PAYLOAD':payloaddict})

def getLatestScrapeSubType(request, subType):
    funcname = '(%s) getLatestScrapeSubType' % filename
    logenter(funcname, simpleprint=False, tprint=True)

    selrows = procCallGetLatestScrapeSubType(subType)
    #loginfo(funcname, '\n\nselrows: %s\n\n' % selrows, '')
    if selrows == -1: # validate db errors #
        err_resp_db = {'ERROR':vErrDb, 'MSG':kErrDb, 'PAYLOAD':{'error':vErrDb}}
        return JSONResponse (err_resp_db)

    l = []
    for row in selrows:
        jsonRow = getJsonDictFromDBQueryRowWithKeys(row, sel_keys_tbl_torrent)
        l.append (jsonRow) # append this json return list entry #

    payloaddict = {'error':vErrNone,'torrent_arr':l,'auth_token':"TODO ; )"}
    #logexit(funcname, 'return error:0', '\npayloaddict: %s\n' % payloaddict)
    logexit(funcname, 'return error:0', 'payloaddict: <print disabled>\n')
    return JSONResponse ({'ERROR':vErrNone,'MSG':'get latest successfully!','PAYLOAD':payloaddict})

######################################################################





