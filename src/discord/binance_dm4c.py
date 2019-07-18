print('GO binance_dm4c.py -> starting IMPORTs')
from constants import *

'''
# https://github.com/sammchardy/python-binance
    $ pip install python-binance
    #NOTE: '$ pip3' == '$ python3.6 -m pip'
        $ python3 -m pip install python-binance
        $ python3.7 -m pip install python-binance

'''
from binance.client import Client

filename = 'binance_dm4c.py'
logenter(filename, "\n IMPORTs complete:- STARTING -> file '%s' . . . " % filename, simpleprint=False, tprint=True)

api_key = sites.api_key
api_secret = sites.api_secret
client = Client(api_key, api_secret) # performs binance REST api handshakes

def getSymbPrice(symbFull='BTCUSDT'):
    funcname = f'({filename}) getSymbPrice'
    logenter(funcname, f'symbFull: {symbFull}', simpleprint=False, tprint=False)
    
    tick = client.get_symbol_ticker(symbol=symbFull)
    price = tick['price']
    return str(price).rstrip('0')

def convertUSD_toAltSymbAmnt(usdAmnt=0.0, altSymbFull=cSymbFullBTC):
    funcname = f'({filename}) convertUSD_toAltSymbAmnt'
    logenter(funcname, f'usdAmnt: {usdAmnt}; altSymbFull: {altSymbFull};', simpleprint=False, tprint=False)

    if usdAmnt <= 0.0 or altSymbFull not in cSymb_lst_binance:
        logerror(funcname, f'invalid input... \nusdAmnt: {usdAmnt}; altSymbFull: {altSymbFull}; \nreturning 0.0')
        return 0.0
    
    # if ETH (return direct conversion to USDT)
    if altSymbFull == cSymbFullETH:
        currPriceETHUSD = getSymbPrice(symbFull=cSymbFullETH)
        ethAmnt = float(usdAmnt) / float(currPriceETHUSD)
        currPriceALTUSD = usdAmnt / ethAmnt
        loginfo(funcname, f' >>> current ETH price: ${currPriceETHUSD}', simpleprint=True)
        loginfo(filename, f' >>> ${usdAmnt} = {ethAmnt} {altSymbFull}', simpleprint=True)
        loginfo(funcname, f' >>> current {altSymbFull} Price: ${currPriceALTUSD}', simpleprint=True)
        return ethAmnt

    # if BTC (return direct conversion to USDT)
    if altSymbFull == cSymbFullBTC:
        currPriceBTCUSD = getSymbPrice(symbFull=cSymbFullBTC)
        btcAmnt = float(usdAmnt) / float(currPriceBTCUSD)
        currPriceALTUSD = usdAmnt / btcAmnt
        loginfo(funcname, f' >>> current BTC Price: ${currPriceBTCUSD}', simpleprint=True)
        loginfo(funcname, f' >>> ${usdAmnt} = {btcAmnt} {altSymbFull}', simpleprint=True)
        loginfo(funcname, f' >>> current {altSymbFull} Price: ${currPriceALTUSD}', simpleprint=True)
        return btcAmnt

    # if other alt (return with conversion through BTC first)
    currPriceBTCUSD = getSymbPrice(symbFull=cSymbFullBTC)
    btcAmnt = float(usdAmnt) / float(currPriceBTCUSD)
    altSymbAmnt = convertBTC_toAltSymbAmnt(btcAmnt=btcAmnt, altSymbFull=altSymbFull)
    currPriceALTUSD = usdAmnt / altSymbAmnt
    loginfo(funcname, f' >>> current BTC Price: ${currPriceBTCUSD}', simpleprint=True)
    loginfo(funcname, f' >>> ${usdAmnt} = {altSymbAmnt} {altSymbFull}', simpleprint=True)
    loginfo(funcname, f' >>> current {altSymbFull} Price: ${currPriceALTUSD}', simpleprint=True)
    return altSymbAmnt

def convertBTC_toAltSymbAmnt(btcAmnt=0.0, altSymbFull=cSymbFullBTC):
    funcname = f'({filename}) convertBTC_toAltSymbAmnt'
    logenter(funcname, f'btcAmnt: {btcAmnt}; altSymbFull: {altSymbFull};', simpleprint=False, tprint=False)
    
    if btcAmnt <= 0.0 or altSymbFull not in cSymb_lst_binance:
        logerror(funcname, f'invalid input... \nbtcAmnt: {btcAmnt}; altSymbFull: {altSymbFull}; \nreturning 0.0')
        return 0.0
    
    currPriceInBTC = getSymbPrice(symbFull=altSymbFull)
    altSymbAmnt = float(btcAmnt) / float(currPriceInBTC)
    loginfo(funcname, f" >>> current {altSymbFull} Price: {currPriceInBTC} BTC", simpleprint=True)
    loginfo(funcname, f" >>> {btcAmnt} {cSymbFullBTC} = {altSymbAmnt} {altSymbFull}", simpleprint=True)
    return altSymbAmnt

#def convertAltSymb_toBTC(altSymbAmnt=0.0, altSymbFull=cSymbFullBTC):
#    funcname = f'({filename}) convertAltSymb_toBTC'
#    logenter(funcname, f'altSymbAmnt: {altSymbAmnt}; altSymbFull: {altSymbFull};', simpleprint=False, tprint=True)
#
#    if altSymbAmnt <= 0.0 or altSymbFull not in cSymb_lst_binance:
#        return 0.0
#
#    currPriceInBTC = getSymbPrice(symbFull=altSymbFull)
#    altSymbValueInBTC = altSymbAmnt * currPriceInBTC
#    return altSymbValueInBTC



#====================================================#
#====================================================#


loginfo(filename, "\n CLASSES & FUNCTIONS initialized:- STARTING -> additional '%s' run scripts (if applicable) . . . \n\n" % filename, simpleprint=True)


#print('\n')
#print('#======================================================================#')
#loginfo(filename, "\n  DONE Executing additional '%s' run scripts ... \n" % filename, simpleprint=True)


