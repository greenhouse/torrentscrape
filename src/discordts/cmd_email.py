print('GO cmd_email.py -> starting IMPORTs')
#from sites import *
from utilities import *
from .db_dm4c import *
from .discord_util import *
#from binance_dm4c import *

filename = 'cmd_email.py'
logenter(filename, "\n IMPORTs complete:- STARTING -> file '%s' . . . " % filename, simpleprint=False, tprint=True)

#====================================================#
# globals                                            #
#====================================================#

#====================================================#
##              validation support                  ##
#====================================================#
def validStrFormatEmail(strEmail):
    funcname = '(%s) validStrFormatEmail' % filename
    logenter(funcname, f'(strEmail={strEmail})', simpleprint=False, tprint=False)

    iStrLen = len(strEmail)
    if iStrLen < 1 or iStrLen > 30:
        logerror(funcname, f"'{strEmail}' lenght > 30; returning False")
        return False

    return True

#====================================================#
##              response msg support                ##
#====================================================#
def getErrorRespMsg():
    msg = f"  We found an error with your request... ```\n  please try again \n  you can use \"!RegisterEmail\" or \"!help\" for more info ```"
    return msg

#====================================================#
##              database support                    ##
#====================================================#
def DBQueryMemberRegisterEmail(member, strEmail):
    user = userDictFromDiscordMem(member)
    dict = {cColPlayerDiscIdFull:user['userFull'],
            cColPlayerDiscIdTag:user['userHashTagId'],
            cColPlayerFirstIpAddr:'no-ip-record',
            cColPlayerEmail:strEmail}
    result = procCallMemberRegisterEmail(dbQueryDict=dict)
    return result

#====================================================#
##              main exec                           ##
#====================================================#
def CMD_email(member, lst_strMsg):
    funcname = '(%s) CMD_email' % filename
    logenter(funcname, f'(member={member}, lst_strMsg={lst_strMsg})', simpleprint=False, tprint=False)
    
    iCmdLen = len(lst_strMsg)
    
    # if only '!deposit' cmd string was received
    if iCmdLen == 1:
        strCurrCmd = lst_strMsg[0]
        usage = "  Commands..."
        usage += f"\n    {strCurrCmd} {cCmdEmailExample}"
        msg = f"  In order provide additional security for your account/funds, please provide your email address by using the following example command (your email will never be used for solicitation, marketing, or advertising) \n``` {usage} ```"
        loginfo(funcname, f'CMD Msg Response: \n{msg}', simpleprint=True)
        return msg
    
    # validate email string (2nd string in lst_strMsg) is properly formatted
    strEmail = lst_strMsg[1]
    if iCmdLen == 2 and validStrFormatEmail(strEmail):
        result = DBQueryMemberRegisterEmail(member, strEmail)
        
        usage = "If you would like to update your registered email at any time, simply use the '!RegisterEmail' command again."
        msg = f"  Your email ``{strEmail}`` has been successfully registered for your discord user ({member})\n```{usage}```"
        if result < 0:
            msg = getErrorRespMsg()
        loginfo(funcname, f'CMD Msg Response: \n{msg}', simpleprint=True)
        return msg

    for msg in lst_strMsg[0:]:
        subcmd = msg.lower()
        lst_depositTypes = [x.lower() for x in cCmd_lst_deposit_types]
        loginfo(funcname, f'   subcmd: {msg}', simpleprint=True)
        if subcmd in lst_depositTypes:
            loginfo(funcname, f'subcmd: {subcmd}', simpleprint=True)

    msg = getErrorRespMsg()
    loginfo(funcname, f'CMD Msg Response: \n{msg}', simpleprint=True)
    return msg


loginfo(filename, "\n CLASSES & FUNCTIONS initialized:- STARTING -> additional '%s' run scripts (if applicable) . . . \n\n" % filename, simpleprint=True)

#print('\n')
#print('#======================================================================#')
#loginfo(filename, "\n  DONE Executing additional '%s' run scripts ... \n" % filename, simpleprint=True)


