print('\n\nSTART _ torrentscrape.py \n\n')
import logging
import json
import sites #required: sites/__init__.py
from request_agents import *
from flask import Flask
from flask import request, redirect,Response

#import time
#from datetime import datetime
#from threading import Timer

GLOBAL_PATH_DEV_LOGS = sites.GLOBAL_PATH_DEV_LOGS
GLOBAL_PATH_ISE_LOGS = sites.GLOBAL_PATH_ISE_LOGS

logging.basicConfig(filename=GLOBAL_PATH_DEV_LOGS, level=logging.DEBUG)
logging.info('*======================================================================*')
logging.info('*                 server started -> torrentscrape.py called            *')
logging.info('*======================================================================*')

app = Flask(__name__)

#runloop.startrunloop()

if __name__ == '__main__':
    app.run() #app.run(debug=True)

if not app.debug:
    from logging import FileHandler
    file_handler = FileHandler(GLOBAL_PATH_ISE_LOGS)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

#=====================================================#
### testing endpoints ###
#=====================================================#
@app.route('/api')
def slash():
    return "Why would you go with just '/'? Are you trying access the root? --> :P torrentscrape"

@app.route('/api/request', methods=['GET', 'POST'])
def slash_request():
    return "/request successful! torrentscrape"

@app.route('/api/request/test', methods=['GET', 'POST'])
def slash_request_test():
    return "/request/test successful! torrentscrape"


#=====================================================#
## NOTES ##
# ref: https://www.quora.com/What-is-the-technology-stack-behind-Uber?redirected_qid=572124
#   (psql plugin good for map integration: Postgis)
#
# Http Requests
#   Default:
#       content-type : application/x-www-form-urlencoded 
#       (example: m_phone=1234567890&f_name=helloworld)
#
#   TODO: research setting json content-type
#       content-type : application/json
#       (example: easyHttp & wireshark testing needed)
#=====================================================#

#=====================================================#
#         torrentscrape Browser Client Endpoints      #
#=====================================================#

#====================================#
## torrentscrape request paths & methods ##
#====================================#
strUriHit = ' :-- URI hit --: '

#===================================#
# SETTINGS
kPathGetInitSett = '/api/getinit/settings' # get initial settings
lst_MethGetInitSett = ['POST']

#====================================#
# GET scrape last
kPathGetScrapeLast = '/api/get/scrape/last'
lst_MethGetScrapeLast = ['GET', 'POST']

##====================================#
### SETTINGS/OTHER request apis      ##
##====================================#
# GET initial settings for torrentscrape
#@app.route(kPathGetInitSett, methods=lst_MethGetInitSett)
#def GetInitSettings():
#    logging.info('%s %s \'%s\'  %s' % (strUriHit, lst_MethGetInitSett, kPathGetInitSett, strUriHit))
#    return request_agents.settings.getInitSettings(request)

#====================================#
## torrentscrape data request apis  ##
#====================================#
# GET all db entries from latest scrape
@app.route(kPathGetScrapeLast, methods=lst_MethGetScrapeLast)
def GetAllLatest():
    logging.info('%s %s \'%s\'  %s' % (strUriHit, lst_MethGetScrapeLast, kPathGetScrapeLast, strUriHit))
    #logging.info(f"{strUriHit} {lst_MethGetScrapeLast} '{kPathGetScrapeLast}'  {strUriHit}")
    return request_agents.torrent.getLatest(request)










