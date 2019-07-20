print('\n\nSTART _ torrentscrape.py \n\n')
import logging
import json
import sites #required: sites/__init__.py
from request_agents import * #imports 'from sites import *'
from utilities import *
from flask import Flask
from flask import request, redirect,Response

GLOBAL_PATH_DEV_LOGS = sites.GLOBAL_PATH_DEV_LOGS
GLOBAL_PATH_ISE_LOGS = sites.GLOBAL_PATH_ISE_LOGS

filename = 'torrentscrape.py'
logenter(filename, "\n IMPORTs complete:- STARTING -> file '%s' . . . " % filename, simpleprint=False, tprint=True)

logging.basicConfig(filename=GLOBAL_PATH_DEV_LOGS, level=logging.DEBUG)
logging.info('*======================================================================*')
logging.info('*                 server started -> torrentscrape.py called            *')
logging.info('*======================================================================*')

app = Flask(__name__)

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
@app.route('/')
def slash():
    return "Why would you go with just '/'? Are you trying access the root? --> :P torrentscrape"

@app.route('/api', methods=['GET', 'POST'])
def slash_api():
    return "/api successful! torrentscrape"

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

kPathGetScrapeLast1 = '/api/get/scrape/last/1'
kPathGetScrapeLast2 = '/api/get/scrape/last/2'
kPathGetScrapeLast3 = '/api/get/scrape/last/3'
kPathGetScrapeLast4 = '/api/get/scrape/last/4'
kPathGetScrapeLast5 = '/api/get/scrape/last/5'
kPathGetScrapeLast6 = '/api/get/scrape/last/6'
kPathGetScrapeLast7 = '/api/get/scrape/last/7'
kPathGetScrapeLast8 = '/api/get/scrape/last/8'


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
    #logging.info('%s %s \'%s\'  %s' % (strUriHit, lst_MethGetScrapeLast, kPathGetScrapeLast, strUriHit))
    logenter(filename, f"{strUriHit} {lst_MethGetScrapeLast} '{kPathGetScrapeLast}'  {strUriHit}")
    return getLatestScrape(request)

@app.route(kPathGetScrapeLast1, methods=lst_MethGetScrapeLast)
def GetAllLatest1():
    logenter(filename, f"{strUriHit} {lst_MethGetScrapeLast} '{kPathGetScrapeLast}'  {strUriHit}")
    return getLatestSubType(request, subType=1)

@app.route(kPathGetScrapeLast2, methods=lst_MethGetScrapeLast)
def GetAllLatest2():
    logenter(filename, f"{strUriHit} {lst_MethGetScrapeLast} '{kPathGetScrapeLast}'  {strUriHit}")
    return getLatestSubType(request, subType=2)

@app.route(kPathGetScrapeLast3, methods=lst_MethGetScrapeLast)
def GetAllLatest3():
    logenter(filename, f"{strUriHit} {lst_MethGetScrapeLast} '{kPathGetScrapeLast}'  {strUriHit}")
    return getLatestSubType(request, subType=3)

@app.route(kPathGetScrapeLast4, methods=lst_MethGetScrapeLast)
def GetAllLatest4():
    logenter(filename, f"{strUriHit} {lst_MethGetScrapeLast} '{kPathGetScrapeLast}'  {strUriHit}")
    return getLatestSubType(request, subType=4)

@app.route(kPathGetScrapeLast5, methods=lst_MethGetScrapeLast)
def GetAllLatest5():
    logenter(filename, f"{strUriHit} {lst_MethGetScrapeLast} '{kPathGetScrapeLast}'  {strUriHit}")
    return getLatestSubType(request, subType=5)

@app.route(kPathGetScrapeLast6, methods=lst_MethGetScrapeLast)
def GetAllLatest6():
    logenter(filename, f"{strUriHit} {lst_MethGetScrapeLast} '{kPathGetScrapeLast}'  {strUriHit}")
    return getLatestSubType(request, subType=6)

@app.route(kPathGetScrapeLast7, methods=lst_MethGetScrapeLast)
def GetAllLatest7():
    logenter(filename, f"{strUriHit} {lst_MethGetScrapeLast} '{kPathGetScrapeLast}'  {strUriHit}")
    return getLatestSubType(request, subType=7)

@app.route(kPathGetScrapeLast8, methods=lst_MethGetScrapeLast)
def GetAllLatest8():
    logenter(filename, f"{strUriHit} {lst_MethGetScrapeLast} '{kPathGetScrapeLast}'  {strUriHit}")
    return getLatestSubType(request, subType=8)

def getLatestSubType(request, subType=0):
    logenter(filename, f"request: {request}; subType: {subType}")
    return getLatestScrapeSubType(request, subType)



loginfo(filename, "\n CLASSES & FUNCTIONS initialized:- STARTING -> additional '%s' run scripts (if applicable) . . . \n\n" % filename, simpleprint=True)
print('\n')
print('#======================================================================#')
loginfo(filename, "\n  DONE Executing additional '%s' run scripts ... \n" % filename, simpleprint=True)





