#--------------------------------------------------------------------------------------------#
#ref: https://github.com/julia-git/webscraping_ny_mta/blob/master/Webscraping.ipynb
#ref: https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
#--------------------------------------------------------------------------------------------#
print('GO scrape.py -> starting IMPORTs')

# Webscrape Example
import requests
import urllib.request
import time
from bs4 import BeautifulSoup # python3.7 -m pip install bs4
from utilities import * #imports 'from sites import *'

filename = 'scrape.py'
logenter(filename, "\n IMPORTs complete:- STARTING -> file '%s' . . . " % filename, simpleprint=False, tprint=True)

# Set the URL params to webscrape from sites/__init__.py
rootUrl = sites.rootUrl
setting_orderBy = sites.setting_orderBy
#url = sites.url + '/'
uriOrderByLeechersMost = sites.uriOrderByLeechersMost
iSiteTypeId = sites.iSiteTypeId
strSiteSubTypeUri = sites.strSiteSubTypeUri
url = sites.url + strSiteSubTypeUri + '/'

## designates the html order that the torrent side is displaying SE & LE
flag_SE_LE_to_print = 1 # SE first = 1; LE first = 0

iLastPageNum = 35
iCntInfoHashSampleSize = 11
torrentCnt = 0
lst_info_hash = []
lst_info_hash_print = []
lst_info_hash_print_sample = []
lst_info_hash_str = ''

lst_info_hash_all = []
lst_info_hash_all_print = []

def getUrlPageNum(pageNum):
    return url + str(pageNum) + uriOrderByLeechersMost

def getInfoHashFromMagnetLink(mag_link):
    info_hash = 'ERROR -> no info hash found'
    if mag_link is None:
        return info_hash
    mag_link = str(mag_link)
    idxStart = mag_link.find("btih:")+5
    idxEnd = mag_link.find("&dn=")
    return mag_link[idxStart:idxEnd]

def getMagnetLink(parent):
    font_string = 'ERROR -> no file size found'
    all_tags = parent.findAll('a')
    for tag in all_tags:
        if tag['href'] and tag['href'].find('magnet:') == 0:
            return tag['href']
    return 'ERROR -> no magnet link found'

def getFileSizeStr(parent):
    file_size = parent.find('font').contents[0]
    idxStart = file_size.find('Size')+5
    idxEnd = file_size.rfind(', ')
    return file_size[idxStart:idxEnd]

def getSeedLeechCntStr(parent):
    global flag_SE_LE_to_print
    strSeed = 'ERROR -> seed count'
    strLeech = 'ERROR -> leech count'
    iSeed = -1
    iLeech = -1
    all_td_tags = parent.findAll(align='right')
    
    # get just numeric values of seed & leech count
    #   (retrieves correct order based on 'flag_SE_LE_to_print' set above)
    for td_tag in all_td_tags:
        strTag = td_tag.string
        if flag_SE_LE_to_print:
            strSeed = f'  Seed Cnt: {strTag}'
            iSeed = int(strTag)
            flag_SE_LE_to_print = 0
        else:
            strLeech = f'  Leech Cnt: {strTag}'
            iLeech = int(strTag)
            flag_SE_LE_to_print = 1
    return strSeed + '\n' + strLeech, iSeed, iLeech

def setSeedLeechCntDisplayOrder(all_abbr_tags):
    # traverse through site header (using <abbr> html tags)
    #   to determine if seed or leech count is displayed first
    for tags in all_abbr_tags:
        if str(tags).find('Seed'):
            print(' ...SEED found first \n')
            flag_SE_LE_print_order = 1
            break
        if str(tags).find('Leech'):
            print(' ...LEECH found first \n')
            flag_SE_LE_print_order = 0
            break

def getSplicedTitleFromHrefTag(href_tag):
    idxSlash1 = href_tag.find('/')
    idxSlash2 = href_tag.find('/', idxSlash1+1)
    idxSlash3 = href_tag.find('/', idxSlash2+1)
    spliced_href_tag = href_tag[idxSlash3+1:]
    return spliced_href_tag

def checkAppendToInfoHashSampleLst(tup_info_hash):
    if isinstance(tup_info_hash, tuple) and isinstance(lst_info_hash, list):
        if len(lst_info_hash) <= iCntInfoHashSampleSize:
            lst_info_hash_print_sample.append(tup_info_hash)

def getPrintTorrentDataSets(all_a_tags, iPgNum=-1):
    global torrentCnt
    # traverse through all html tags <a>, looking for torrent rows containing seed & leech counts
    for i,tag in enumerate(all_a_tags):

        # FIND 'href' tags -> 'href' tags dictate potential data rows with possible '/torrent'
        if tag['href']:
            href_tag = tag['href']

            # FIND '/torrent/' URIs -> '/torrent' URIs dictate data rows with seed & leech counts
            if href_tag.find('/torrent/') == 0:
                torrentCnt += 1
                print(f" [{torrentCnt}] href# {i}: '{rootUrl+href_tag}'")

                ## since we now found a correct data row with seed & leech counts
                # GET magnet link from '<a href>' that is 2 parent levels up
                mag_link = getMagnetLink(tag.parent.parent)

                ## info_hash is extractable from magnet link
                # GET info hash from mag_link
                info_hash = getInfoHashFromMagnetLink(mag_link)

                ## since we now found a correct data row with seed & leech counts
                # GET file size from <font> tag that is 2 parent levels up
                file_size = getFileSizeStr(tag.parent.parent)

                ## since we now found a correct data row with seed & leech counts
                # GET seed & leech counts from 2 <td> tags that are 3 parent levels up
                seed_leech, iSeed, iLeech = getSeedLeechCntStr(tag.parent.parent.parent)

                ## create info_hash tuple for print
                spl_href_tag = getSplicedTitleFromHrefTag(href_tag)
                strPgNum = 'PG# ' + str(iPgNum)
                tup_info_hash_print = (strPgNum, info_hash, iSeed, iLeech, file_size, spl_href_tag)
                tup_info_hash_print_sample = (info_hash, spl_href_tag)
                
                ## create info_hash tuple for database
                tup_info_hash = (strPgNum, info_hash, iSeed, iLeech, file_size, spl_href_tag, href_tag, mag_link, 0)
                #tup_info_hash = (strPgNum, info_hash, iSeed, iLeech, file_size, spl_href_tag, '<href_tag>', '<mag_link>', 0)

                if iSeed < iLeech:
                    print(f'{seed_leech}')
                    print(f'  Torrent File Size: {file_size}')
                    print(f'  Info_Hash: {info_hash}')
                    print(f'  Magnet Link: {mag_link}')
                    print()

                    # add tuple to list of hashes in demand
                    #checkAppendToInfoHashSampleLst(tup_info_hash_print_sample)
                    if len(lst_info_hash) <= iCntInfoHashSampleSize: lst_info_hash_print_sample.append(tup_info_hash_print_sample)
                    lst_info_hash.append(tup_info_hash)
                    lst_info_hash_print.append(tup_info_hash_print)
                
                # add tuple to list of all hashes scraped
                lst_info_hash_all.append(tup_info_hash)
                lst_info_hash_all_print.append(tup_info_hash_print)
        else:
            print('class not found')

def printCurrentScrapeMetrics(currPgNum=-1, lastPgNum=-1, end=False):
    strCurrTotal = 'TOTAL' if end else 'CURRENT'

    strEnd = f'TOTAL Pages SCARPED _ {lastPgNum} of {lastPgNum}'
    strStatus = f'PAGE #{x} of {iLastPageNum} _ SCRAPED'
    strLstCnt = f'{strCurrTotal} seed | leech counts found: {len(lst_info_hash)}'
    strRequestCnt = f'{strCurrTotal} Request Count: {cntRequest}'
    strResp200Cnt = f'{strCurrTotal} Response 200 Count: {cntResp200}'
    strResp502Cnt = f'{strCurrTotal} Response 502 Count: {cntResp502}'
    strExceptCnt = f'{strCurrTotal} Exception Count: {cntExceptionsHit}'

    if end:
        print(f'\n\nEND _', f'{strEnd}', f'{strLstCnt}', f'{strRequestCnt}', f'{strResp200Cnt}', f'{strResp502Cnt}', f'{strExceptCnt}', sep='\n')
    else:
        print(f'\n\nSTATUS _ {strStatus}', f'{strLstCnt}', f'{strRequestCnt}', f'{strResp200Cnt}', f'{strResp502Cnt}', f'{strExceptCnt}', sep='\n')

# Connect to the URL & parse HTML to BeautifulSoup object
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")

cntExceptionsHit = 0
cntRequest = 0
cntResp200 = 0
cntResp502 = 0
for x in range(0, iLastPageNum+1):
    pageUrl = getUrlPageNum(x)

    response = None
    bExcept = False
    try:
        # Connect to the URL & parse HTML to BeautifulSoup object
        cntRequest += 1
        print(f'\n\nATTEMPTING request #{cntRequest} -> GET on URL: {pageUrl}')
        response = requests.get(pageUrl)
        if response.status_code == 200:
            cntResp200 += 1
        if response.status_code == 502:
            cntResp502 += 1
    except ValueError as e:
        strE_0 = f"Exception hit... \nFAILED 'GET' request: requests.get({pageUrl});"
        strE_1 = f"\n __Exception__: \n{e}\n __Exception__"
        logerror(filename, strE_0, strE_1, simpleprint=False)
        logalert(filename, "Exception hit with 'GET' request; continuing to next iteration", simpleprint=False, tprint=True)
        bExcept = True
        continue
    except Exception as e:
        #print type(e)       # the exception instance
        #print e.args        # arguments stored in .args
        #print e             # __str__ allows args to be printed directly
        strE_0 = f"Exception hit... \nFAILED 'GET' request: requests.get({pageUrl}); \nException is NOT 'ValueError';"
        strE_1 = f"\n __Exception__ e: \n{e}\n __Exception__"
        strE_2 = f"\n __Exception__ type(e): \n{type(e)}\n __Exception__"
        strE_3 = f"\n __Exception__ e.args: \n{e.args}\n __Exception__"
        logerror(filename, f"{strE_0}", f" {strE_1}\n {strE_2}\n {strE_2}\n", simpleprint=False, tprint=True)
        logalert(filename, "Exception hit with 'GET' request; continuing to next iteration", simpleprint=False, tprint=True)
        bExcept = True
        continue
    finally:
        if bExcept: cntExceptionsHit += 1
        print(f' ... exception hit: {bExcept} -> ATTEMPTING request -> GET on URL: {pageUrl}\n')

    print(f'RECEIVED response -> GET on URL: {pageUrl}')
    print(f'... proceeding to parse response.text with BeautifulSoup\n\n')
    soup = BeautifulSoup(response.text, "html.parser")

    # print response (note: '<Response [200]>' means it went through)
    print(f'RESPONSE from requests.get({pageUrl}):\n {response}\n {setting_orderBy}\n')

    # print full 'soup' parsed html text
    #print('printing full soup parsed html text:', soup)
    #print()

    print('CHECKING torrent site (for seed|leech display order)...')
    # get all 'abbr' tags
    all_abbr_tags = soup.findAll('abbr')
    setSeedLeechCntDisplayOrder(all_abbr_tags)

    print('PRINTING all_abbr_tags...', *all_abbr_tags, sep='\n ')
    print()

    print('SEARCH & PRINTING torrent rows & seed | leech counts...')
    # get all 'a' tags
    all_a_tags = soup.findAll('a')
    getPrintTorrentDataSets(all_a_tags, iPgNum=x)

    print('\n\n', cStrDivider2, sep='')
    # print current info_hash list accumulated
    lst_info_hash_str = getPrintListStrTuple(lst_info_hash_print, strListTitle='CURRENT info_hash found; where SEED < LEECH', useEnumerate=True, goIdxPrint=True)

    # print current status
    printCurrentScrapeMetrics(currPgNum=x, lastPgNum=iLastPageNum, end=False)
    print(cStrDivider2, 'sleep(1)', sep='\n\n', end='\n\n')
    time.sleep(1)

print('\n\n', cStrDivider2, sep='')
# print ALL 'in demand' info hashes found
getPrintListStr(lst_info_hash_print, strListTitle='ALL info_hash found; where SEED < LEECH', useEnumerate=True, goIdxPrint=True)

print('\n\n', cStrDivider2, sep='')
# perform db call to store scraped data
tup_scrape_inst = (iSiteTypeId, strSiteSubTypeUri, rootUrl, iLastPageNum, 0)
procCallAdminCreateScrapeInstance(tup_scrape_inst, lst_info_hash)

print('\n\n', cStrDivider2, sep='')
# print Minimal sample data info hashes found
getPrintListStrTuple(lst_info_hash_print_sample, strListTitle='SAMPLE DATA info_hash in HIGH DEMAND; where SEED < LEECH', useEnumerate=True, goIdxPrint=False)

# print ALL TOTAL info hashes scraped
#getPrintListStr(lst_info_hash_all_print, strListTitle='ALL info_hash found; TOTAL', useEnumerate=True, goIdxPrint=True)


# print end status
print('\n\n', cStrDivider2, sep='')
printCurrentScrapeMetrics(currPgNum=iLastPageNum, lastPgNum=iLastPageNum, end=True)
print(cStrDivider2, 'exit(0)', sep='\n\n', end='\n\n')
exit(0)



