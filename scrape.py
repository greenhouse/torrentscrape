#--------------------------------------------------------------------------------------------#
#ref: https://github.com/julia-git/webscraping_ny_mta/blob/master/Webscraping.ipynb
#ref: https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
#--------------------------------------------------------------------------------------------#

print('\n\nSTART _ scrape.py \n\n')

# Webscrape Example
import requests
import urllib.request
import time
import sites
from bs4 import BeautifulSoup # python3.7 -m pip install bs4

# Set the URL params to webscrape from
rootUrl = sites.rootUrl
setting_orderBy = sites.setting_orderBy
url = sites.url

## designates the html order that the torrent side is displaying SE & LE
flag_SE_LE_to_print = 1 # SE first = 1; LE first = 0

# Connect to the URL & parse HTML to BeautifulSoup object
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


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
    strSeech = 'ERROR -> seed count'
    strLeech = 'ERROR -> leech count'
    all_td_tags = parent.findAll(align='right')
    
    # get just numeric values of seed & leech count
    #   (retrieves correct order based on 'flag_SE_LE_to_print' set above)
    for td_tag in all_td_tags:
        strTag = td_tag.string
        if flag_SE_LE_to_print:
            strSeech = f'  Seed Cnt: {strTag}'
            flag_SE_LE_to_print = 0
        else:
            strLeech = f'  Leech Cnt: {strTag}'
            flag_SE_LE_to_print = 1
    return strSeech + '\n' + strLeech

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

def getPrintTorrentDataSets(all_a_tags):
    # traverse through all html tags <a>, looking for torrent rows containing seed & leech counts
    torrentCnt = 0
    for i,tag in enumerate(all_a_tags):

        # FIND 'href' tags -> 'href' tags dictate potential data rows with possible '/torrent'
        if tag['href']:
            href_tag = tag['href']

            # FIND '/torrent/' URIs -> '/torrent' URIs dictate data rows with seed & leech counts
            if href_tag.find('/torrent/') == 0:
                torrentCnt += 1
                print(f" [{torrentCnt}] href#{i}: '{rootUrl+href_tag}'")

                ## since we now found a correct data row with seed & leech counts
                # GET magnet link from '<a href>' that is 2 parent levels up
                mag_link = getMagnetLink(tag.parent.parent)

                ## since we now found a correct data row with seed & leech counts
                # GET file size from <font> tag that is 2 parent levels up
                file_size = getFileSizeStr(tag.parent.parent)

                ## since we now found a correct data row with seed & leech counts
                # GET seed & leech counts from 2 <td> tags that are 3 parent levels up
                seed_leech = getSeedLeechCntStr(tag.parent.parent.parent)

                print(f'{seed_leech}')
                print(f'  Torrent File Size: {file_size}')
                print(f'  Magnet Link: {mag_link}')
                print()
        else:
            print('class not found')

# print response (note: '<Response [200]>' means it went through)
print(f'RESPONSE from requests.get({url}):\n {response}\n {setting_orderBy}')
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
getPrintTorrentDataSets(all_a_tags)

print('\n\nEND _ ALL seed | leech counts found... exit(0) \n\n')
exit(0)



