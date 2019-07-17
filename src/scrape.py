#--------------------------------------------------------------------------------------------#
#ref: https://github.com/julia-git/webscraping_ny_mta/blob/master/Webscraping.ipynb
#ref: https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
#--------------------------------------------------------------------------------------------#

print('\n\nSTART _ scrape.py \n\n')

# Webscrape Example
import requests
import urllib.request
import time
from bs4 import BeautifulSoup # python3.7 -m pip install bs4

import sites #required: sites/__init__.py
from utilities import *

# Set the URL params to webscrape from sites/__init__.py
rootUrl = sites.rootUrl
setting_orderBy = sites.setting_orderBy
url = sites.url + '/'
uriOrderByLeechersMost = sites.uriOrderByLeechersMost
iSiteTypeId = sites.iSiteTypeId

## designates the html order that the torrent side is displaying SE & LE
flag_SE_LE_to_print = 1 # SE first = 1; LE first = 0

iLastPageNum = 30
torrentCnt = 0
lst_info_hash = []
lst_info_hash_print = []
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
                    lst_info_hash.append(tup_info_hash)
                    lst_info_hash_print.append(tup_info_hash_print)
                
                # add tuple to list of all hashes scraped
                lst_info_hash_all.append(tup_info_hash)
                lst_info_hash_all_print.append(tup_info_hash_print)
        else:
            print('class not found')

def getPrintListStr(lst=[], strListTitle='list', useEnumerate=True, goIdxPrint=False, goStrTupPrint=False, goPrint=True):
    strGoIndexPrint = None
    if goIdxPrint:
        strGoIndexPrint = '(w/ indexes)'
    else:
        strGoIndexPrint = '(w/o indexes)'

    lst_str = None
    if useEnumerate:
        if goIdxPrint:
            if goStrTupPrint:
                lst_str = [f"{i}: {', '.join(map(str,v))}" for i,v in enumerate(lst)]
            else:
                lst_str = [f'{i}: {v}' for i,v in enumerate(lst)]
        else:
            if goStrTupPrint:
                lst_str = [f"{', '.join(map(str,v))}" for i,v in enumerate(lst)]
            else:
                lst_str = [f'{v}' for i,v in enumerate(lst)]
    else:
        if goIdxPrint:
            if goStrTupPrint:
                lst_str = [f"{lst.index(x)}: {', '.join(map(str,x))}" for x in lst]
            else:
                lst_str = [f'{lst.index(x)}: {x}' for x in lst]
        else:
            if goStrTupPrint:
                lst_str = [f"{', '.join(map(str,x))}" for x in lst]
            else:
                lst_str = [f'{x}' for x in lst]

    lst_len = len(lst)
    print(f'\nPrinting List... {strListTitle} _ {strGoIndexPrint} _ found {lst_len}:', *lst_str, sep = "\n ")
    return lst_str


# Connect to the URL & parse HTML to BeautifulSoup object
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")

for x in range(0, iLastPageNum+1):
    pageUrl = getUrlPageNum(x)

    # Connect to the URL & parse HTML to BeautifulSoup object
    print(f'ATTEMPTING request -> GET on URL: {pageUrl}')
    response = requests.get(pageUrl)
    print(f'RECEIVED response -> GET on URL: {pageUrl}')
    print(f'... proceeding to parse response.text with BeautifulSoup\n\n')
    soup = BeautifulSoup(response.text, "html.parser")

    # print response (note: '<Response [200]>' means it went through)
    print(f'RESPONSE from requests.get({pageUrl}):\n {response}\n {setting_orderBy}')
    print()

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

    # print current info_hash list accumulated
    lst_info_hash_str = getPrintListStr(lst_info_hash_print, strListTitle='current info_hash found; where SEED < LEECH', useEnumerate=True, goIdxPrint=True, goStrTupPrint=True)
    print(f'\n Page #{x} of {iLastPageNum} _ DONE... sleep(1)\n\n')
    time.sleep(1)

getPrintListStr(lst_info_hash_print, strListTitle='ALL info_hash found; where seed < leech', useEnumerate=True, goIdxPrint=True)
#printListStr(lst_info_hash_all_print, strListTitle='ALL info_hash found; TOTAL', useEnumerate=True, goIdxPrint=True)

tup_scrape_inst = (iSiteTypeId, rootUrl, iLastPageNum, 0)
procCallAdminCreateScrapeInstance(tup_scrape_inst, lst_info_hash)

print('\n\nEND _ ALL seed | leech counts found... exit(0) \n\n')
exit(0)


