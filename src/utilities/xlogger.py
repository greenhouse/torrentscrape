print('GO xlogger.py -> starting IMPORTs')
import logging
import time
from datetime import datetime
import sites #required: sites/__init__.py

logging.basicConfig(filename=sites.GLOBAL_PATH_DEV_LOGS, level=logging.DEBUG)
logging.info(' ')
logging.info('logging started -> ./xlogger.py')


#enable_debug_log = True
enable_debug_log = False


legstar   = '***************************'
todostar  = '********************************************'
errstar   = '*****************************************'
enterstar = '*******************'
exitstar  = '*******************'
infostar  = '******************'
alertstar   = '************************************** '
warnstar   = '************************************** <WARNING>'
debugstar   = '**** DEBUG **** DEBUG **** DEBUG ****'

strerror = '<ERROR>'
strenter = '<ENTER>'
strexit = '<EXIT>'
strinfo = '<INFO>'
strevent = '<EVENT>'
stralert = '<ALERT>'
strwarn = '<WARNING>'
strdebug = '<DEBUG>'


strtodo = '<TODO>'
strlegacy = '<legacy log>'

###################################################################
############ function ############
###################################################################
def logtodo(funcname, prefix, suffix):
    timenow = '%s' % int(round(time.time()))
    logging.info('[%s] _ %s  %s %s %s %s %s' % (timenow, strtodo, funcname, prefix, todostar, suffix, strtodo))

def logerror(funcname, prefix='', suffix='', simpleprint=False, tprint=True, timeconv=True):
    timenow = '%s' % int(round(time.time()))
    if timeconv:
        timenow = datetime.fromtimestamp(int(timenow))
    logging.info('\n\n[%s] _ %s  %s %s %s %s %s' % (timenow, strerror, funcname, prefix, errstar, suffix, strerror))
    if tprint:
        if simpleprint:
            simplePrint(prefix, suffix)
        else:
            print('\n\n[%s] _ %s  %s %s\n\n  * * * *   * * * *   * * * *   * * * *   * * * *\n\n%s \n%s\n\n  * * * *   * * * *   * * * *   * * * *   * * * *\n\n' % (timenow, strerror, funcname, strerror, prefix, suffix))

def logenter(funcname, prefix='', suffix='', simpleprint=False, tprint=True, timeconv=True):
    timenow = '%s' % int(round(time.time()))
    if timeconv:
        timenow = datetime.fromtimestamp(int(timenow))
    logging.info('[%s] _ %s  %s %s %s %s %s' % (timenow, strenter, funcname, prefix, enterstar, suffix, strenter))
    if tprint:
        if simpleprint:
            simplePrint(prefix, suffix)
        else:
            print('\n[%s] _ %s  %s  %s\n%s %s\n' % (timenow, strenter, funcname, strenter, prefix, suffix))

def logexit(funcname, prefix='', suffix='', error=0, simpleprint=False, tprint=True, timeconv=True):
    timenow = '%s' % int(round(time.time()))
    if timeconv:
        timenow = datetime.fromtimestamp(int(timenow))
    logging.info('[%s] _ %s  %s %s %s %s %s' % (timenow, strexit, funcname, prefix, exitstar, suffix, strexit))
    if tprint:
        if simpleprint:
            simplePrint(prefix, suffix)
        else:
            print('[%s] _ %s  %s [err %s]: %s %s %s\n' % (timenow, strexit, funcname, error, prefix, suffix, strexit))

def loginfo(funcname, prefix='', suffix='', simpleprint=False, tprint=True, timeconv=True):
    timenow = '%s' % int(round(time.time()))
    if timeconv:
        timenow = datetime.fromtimestamp(int(timenow))
    logging.info('[%s] _ %s  %s %s %s %s %s' % (timenow, strinfo, funcname, prefix, infostar, suffix, strinfo))
    if tprint:
        if simpleprint:
            simplePrint(prefix, suffix)
        else:
            print('[%s] _ %s  %s %s\n%s %s\n' % (timenow, strinfo, funcname, strinfo, prefix, suffix))

def logevent(funcname, prefix='', suffix='', simpleprint=False, tprint=True):
    timenow = '%s' % int(round(time.time()))
    logging.info('[%s] _ %s  %s %s %s %s %s' % (timenow, strevent, funcname, prefix, infostar, suffix, strevent))
    if tprint:
        if simpleprint:
            simplePrint(prefix, suffix)
        else:
            print('[%s] _ %s  %s %s\n %s %s\n' % (timenow, strevent, funcname, strevent, prefix, suffix))

def logprint(funcname, prefix, suffix):
    timenow = '%s' % int(round(time.time()))
    logging.info('[%s] _ %s  %s %s %s %s %s' % (timenow, strevent, funcname, prefix, infostar, suffix, strevent))
    print('[%s] _ %s  %s %s\n%s %s\n' % (timenow, strevent, funcname, strevent, prefix, suffix))

def logalert(funcname, prefix='', suffix='', simpleprint=False, tprint=True, timeconv=True):
    timenow = '%s' % int(round(time.time()))
    if timeconv:
        timenow = datetime.fromtimestamp(int(timenow))
    logging.info('[%s] _ %s  %s %s %s %s %s' % (timenow, stralert, funcname, prefix, alertstar, suffix, stralert))
    if tprint:
        if simpleprint:
            simplePrint(prefix, suffix)
        else:
            print('[%s] _ %s  %s  %s \n%s\n %s %s \n%s %s\n' % (timenow, stralert, funcname, stralert, alertstar, prefix, suffix, alertstar, stralert))

def logwarn(funcname, prefix='', suffix='', simpleprint=False, tprint=True, timeconv=True):
    timenow = '%s' % int(round(time.time()))
    if timeconv:
        timenow = datetime.fromtimestamp(int(timenow))
    logging.info('[%s] _ %s  %s %s %s %s %s' % (timenow, strwarn, funcname, prefix, warnstar, suffix, strwarn))
    if tprint:
        if simpleprint:
            prefix = warnstar+'\n '+prefix
            suffix = ' '+suffix+'\n '+warnstar
            simplePrint(prefix, suffix)
        else:
            print('[%s] _ %s  %s  %s \n%s\n %s %s \n%s\n' % (timenow, strwarn, funcname, strwarn, warnstar, prefix, suffix, warnstar))

def logdebug(funcname, prefix, suffix):
    timenow = '%s' % int(round(time.time()))
    logging.info('[%s] _ %s  %s %s %s %s %s' % (timenow, strdebug, funcname, prefix, debugstar, suffix, strdebug))

def simplePrint(prefix, suffix):
    print(' %s %s' % (prefix, suffix))













