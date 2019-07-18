print('GO cmd_deposit.py -> starting IMPORTs')
from constants import *
from db_dm4c import *
from discord_util import *
from binance_dm4c import *

'''
# https://discordapp.com/developers/applications/
# https://discordapp.com/oauth2/authorize?client_id=588170504503033856&scope=bot&permissions=8
#NOTE: '$ pip3' == '$ python3.6 -m pip'
    $ pip3 install discord.py
    $ python3.6 -m pip install discord.py
'''
#import discord
# $ python3 server.join.py

filename = 'cmd_deposit.py'
logenter(filename, "\n IMPORTs complete:- STARTING -> file '%s' . . . " % filename, simpleprint=False, tprint=True)

#====================================================#
# globals                                            #
#====================================================#


#====================================================#
##              list comprehension support          ##
#====================================================#
def getDepositTypes():
    lst_depositTypes = [x.lower() for x in cCmd_lst_deposit_types]
    return lst_depositTypes

def getDepositCryptosList():
    lst_depositCryptos = [x.lower() for x in cCmd_lst_deposit_cryptos]
    return lst_depositCryptos

def getDepositUsdList():
    lst_depositUsd = [x.lower() for x in cCmd_lst_deposit_usd]
    return lst_depositUsd

#====================================================#
##              validation support                  ##
#====================================================#
def validStrFormatUSD(strUSD):
    funcname = '(%s) validStrFormatUSD' % filename
    logenter(funcname, f'(strUSD={strUSD})', simpleprint=False, tprint=False)

    if not strUSD.startswith('$'):
        logerror(funcname, f"'{strUSD}' does not start with '$'; returning False")
        return False

    strValue = strUSD[1:]
    try:
        value = float(strValue)
        strPrint = f'strUSD: {strUSD}; \n strValue: {strValue}; \n value: {value}; \n returning True'
        loginfo(funcname, strPrint, simpleprint=True, tprint=False)
        return True
    except ValueError as e:
        strE_0 = f"Exception hit... \nFAILED cast to float: float({strUSD}); \nreturning False"
        strE_1 = f"\n __Exception__: \n{e}\n __Exception__"
        logerror(funcname, strE_0, strE_1, simpleprint=False)
        return False

#====================================================#
##              deposit address support             ##
#====================================================#
def getDepositAddrForSymb(strAltSymb):
    funcname = '(%s) getDepositAddrForSymb' % filename
    logenter(funcname, f'(strAltSymb={strAltSymb})', simpleprint=False, tprint=False)

    strAltSymb = strAltSymb.upper()
    if strAltSymb in cWallet_dict_addr:
        return cWallet_dict_addr[strAltSymb]
    else:
        logerror(funcname, f'no deposit address for {strAltSymb}; \n returning None', simpleprint=False)
        return None

def getDepositAddrForCashAcct(strCashAcct):
    funcname = '(%s) getDepositAddrForCashAcct' % filename
    logenter(funcname, f'(strCashAcct={strCashAcct})', simpleprint=False, tprint=False)

    strCashAcct = strCashAcct.upper()
    if strCashAcct in cCash_dict_addr:
        return cCash_dict_addr[strCashAcct]
    else:
        logerror(funcname, f'no deposit address for {strCashAcct}; \n returning None', simpleprint=False)
        return None

#====================================================#
##              response msg support                ##
#====================================================#
def getErrorRespMsg():
    msg = f"  We found an error with your request... ```\n  please try again \n  you can use \"!deposit\" or \"!help\" for more info ```"
    return msg

def getUsageRespMsg(member, strCurrType):
    funcname = '(%s) getUsageRespMsg' % filename
    logenter(funcname, f'(member={member}, strCurrType={strCurrType})', simpleprint=False, tprint=False)
    usage = (f"```Please include your current discord 'name#id' ({member}) within the {strCurrType.upper()} transaction description.``` \n"
             "```After your deposit is processed, you will receive a confirmation with the fivem server IP address to use for 'Direct Connect'```")
    return usage

def getDepositCryptoRespMsg(member, strCurrType, usdAmnt, usage):
    funcname = '(%s) getDepositCryptoRespMsg' % filename
    logenter(funcname, f'(member={member}, strCurrType={strCurrType}, usdAmnt=${usdAmnt}, usage=...)', simpleprint=False, tprint=False)
    
    lst_binanceSymbFull = [x for x in cSymb_lst_binance if strCurrType == x.lower()[:3]]
    loginfo(funcname, f'lst_binanceSymbFull: {lst_binanceSymbFull}', simpleprint=True, tprint=False)
    
    symbFull = lst_binanceSymbFull[0]
    depositAmnt = convertUSD_toAltSymbAmnt(usdAmnt=usdAmnt, altSymbFull=symbFull)
    depositAddr = getDepositAddrForSymb(strCurrType)
    if depositAddr is None:
        return getErrorRespMsg()
    
    pctid = DBQueryMemberDepRequest(member, cCurreny_dict_types[strCurrType.upper()], depositAmnt, usdAmnt, depositAddr)
    msg = f"  Please send {depositAmnt} {strCurrType.upper()} to the following address \n``` {depositAddr} ```\n{usage}\n```PTCID[{pctid}]```"
    return msg

def getDepositUsdRespMsg(member, strCurrType, usdAmnt, usage):
    funcname = '(%s) getDepositUsdRespMsg' % filename
    logenter(funcname, f'(member={member}, strCurrType={strCurrType}, usdAmnt=${usdAmnt}, usage=...)', simpleprint=False, tprint=False)
    
    depositAddr = getDepositAddrForCashAcct(strCurrType)
    if depositAddr is None:
        return getErrorRespMsg()
    
    pctid = DBQueryMemberDepRequest(member, cCurreny_dict_types[cCmdDepositDHT], usdAmnt, usdAmnt, depositAddr)
    msg = f"  Please send ${usdAmnt} via '{strCurrType}' using the following address \n``` {depositAddr} ```\n{usage}```PTCID[{pctid}]```"
    return msg

#====================================================#
##              database support                    ##
#====================================================#
def DBQueryMemberDepRequest(member, currTypeId, currValue, dhtValue, depositAddr):
    user = userDictFromDiscordMem(member)
    dict = {cColPlayerDiscIdFull:user['userFull'],
            cColPlayerDiscIdTag:user['userHashTagId'],
            cColPlayerFirstIpAddr:'no-ip-record',
            cColCurrTypeId:currTypeId,
            cColCurrValue:currValue,
            cColDhtValue:dhtValue,
            cColDepositAddr:depositAddr,
            cColOutPTCID:0}
    player_trans_curr_id = procCallMemberDepositRequest(dbQueryDict=dict)
    return player_trans_curr_id

#====================================================#
##              main exec                           ##
#====================================================#
def CMD_deposit(member, lst_strMsg):
    funcname = '(%s) CMD_deposit' % filename
    logenter(funcname, f'(member={member}, lst_strMsg={lst_strMsg})', simpleprint=False, tprint=False)
    
    iCmdLen = len(lst_strMsg)
    
    # if only '!deposit' cmd string was received
    if iCmdLen == 1:
        strCurrCmd = lst_strMsg[0]
        usage = "  Commands..."
        for sub in cCmd_list_deposit_amnts:
            usage += f"\n    {strCurrCmd} {sub}"
        
        msg = f"  Please choose a deposit amount (by using one of the following commands) ```\n{usage} ```"
        loginfo(funcname, f'CMD Msg Response: \n{msg}', simpleprint=True)
        return msg
    
    # validate USD string (2nd string in lst_strMsg) is properly formatted
    strUSD = lst_strMsg[1]
    if validStrFormatUSD(strUSD):

        usdAmnt = float(strUSD[1:])
        
        if iCmdLen == 2:
            #strCurrCmd = ' '.join(lst_strMsg[:2])
            strCurrCmd = ' '.join(lst_strMsg)
            usage = "  Commands..."
            for sub in cCmd_lst_deposit_types:
                usage += f"\n    {strCurrCmd} with {sub}"

            msg = f"  Now, please choose a deposit method (by using one of the following commands) ```\n{usage} ```"
            loginfo(funcname, f'CMD Msg Response: \n{msg}', simpleprint=True)
            return msg

        if iCmdLen == 4:
            strCurrType = lst_strMsg[3].lower()
            lst_depositTypes = getDepositTypes()
            loginfo(funcname, f'strCurrType: {strCurrType}', simpleprint=True, tprint=False)
            
            if strCurrType in lst_depositTypes:
                lst_depositCryptos = getDepositCryptosList()
                lst_depositUsd = getDepositUsdList()

                if strCurrType in lst_depositCryptos:
                    usage = getUsageRespMsg(member, strCurrType)
                    msg = getDepositCryptoRespMsg(member, strCurrType, usdAmnt, usage)
                    loginfo(funcname, f'CMD Msg Response: \n{msg}', simpleprint=True)
                    return msg
                elif strCurrType in lst_depositUsd:
                    usage = getUsageRespMsg(member, strCurrType)
                    msg = getDepositUsdRespMsg(member, strCurrType, usdAmnt, usage)
                    loginfo(funcname, f'CMD Msg Response: \n{msg}', simpleprint=True)
                    return msg
                else:
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


