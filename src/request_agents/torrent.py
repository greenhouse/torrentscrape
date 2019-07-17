print('GO torrent.py -> starting IMPORTs')
from utilities import *
import logging
#from request_agents import helpers
import time # new

#from controllers import parser
#from controllers import database
#from controllers import s3support
#from controllers import xlogger
#from controllers import runloop
#from controllers import apns
#from controllers import email

#from flask import Flask
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
## GET INIT SETTINGS (min_ios_ver) in the 'settings' db table ##
#
# @endpoint: POST /api/getinit/settings
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
#   'PAYLOAD':{'error':<vErr>, 'settings_arr':[sel_keys_tbl_torrent, ...],
#              'auth_token':<new auth_token>}}
#
#       sel_keys_tbl_settings = ['id','dt_created','dt_updated','min_ios_ver','min_droid_ver'
#                                'url_img_splash']
#=======================================================================#
def getLatestScrape(request):
    funcname = '(%s) getLatestScrape' % filename
    logenter(funcname, simpleprint=False, tprint=True)
    
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
#    selrows = database.selectAllFromTableOrderByColDescAsc('settings', 'id', 'desc')
    selrows = procCallGetLatestScrape()
    
    #loginfo(funcname, '\n\nselrows: %s\n\n' % selrows, '')
    if selrows == -1: # validate db errors #
        err_resp_db = {'ERROR':vErrDb, 'MSG':kErrDb, 'PAYLOAD':{'error':vErrDb}}
        return JSONResponse (err_resp_db)

    #=======================================================================#
    # 3) prepare return json model                                          #
    #=======================================================================#
    l = []
    sel_keys_tbl_torrent  = ['id',
                             'fk_scrape_inst_id',
                             'scrape_idx',
                             'scrape_pg_num',
                             'info_hash',
                             'seed_cnt',
                             'leech_cnt',
                             'file_size',
                             'scrape_href_title',
                             'scrape_href',
                             'mag_link',
                             'dt_created',
                             'dt_updated']
    for row in selrows:
        jsonRow = getJsonDictFromDBQueryRowWithKeys(row, sel_keys_tbl_torrent)
        l.append (jsonRow) # append this json return list entry #

    payloaddict = {'error':vErrNone,'torrent_arr':l,'auth_token':"TODO ; )"}
    #logexit(funcname, 'return error:0', '\npayloaddict: %s\n' % payloaddict)
    logexit(funcname, 'return error:0', '\npayloaddict: <print disabled\n')
    return JSONResponse ({'ERROR':vErrNone,'MSG':'get latest successfully!','PAYLOAD':payloaddict})

######################################################################





