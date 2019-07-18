from xlogger import *

filename = 'test.py'
logenter(filename, "\n IMPORTs complete:- STARTING -> file '%s' . . . " % filename, simpleprint=False, tprint=True)
def validStrFormatUSD(strUSD):
    funcname = '(%s) validStrFormatUSD' % filename
    logenter(funcname, f'(strUSD={strUSD}', simpleprint=False, tprint=True)
    
    if not strUSD.startswith('$'):
        logerror(funcname, f"'{strUSD}' does not start with '$'; returning False")
        return False
    
    strValue = strUSD[1:]
    try:
        #v = int(strUSD)
        value = float(strValue)
        loginfo(funcname, f'strUSD: {strUSD}; \n strValue: {strValue}; \n value: {value}; \n returning True', simpleprint=True)
        return True
    except ValueError as e:
        strE_0 = f"Exception hit... \nFAILED cast to float: float({strUSD}); \nreturning False"
        strE_1 = f"\n __Exception__: \n{e}\n __Exception__"
        logerror(funcname, strE_0, strE_1, simpleprint=False)
        return False


loginfo(filename, "\n CLASSES & FUNCTIONS initialized:- STARTING -> additional '%s' run scripts (if applicable) . . . \n\n" % filename, simpleprint=True)


#validStrFormatUSD('$50')
#validStrFormatUSD('50.0')

strMsgContent = '!deposit $50.11$'
lstMsgContent = strMsgContent.split(' ')
lst_strMsg = lstMsgContent
strUSD = lst_strMsg[1]
#validStrFormatUSD(strUSD)

strMsgContent = '!deposit $50.0'
strMsgContent = '!deposit $10.0 with BTC'
#strMsgContent = '!deposit $50.0 with ETH'
#strMsgContent = '!deposit $50.0 with TRX'
#strMsgContent = '!deposit $50.0 with venmo'
#strMsgContent = '!deposit $50.0 with patreon'
lstMsgContent = strMsgContent.split(' ')
lst_strMsg = lstMsgContent
#from cmd_deposit import *
#CMD_deposit('<test-mem#1492>', lst_strMsg)

from binance_dm4c import *
usdAmnt = 865
#symbFull = 'ETHUSDT'
symbFull = 'BTCUSDT'
#symbFull = 'TRXBTC'
#symbFull = 'BTTBTC'
#convertedvalue = convertUSD_toAltSymbAmnt(usdAmnt=9272.79, altSymbFull='BTCUSDT')
depositAmnt = convertUSD_toAltSymbAmnt(usdAmnt=usdAmnt, altSymbFull=symbFull)
#loginfo(filename, f'deposit amount {depositAmnt} {symbFull}, for ${usdAmnt}', simpleprint=True)

print('\n')
print('#======================================================================#')
loginfo(filename, "\n  DONE Executing additional '%s' run scripts ... \n" % filename, simpleprint=True)
