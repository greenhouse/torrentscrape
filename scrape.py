#--------------------------------------------------------------------------------------------#
#ref: https://github.com/julia-git/webscraping_ny_mta/blob/master/Webscraping.ipynb
#ref: https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
#--------------------------------------------------------------------------------------------#

print('START scrape.py')

# Webscrape Example
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#import re

# pirate bay root url
rootUrl = 'https://www.thepiratebay.org'
browseMovieUri = '/browse/201' #note: same as w/ 'browseMovieUriP0' appended
uriPage0OrderByDefault = '/0/3' #note: default same as just 'browseMovieUri'

uriPage0 = '/0' #note: default same as just 'browseMovieUri'
uriPage1 = '/1'
uriPage2 = '/2'
uriPage3 = '/3'
uriPage4 = '/4'

uriOrderByUpdate = '/3' #note: default same as just 'browseMovieUri'
uriOrderByName = '/1'
uriOrderBySize = '/5'
uriOrderBySeedersMost = '/7'
uriOrderBySeedersLeast = '/8'
uriOrderByLeechersMost = '/9'
uriOrderByLeechersLeast = '/10' # BUG_07.11.19 pirate bay broken (always orders by 'most')

## designates the html order that 'pirate bay' displaying SE & LE
# SE first = 1; LE first = 0
flag_SE_LE_to_print = 1

# Set the URL you want to webscrape from
url = rootUrl + browseMovieUri + uriPage0 + uriOrderByLeechersMost

# Connect to the URL
response = requests.get(url)
# print response (note: response #200 means it went through)
print(f'response from requests.get({url}):\n {response}', 'uriOrderByLeechersMost')
print()
'''
<Response [200]>
'''

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")
'''
#prints full 'soup' parsed html text (note: example displayed below)
#print('printing full soup parsed html text:', soup)
#print()
'''

def getFileSizeStr(parent):
    all_tags = parent.find('font')
    print(*all_tags, sep='\n ')
    cont = all_tags.contents
    print(*cont, sep='\n ')
    return cont[0]
#    return all_tags.string
#    for i,tag in enumerate(all_tags):
#        print(f'{i} {tag}')
###        if tag.string:
##        return tag.string
##
    return 'ERROR -> no file size found'

#def getMagnetLink(all_tags):
#    href_link = 'ERROR -> no magnet link found'
#    font_string = 'ERROR -> no file size found'
##    sib = tag.next_sibling
##    while sib is not None:
#    for i,tag in enumerate(all_tags):
##        print(f"sib: {sib}")
#        print(f"tag: {tag}")
#        if isinstance(tag, str):
##            sib = sib.next_sibling
#            continue
#
##        if tag['href']:
#        if 'href' in tag:
#            href_tag = tag['href']
#            if href_tag.find('magnet:') == 0:
#                href_link = href_tag
#
##        if tag['font']:
#        if 'font' in tag:
#            font_tag = tag['font']
#            font_string = font_tag.string
#
##        sib = sib.next_sibling
#
#    return href_link, font_string

def getMagnetLink(parent):
    font_string = 'ERROR -> no file size found'
    all_tags = parent.findAll('a')
    for tag in all_tags:
        if tag['href'] and tag['href'].find('magnet:') == 0:
            return tag['href']

    return 'ERROR -> no magnet link found'

print('checking Pirate Bay (for seed or leech displayed first)...')
# get all 'abbr' tags
all_abbr_tags = soup.findAll('abbr')

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


print('printing all_abbr_tags...', *all_abbr_tags, sep='\n ')
print()

print('searching & printing torrent rows & seed | leech counts...')
# get all 'a' tags
all_a_tags = soup.findAll('a')

# traverse through all html tags <a>, looking for torrent rows containing seed & leech counts
torrentCnt = 0
for i,tag in enumerate(all_a_tags):

    # FIND 'href' tags -> 'href' tags dictate potential data rows with possible '/torrent'
    if tag['href']:
        href_tag = tag['href']
        
        # FIND '/torrent/' URIs -> '/torrent' URIs dictate data rows with seed & leech counts
        if href_tag.find('/torrent/') == 0:
            torrentCnt += 1
            print(f" [{torrentCnt}] {i}: href='{href_tag}'")

            # GET tag that is 2 parent levels up (since we now found a correct data row with seed & leech counts
            td_parent = tag.parent.parent.parent

            # GET magnet link
            mag_sib_start = tag.parent.next_sibling
#            mag_link = getMagnetLink(mag_sib_start)
#            mag_link, file_size = getMagnetLink(tag.parent.parent)
            mag_link = getMagnetLink(tag.parent.parent)
            
            
            # GET file size from t
            file_size = tag.parent.parent.find('font').contents[0]
            idxStart = file_size.find('Size')
            idxEnd = file_size.rfind(', ')
            file_size = file_size[idxStart:idxEnd]

            # FIND the 2 'td' tags with seed & leech counts
            all_td_tags = td_parent.findAll(align='right')

            # print both full 'td' tags with seed & leech counts
            #print(*all_td_tags, sep=' \n')
            
            # print just numeric values of seed & leech count
            #   (prints correct order based on 'flag_SE_LE_to_print' set above)
            for td_tag in all_td_tags:
                strTag = td_tag.string
                if flag_SE_LE_to_print:
                    print(f'  Seed Cnt: {strTag}')
                    flag_SE_LE_to_print = 0
                else:
                    print(f'  Leech Cnt: {strTag}')
                    flag_SE_LE_to_print = 1
            print(f'  Torrent File Size: {file_size}')
            print(f'  Magnet Link: {mag_link}')
            print()
    else:
        print('class not found')


print(' ALL seed | leech counts found... exit(0)')
exit(0)



