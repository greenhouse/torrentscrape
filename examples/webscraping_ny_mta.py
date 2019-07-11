#--------------------------------------------------------------------------------------------#
#ref: https://github.com/julia-git/webscraping_ny_mta/blob/master/Webscraping.ipynb
#ref: https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
#--------------------------------------------------------------------------------------------#

# Webscrape Example
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'http://web.mta.info/developers/turnstile.html'

# Connect to the URL
response = requests.get(url)

# print response
print(f'response:\n {response}\n') # response #200 means it went through
'''
<Response [200]>
'''

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")
'''
print(f'soup:\n {soup}') # note: example displayed below
'''

# To locate all 'a' tags
all_a_tags = soup.findAll('a')
#print(f'all_a_tags:\n {all_a_tags}\n')

#strPring = 'printing all_a_tags:\n %s' % *all_a_tags
#print(strPring)
cnt = 0
strSep = "\n %i" % cnt
#print('printing all_a_tags:\n ', *all_a_tags, sep = f"\n %i" % cnt++)
#print('printing all_a_tags:\n ', *all_a_tags, sep = strSep)
#print('printing all_a_tags:\n ', *all_a_tags, sep = '\n '+ str(*all_a_tags.index))
#print('printing all_a_tags:\n ', *all_a_tags, sep = '\n ' + str(cnt++))

#print()

cnt = 0
print('\n'.join(map(str, all_a_tags)))
#print('\n'.join(map(str, all_a_tags)))


#print('printing all_a_tags:\n ')
#print(*all_a_tags, sep = "\n ")
#print()


#print(*a, sep = "\n")


# Let's take a quick look at the very first data file, which starts on line 36
one_a_tag = soup.findAll('a')[36]
print(f'one_a_tag:\n {one_a_tag}\n')

# We want to extract the actual link
link = one_a_tag['href']

# print link
print(f'one_a_tag link:\n {link}\n')
'''
'data/nyct/turnstile/turnstile_180922.txt'
'''


## The full download URL is 'http://web.mta.info/developers/' + link
# To download the whole data set, let's do a for loop through all a tags
for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links
    
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    download_url = 'http://web.mta.info/developers/'+ link
    print()
    print(f'downloading url: {download_url}')
    print(f" w/ found 'a' tag: {one_a_tag}")
    print(f" w/ found 'href' link: {link}")
    urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
    print(' download DONE... sleep(1)')
    time.sleep(1)


#--------------------------------------------------------------------------------#
## example HTML print from 'BeautifulSoup(response.text, "html.parser")' call
#--------------------------------------------------------------------------------#
#soup = BeautifulSoup(response.text, "html.parser")
#print(f'soup:\n {soup}')

'''
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
    "http://www.w3.org/TR/html4/strict.dtd">
    
    <html lang="en">
    <head>
    <title>mta.info | Turnstile Data</title>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
    <meta content="width=device-width, initial-scale=1" name="viewport"/>
    <!--<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7">-->
    <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
    <link href="/siteimages/favicon.ico" rel="shortcut icon"/>
    <link href="/css/base.css" rel="stylesheet" type="text/css"/>
    <link href="/css/grid.css" rel="stylesheet" type="text/css"/>
    <link href="/css/topbar.css" rel="stylesheet" type="text/css"/>
    <link href="/css/formalize.css" rel="stylesheet" type="text/css"/>
    <!-- <link rel="stylesheet" type="text/css" href="/css/jquery.datepick.css"> -->
    <!-- jQuery include should be at the top -->
    <script language="javascript" src="/js/jquery-1.4.4.min.js" type="text/javascript"></script>
    <link href="/css/template.css" rel="stylesheet" type="text/css"/>
    <meta content="News" name="WT.cg_n">
    <style media="all" type="text/css">
    @import url(/mta/mtahq_custom_clean.css);
    @import url(/mta/news/newsroom_custom.css);
    #contentbox h2,h3 {
    padding-bottom:8px;
    padding-top:12px;
    }
    .indented {
    padding-left:15px;
    }
    </style>
    <!--[if lt IE 9]>
    <style>.roundCorners {border: 1px solid #b4b4b4;-moz-border-radius: 5px;-webkit-border-radius: 5px;border-radius: 5px;background: #fff;behavior: url(/css/border-radius.htc);}</style>
    <![endif]-->
    <!--[if IE 6]>
    <style>
    #topbar { margin: 0; padding:0;    height: 122px; width: 961px;}
    #horizontalcssmenu ul#cssmenu1 li{ position: relative; display: inline;    float: left; border: none; }
    </style>
    <![endif]-->
    <link href="/css/print.css" media="print" rel="stylesheet" type="text/css"/>
    </meta></head>
    <body>
    <div id="skip-navigation">
    <a href="#main-content">Skip to main content</a>
    </div>
    <div id="mainbox">
    <div id="topbar">
    <div id="branding">
    <a href="http://www.mta.info"><img alt="Go to MTA homepage" src="/template/images/mta_info.gif"/></a>
    </div>
    <div id="search">
    <ul id="topbar-links">
    <li class="list_h" style="margin-left:4px;"><a href="/accessibility">Accessibility</a></li>
    <li class="list_h" style="margin-left:4px;"><a href="http://assistive.usablenet.com/tt/http://www.mta.info">Text-only</a></li>
    <li class="list_h" style="margin-left:4px;"><a href="/selfserve">Customer Self-Service</a></li>
    <li class="list_h" style="margin-left:4px;"><a href="/mta/employment/">Employment</a></li>
    <li class="list_h" style="margin-left:4px;"><a href="/faqs.htm">FAQs/Contact Us</a></li>
    </ul><br/>
    <div id="search-box" style="width:230px; height:32px; float:right; margin-top:4px; margin-right:0; padding-right:0;">
    <form action="http://search.mta.info/search" id="searchform" method="get" style="margin:0; padding:0; height:32px; float:left;">
    <input name="site" type="hidden" value="my_collection"/>
    <input name="client" type="hidden" value="my_collection"/>
    <input name="proxystylesheet" type="hidden" value="my_collection"/>
    <input name="output" type="hidden" value="xml_no_dtd"/>
    <!--                <label for="searchinputbox" style="margin-left:-999px; margin-top:0; font-size:10px;">Enter search term:</label>-->
    <input alt="searchinputbox" aria-label="textbox for Search" id="searchinputbox" maxlength="255" name="q" size="20" style="margin-right:6px;float:left;" type="text" value=""/><input id="searchbutton" name="btnG" style="padding:1px 8px; float:right; margin-left:0;margin-top:-1px;" type="submit" value="search"/>
    </form>
    </div>
    </div>
    <!-- <div class="special-banner-content" style="clear: both; text-align:center; margin-top:-1em;">
    <p style="padding:0 3em 0 3em; font-size:125%; text-align:center;"><span class="blink" style="font-weight: bold; color: red;"><a href="http://nymta.civicconnect.com/LIRR-PennStation" style="color:red; ">The LIRR will resume regular weekday service on 9/5, following Amtrak&rsquo;s return to regularly scheduled operations at Penn Station. New timetables in effect 9/5. Special discounted fares through 8/31.<br />
    Temporary bus &amp; ferry service through 9/1.</a></span></p>
    </div> -->
    <div id="horizontalcssmenu" style="clear: both;">
    <ul id="cssmenu1">
    <li style="width: 75px; border-left: none;"><a href="http://www.mta.info" style="padding-left:18px;">Home</a>
    <ul>
    <li><a href="http://www.mta.info">MTA Home</a></li>
    <li><a href="http://www.mta.info/nyct">NYC Subways and Buses</a></li>
    <li><a href="http://www.mta.info/lirr">Long Island Rail Road</a></li>
    <li><a href="http://www.mta.info/mnr">Metro-North Railroad</a></li>
    <li><a href="http://www.mta.info/bandt">Bridges and Tunnels</a></li>
    <li><a href="http://web.mta.info/capital">MTA Capital Program</a></li>
    </ul>
    </li>
    <li style="width: 99px;"><a href="http://www.mta.info/schedules">Schedules</a></li>
    <li style="width: 117px;"><a href="http://web.mta.info/fares">Fares &amp; Tolls</a></li>
    <li style="width: 65px;"><a href="http://web.mta.info/maps">Maps</a></li>
    <li style="width: 199px;"><a href="http://web.mta.info/service">Planned Service Changes</a></li>
    <li style="width: 96px;"><a href="http://web.mta.info/about">MTA Info</a></li>
    <li style="width: 183px;"><a href="http://web.mta.info/business">Doing Business With Us</a></li>
    <li style="width: 119px;"><a href="http://web.mta.info/accountability/" style="padding-right:23px;">Transparency</a>
    <ul>
    <li><a href="http://web.mta.info/accountability">Main Page</a></li>
    <li><a href="http://web.mta.info/mta/boardmaterials.html">Board Materials</a></li>
    <li><a href="http://web.mta.info/mta/budget/">Budget Info</a></li>
    <li><a href="http://web.mta.info/capital">Capital Program Info</a></li>
    <li><a href="http://web.mta.info/capitaldashboard/CPDHome.html">Capital Program Dashboard</a></li>
    <li><a href="http://web.mta.info/mta/investor/">Investor Information</a></li>
    <li><a href="http://web.mta.info/mta/leadership/">MTA Leadership</a></li>
    <li><a href="http://web.mta.info/persdashboard/performance14.html">Performance Indicators</a></li>
    <li><a href="http://www.mta.info/mta-news">Press Releases and News</a></li>
    <li><a href="http://web.mta.info/mta/news/hearings">Public Hearings</a></li>
    <li><a class="last" href="http://web.mta.info/mta/news/hearings/index-reinvention.html">Transportation Reinvention Commission</a></li>
    </ul>
    </li>
    </ul>
    </div>
    </div> <!-- close topbar -->
    <div class="roundCorners clearfix" id="contentbox">
    <!-- skip navigation anchor -->
    <a name="main-content"> </a>
    <!-- Enter Content Here -->
    <h1>Turnstile Data</h1>
    <div class="container">
    <br/>
    <h2>Key/Resources</h2>
    <p>
    <ul class="arrow">
    <li style="font-weight:bold;">Field Description:
    <ul class="arrow">
    <li><a href="resources/nyct/turnstile/ts_Field_Description_pre-10-18-2014.txt">Prior to 10/18/14</a></li>
    <li><a href="resources/nyct/turnstile/ts_Field_Description.txt">Current</a></li>
    </ul>
    </li>
    <li><a href="resources/nyct/turnstile/Remote-Booth-Station.xls">Remote Unit/Control Area/Station Name Key</a></li>
    </ul>
    </p>
    <div class="span-84 last">
    <h2>Data Files</h2>
    <br/>
    <a href="data/nyct/turnstile/turnstile_180922.txt">Saturday, September 22, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180915.txt">Saturday, September 15, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180908.txt">Saturday, September 08, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180901.txt">Saturday, September 01, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180825.txt">Saturday, August 25, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180818.txt">Saturday, August 18, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180811.txt">Saturday, August 11, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180804.txt">Saturday, August 04, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180728.txt">Saturday, July 28, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180721.txt">Saturday, July 21, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180714.txt">Saturday, July 14, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180707.txt">Saturday, July 07, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180630.txt">Saturday, June 30, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180623.txt">Saturday, June 23, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180616.txt">Saturday, June 16, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180609.txt">Saturday, June 09, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180602.txt">Saturday, June 02, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180526.txt">Saturday, May 26, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180519.txt">Saturday, May 19, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180512.txt">Saturday, May 12, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180505.txt">Saturday, May 05, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180428.txt">Saturday, April 28, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180421.txt">Saturday, April 21, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180414.txt">Saturday, April 14, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180407.txt">Saturday, April 07, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180331.txt">Saturday, March 31, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180324.txt">Saturday, March 24, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180317.txt">Saturday, March 17, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180310.txt">Saturday, March 10, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180303.txt">Saturday, March 03, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180224.txt">Saturday, February 24, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180217.txt">Saturday, February 17, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180210.txt">Saturday, February 10, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180203.txt">Saturday, February 03, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180127.txt">Saturday, January 27, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180120.txt">Saturday, January 20, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180113.txt">Saturday, January 13, 2018</a><br/><a href="data/nyct/turnstile/turnstile_180106.txt">Saturday, January 06, 2018</a><br/><a href="data/nyct/turnstile/turnstile_171230.txt">Saturday, December 30, 2017</a><br/><a href="data/nyct/turnstile/turnstile_171223.txt">Saturday, December 23, 2017</a><br/><a href="data/nyct/turnstile/turnstile_171216.txt">Saturday, December 16, 2017</a><br/><a href="data/nyct/turnstile/turnstile_171209.txt">Saturday, December 09, 2017</a><br/><a href="data/nyct/turnstile/turnstile_171202.txt">Saturday, December 02, 2017</a><br/><a href="data/nyct/turnstile/turnstile_171125.txt">Saturday, November 25, 2017</a><br/><a href="data/nyct/turnstile/turnstile_171118.txt">Saturday, November 18, 2017</a><br/><a href="data/nyct/turnstile/turnstile_171111.txt">Saturday, November 11, 2017</a><br/><a href="data/nyct/turnstile/turnstile_171104.txt">Saturday, November 04, 2017</a><br/><a href="data/nyct/turnstile/turnstile_171028.txt">Saturday, October 28, 2017</a><br/><a href="data/nyct/turnstile/turnstile_171021.txt">Saturday, October 21, 2017</a><br/><a href="data/nyct/turnstile/turnstile_171014.txt">Saturday, October 14, 2017</a><br/><a href="data/nyct/turnstile/turnstile_171007.txt">Saturday, October 07, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170930.txt">Saturday, September 30, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170923.txt">Saturday, September 23, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170916.txt">Saturday, September 16, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170909.txt">Saturday, September 09, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170902.txt">Saturday, September 02, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170826.txt">Saturday, August 26, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170819.txt">Saturday, August 19, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170812.txt">Saturday, August 12, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170805.txt">Saturday, August 05, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170729.txt">Saturday, July 29, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170722.txt">Saturday, July 22, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170715.txt">Saturday, July 15, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170708.txt">Saturday, July 08, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170701.txt">Saturday, July 01, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170624.txt">Saturday, June 24, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170617.txt">Saturday, June 17, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170610.txt">Saturday, June 10, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170603.txt">Saturday, June 03, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170527.txt">Saturday, May 27, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170520.txt">Saturday, May 20, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170513.txt">Saturday, May 13, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170506.txt">Saturday, May 06, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170429.txt">Saturday, April 29, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170422.txt">Saturday, April 22, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170415.txt">Saturday, April 15, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170408.txt">Saturday, April 08, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170401.txt">Saturday, April 01, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170325.txt">Saturday, March 25, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170318.txt">Saturday, March 18, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170311.txt">Saturday, March 11, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170304.txt">Saturday, March 04, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170225.txt">Saturday, February 25, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170218.txt">Saturday, February 18, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170211.txt">Saturday, February 11, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170204.txt">Saturday, February 04, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170128.txt">Saturday, January 28, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170121.txt">Saturday, January 21, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170114.txt">Saturday, January 14, 2017</a><br/><a href="data/nyct/turnstile/turnstile_170107.txt">Saturday, January 07, 2017</a><br/><a href="data/nyct/turnstile/turnstile_161231.txt">Saturday, December 31, 2016</a><br/><a href="data/nyct/turnstile/turnstile_161224.txt">Saturday, December 24, 2016</a><br/><a href="data/nyct/turnstile/turnstile_161217.txt">Saturday, December 17, 2016</a><br/><a href="data/nyct/turnstile/turnstile_161210.txt">Saturday, December 10, 2016</a><br/><a href="data/nyct/turnstile/turnstile_161203.txt">Saturday, December 03, 2016</a><br/><a href="data/nyct/turnstile/turnstile_161126.txt">Saturday, November 26, 2016</a><br/><a href="data/nyct/turnstile/turnstile_161119.txt">Saturday, November 19, 2016</a><br/><a href="data/nyct/turnstile/turnstile_161112.txt">Saturday, November 12, 2016</a><br/><a href="data/nyct/turnstile/turnstile_161105.txt">Saturday, November 05, 2016</a><br/><a href="data/nyct/turnstile/turnstile_161029.txt">Saturday, October 29, 2016</a><br/><a href="data/nyct/turnstile/turnstile_161022.txt">Saturday, October 22, 2016</a><br/><a href="data/nyct/turnstile/turnstile_161015.txt">Saturday, October 15, 2016</a><br/><a href="data/nyct/turnstile/turnstile_161008.txt">Saturday, October 08, 2016</a><br/><a href="data/nyct/turnstile/turnstile_161001.txt">Saturday, October 01, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160924.txt">Saturday, September 24, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160917.txt">Saturday, September 17, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160910.txt">Saturday, September 10, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160903.txt">Saturday, September 03, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160827.txt">Saturday, August 27, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160820.txt">Saturday, August 20, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160813.txt">Saturday, August 13, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160806.txt">Saturday, August 06, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160730.txt">Saturday, July 30, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160723.txt">Saturday, July 23, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160716.txt">Saturday, July 16, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160709.txt">Saturday, July 09, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160702.txt">Saturday, July 02, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160625.txt">Saturday, June 25, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160618.txt">Saturday, June 18, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160611.txt">Saturday, June 11, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160604.txt">Saturday, June 04, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160528.txt">Saturday, May 28, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160521.txt">Saturday, May 21, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160514.txt">Saturday, May 14, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160507.txt">Saturday, May 07, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160430.txt">Saturday, April 30, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160423.txt">Saturday, April 23, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160416.txt">Saturday, April 16, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160409.txt">Saturday, April 09, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160402.txt">Saturday, April 02, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160326.txt">Saturday, March 26, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160319.txt">Saturday, March 19, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160312.txt">Saturday, March 12, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160305.txt">Saturday, March 05, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160227.txt">Saturday, February 27, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160220.txt">Saturday, February 20, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160213.txt">Saturday, February 13, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160206.txt">Saturday, February 06, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160130.txt">Saturday, January 30, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160123.txt">Saturday, January 23, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160116.txt">Saturday, January 16, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160109.txt">Saturday, January 09, 2016</a><br/><a href="data/nyct/turnstile/turnstile_160102.txt">Saturday, January 02, 2016</a><br/><a href="data/nyct/turnstile/turnstile_151226.txt">Saturday, December 26, 2015</a><br/><a href="data/nyct/turnstile/turnstile_151219.txt">Saturday, December 19, 2015</a><br/><a href="data/nyct/turnstile/turnstile_151212.txt">Saturday, December 12, 2015</a><br/><a href="data/nyct/turnstile/turnstile_151205.txt">Saturday, December 05, 2015</a><br/><a href="data/nyct/turnstile/turnstile_151128.txt">Saturday, November 28, 2015</a><br/><a href="data/nyct/turnstile/turnstile_151121.txt">Saturday, November 21, 2015</a><br/><a href="data/nyct/turnstile/turnstile_151114.txt">Saturday, November 14, 2015</a><br/><a href="data/nyct/turnstile/turnstile_151107.txt">Saturday, November 07, 2015</a><br/><a href="data/nyct/turnstile/turnstile_151031.txt">Saturday, October 31, 2015</a><br/><a href="data/nyct/turnstile/turnstile_151024.txt">Saturday, October 24, 2015</a><br/><a href="data/nyct/turnstile/turnstile_151017.txt">Saturday, October 17, 2015</a><br/><a href="data/nyct/turnstile/turnstile_151010.txt">Saturday, October 10, 2015</a><br/><a href="data/nyct/turnstile/turnstile_151003.txt">Saturday, October 03, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150926.txt">Saturday, September 26, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150919.txt">Saturday, September 19, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150912.txt">Saturday, September 12, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150905.txt">Saturday, September 05, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150829.txt">Saturday, August 29, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150822.txt">Saturday, August 22, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150815.txt">Saturday, August 15, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150808.txt">Saturday, August 08, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150801.txt">Saturday, August 01, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150725.txt">Saturday, July 25, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150718.txt">Saturday, July 18, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150711.txt">Saturday, July 11, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150704.txt">Saturday, July 04, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150627.txt">Saturday, June 27, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150620.txt">Saturday, June 20, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150613.txt">Saturday, June 13, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150606.txt">Saturday, June 06, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150530.txt">Saturday, May 30, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150523.txt">Saturday, May 23, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150516.txt">Saturday, May 16, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150509.txt">Saturday, May 09, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150502.txt">Saturday, May 02, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150425.txt">Saturday, April 25, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150418.txt">Saturday, April 18, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150411.txt">Saturday, April 11, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150404.txt">Saturday, April 04, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150328.txt">Saturday, March 28, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150321.txt">Saturday, March 21, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150314.txt">Saturday, March 14, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150307.txt">Saturday, March 07, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150228.txt">Saturday, February 28, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150221.txt">Saturday, February 21, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150214.txt">Saturday, February 14, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150207.txt">Saturday, February 07, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150131.txt">Saturday, January 31, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150124.txt">Saturday, January 24, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150117.txt">Saturday, January 17, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150110.txt">Saturday, January 10, 2015</a><br/><a href="data/nyct/turnstile/turnstile_150103.txt">Saturday, January 03, 2015</a><br/><a href="data/nyct/turnstile/turnstile_141227.txt">Saturday, December 27, 2014</a><br/><a href="data/nyct/turnstile/turnstile_141220.txt">Saturday, December 20, 2014</a><br/><a href="data/nyct/turnstile/turnstile_141213.txt">Saturday, December 13, 2014</a><br/><a href="data/nyct/turnstile/turnstile_141206.txt">Saturday, December 06, 2014</a><br/><a href="data/nyct/turnstile/turnstile_141129.txt">Saturday, November 29, 2014</a><br/><a href="data/nyct/turnstile/turnstile_141122.txt">Saturday, November 22, 2014</a><br/><a href="data/nyct/turnstile/turnstile_141115.txt">Saturday, November 15, 2014</a><br/><a href="data/nyct/turnstile/turnstile_141108.txt">Saturday, November 08, 2014</a><br/><a href="data/nyct/turnstile/turnstile_141101.txt">Saturday, November 01, 2014</a><br/><a href="data/nyct/turnstile/turnstile_141025.txt">Saturday, October 25, 2014</a><br/><a href="data/nyct/turnstile/turnstile_141018.txt">Saturday, October 18, 2014</a><br/><a href="data/nyct/turnstile/turnstile_141011.txt">Saturday, October 11, 2014</a><br/><a href="data/nyct/turnstile/turnstile_141004.txt">Saturday, October 04, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140927.txt">Saturday, September 27, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140920.txt">Saturday, September 20, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140913.txt">Saturday, September 13, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140906.txt">Saturday, September 06, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140830.txt">Saturday, August 30, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140823.txt">Saturday, August 23, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140816.txt">Saturday, August 16, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140809.txt">Saturday, August 09, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140802.txt">Saturday, August 02, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140726.txt">Saturday, July 26, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140719.txt">Saturday, July 19, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140712.txt">Saturday, July 12, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140705.txt">Saturday, July 05, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140628.txt">Saturday, June 28, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140621.txt">Saturday, June 21, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140614.txt">Saturday, June 14, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140607.txt">Saturday, June 07, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140531.txt">Saturday, May 31, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140524.txt">Saturday, May 24, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140517.txt">Saturday, May 17, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140510.txt">Saturday, May 10, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140503.txt">Saturday, May 03, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140426.txt">Saturday, April 26, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140419.txt">Saturday, April 19, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140412.txt">Saturday, April 12, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140405.txt">Saturday, April 05, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140329.txt">Saturday, March 29, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140322.txt">Saturday, March 22, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140315.txt">Saturday, March 15, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140308.txt">Saturday, March 08, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140301.txt">Saturday, March 01, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140222.txt">Saturday, February 22, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140215.txt">Saturday, February 15, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140208.txt">Saturday, February 08, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140201.txt">Saturday, February 01, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140125.txt">Saturday, January 25, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140118.txt">Saturday, January 18, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140111.txt">Saturday, January 11, 2014</a><br/><a href="data/nyct/turnstile/turnstile_140104.txt">Saturday, January 04, 2014</a><br/><a href="data/nyct/turnstile/turnstile_131228.txt">Saturday, December 28, 2013</a><br/><a href="data/nyct/turnstile/turnstile_131221.txt">Saturday, December 21, 2013</a><br/><a href="data/nyct/turnstile/turnstile_131214.txt">Saturday, December 14, 2013</a><br/><a href="data/nyct/turnstile/turnstile_131207.txt">Saturday, December 07, 2013</a><br/><a href="data/nyct/turnstile/turnstile_131130.txt">Saturday, November 30, 2013</a><br/><a href="data/nyct/turnstile/turnstile_131123.txt">Saturday, November 23, 2013</a><br/><a href="data/nyct/turnstile/turnstile_131116.txt">Saturday, November 16, 2013</a><br/><a href="data/nyct/turnstile/turnstile_131109.txt">Saturday, November 09, 2013</a><br/><a href="data/nyct/turnstile/turnstile_131102.txt">Saturday, November 02, 2013</a><br/><a href="data/nyct/turnstile/turnstile_131026.txt">Saturday, October 26, 2013</a><br/><a href="data/nyct/turnstile/turnstile_131019.txt">Saturday, October 19, 2013</a><br/><a href="data/nyct/turnstile/turnstile_131012.txt">Saturday, October 12, 2013</a><br/><a href="data/nyct/turnstile/turnstile_131005.txt">Saturday, October 05, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130928.txt">Saturday, September 28, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130921.txt">Saturday, September 21, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130914.txt">Saturday, September 14, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130907.txt">Saturday, September 07, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130831.txt">Saturday, August 31, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130824.txt">Saturday, August 24, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130817.txt">Saturday, August 17, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130810.txt">Saturday, August 10, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130803.txt">Saturday, August 03, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130727.txt">Saturday, July 27, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130720.txt">Saturday, July 20, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130713.txt">Saturday, July 13, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130706.txt">Saturday, July 06, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130629.txt">Saturday, June 29, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130622.txt">Saturday, June 22, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130615.txt">Saturday, June 15, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130608.txt">Saturday, June 08, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130601.txt">Saturday, June 01, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130525.txt">Saturday, May 25, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130518.txt">Saturday, May 18, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130511.txt">Saturday, May 11, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130504.txt">Saturday, May 04, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130427.txt">Saturday, April 27, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130420.txt">Saturday, April 20, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130413.txt">Saturday, April 13, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130406.txt">Saturday, April 06, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130330.txt">Saturday, March 30, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130323.txt">Saturday, March 23, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130316.txt">Saturday, March 16, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130309.txt">Saturday, March 09, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130302.txt">Saturday, March 02, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130223.txt">Saturday, February 23, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130216.txt">Saturday, February 16, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130209.txt">Saturday, February 09, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130202.txt">Saturday, February 02, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130126.txt">Saturday, January 26, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130119.txt">Saturday, January 19, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130112.txt">Saturday, January 12, 2013</a><br/><a href="data/nyct/turnstile/turnstile_130105.txt">Saturday, January 05, 2013</a><br/><a href="data/nyct/turnstile/turnstile_121229.txt">Saturday, December 29, 2012</a><br/><a href="data/nyct/turnstile/turnstile_121222.txt">Saturday, December 22, 2012</a><br/><a href="data/nyct/turnstile/turnstile_121215.txt">Saturday, December 15, 2012</a><br/><a href="data/nyct/turnstile/turnstile_121208.txt">Saturday, December 08, 2012</a><br/><a href="data/nyct/turnstile/turnstile_121201.txt">Saturday, December 01, 2012</a><br/><a href="data/nyct/turnstile/turnstile_121124.txt">Saturday, November 24, 2012</a><br/><a href="data/nyct/turnstile/turnstile_121117.txt">Saturday, November 17, 2012</a><br/><a href="data/nyct/turnstile/turnstile_121110.txt">Saturday, November 10, 2012</a><br/><a href="data/nyct/turnstile/turnstile_121103.txt">Saturday, November 03, 2012</a><br/><a href="data/nyct/turnstile/turnstile_121027.txt">Saturday, October 27, 2012</a><br/><a href="data/nyct/turnstile/turnstile_121020.txt">Saturday, October 20, 2012</a><br/><a href="data/nyct/turnstile/turnstile_121013.txt">Saturday, October 13, 2012</a><br/><a href="data/nyct/turnstile/turnstile_121006.txt">Saturday, October 06, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120929.txt">Saturday, September 29, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120922.txt">Saturday, September 22, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120915.txt">Saturday, September 15, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120908.txt">Saturday, September 08, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120901.txt">Saturday, September 01, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120825.txt">Saturday, August 25, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120818.txt">Saturday, August 18, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120811.txt">Saturday, August 11, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120804.txt">Saturday, August 04, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120728.txt">Saturday, July 28, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120721.txt">Saturday, July 21, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120714.txt">Saturday, July 14, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120707.txt">Saturday, July 07, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120630.txt">Saturday, June 30, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120623.txt">Saturday, June 23, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120616.txt">Saturday, June 16, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120609.txt">Saturday, June 09, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120602.txt">Saturday, June 02, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120526.txt">Saturday, May 26, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120519.txt">Saturday, May 19, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120512.txt">Saturday, May 12, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120505.txt">Saturday, May 05, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120428.txt">Saturday, April 28, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120421.txt">Saturday, April 21, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120414.txt">Saturday, April 14, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120407.txt">Saturday, April 07, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120331.txt">Saturday, March 31, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120324.txt">Saturday, March 24, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120317.txt">Saturday, March 17, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120310.txt">Saturday, March 10, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120303.txt">Saturday, March 03, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120225.txt">Saturday, February 25, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120218.txt">Saturday, February 18, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120211.txt">Saturday, February 11, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120204.txt">Saturday, February 04, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120128.txt">Saturday, January 28, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120121.txt">Saturday, January 21, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120114.txt">Saturday, January 14, 2012</a><br/><a href="data/nyct/turnstile/turnstile_120107.txt">Saturday, January 07, 2012</a><br/><a href="data/nyct/turnstile/turnstile_111231.txt">Saturday, December 31, 2011</a><br/><a href="data/nyct/turnstile/turnstile_111224.txt">Saturday, December 24, 2011</a><br/><a href="data/nyct/turnstile/turnstile_111219.txt">Monday, December 19, 2011</a><br/><a href="data/nyct/turnstile/turnstile_111210.txt">Saturday, December 10, 2011</a><br/><a href="data/nyct/turnstile/turnstile_111203.txt">Saturday, December 03, 2011</a><br/><a href="data/nyct/turnstile/turnstile_111126.txt">Saturday, November 26, 2011</a><br/><a href="data/nyct/turnstile/turnstile_111119.txt">Saturday, November 19, 2011</a><br/><a href="data/nyct/turnstile/turnstile_111112.txt">Saturday, November 12, 2011</a><br/><a href="data/nyct/turnstile/turnstile_111105.txt">Saturday, November 05, 2011</a><br/><a href="data/nyct/turnstile/turnstile_111029.txt">Saturday, October 29, 2011</a><br/><a href="data/nyct/turnstile/turnstile_111022.txt">Saturday, October 22, 2011</a><br/><a href="data/nyct/turnstile/turnstile_111015.txt">Saturday, October 15, 2011</a><br/><a href="data/nyct/turnstile/turnstile_111008.txt">Saturday, October 08, 2011</a><br/><a href="data/nyct/turnstile/turnstile_111001.txt">Saturday, October 01, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110924.txt">Saturday, September 24, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110917.txt">Saturday, September 17, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110910.txt">Saturday, September 10, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110903.txt">Saturday, September 03, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110827.txt">Saturday, August 27, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110820.txt">Saturday, August 20, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110813.txt">Saturday, August 13, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110806.txt">Saturday, August 06, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110730.txt">Saturday, July 30, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110723.txt">Saturday, July 23, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110716.txt">Saturday, July 16, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110709.txt">Saturday, July 09, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110702.txt">Saturday, July 02, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110625.txt">Saturday, June 25, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110618.txt">Saturday, June 18, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110611.txt">Saturday, June 11, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110604.txt">Saturday, June 04, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110528.txt">Saturday, May 28, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110521.txt">Saturday, May 21, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110514.txt">Saturday, May 14, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110507.txt">Saturday, May 07, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110430.txt">Saturday, April 30, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110423.txt">Saturday, April 23, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110416.txt">Saturday, April 16, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110409.txt">Saturday, April 09, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110402.txt">Saturday, April 02, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110326.txt">Saturday, March 26, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110319.txt">Saturday, March 19, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110312.txt">Saturday, March 12, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110305.txt">Saturday, March 05, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110226.txt">Saturday, February 26, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110219.txt">Saturday, February 19, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110212.txt">Saturday, February 12, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110205.txt">Saturday, February 05, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110129.txt">Saturday, January 29, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110122.txt">Saturday, January 22, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110115.txt">Saturday, January 15, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110108.txt">Saturday, January 08, 2011</a><br/><a href="data/nyct/turnstile/turnstile_110101.txt">Saturday, January 01, 2011</a><br/><a href="data/nyct/turnstile/turnstile_101225.txt">Saturday, December 25, 2010</a><br/><a href="data/nyct/turnstile/turnstile_101218.txt">Saturday, December 18, 2010</a><br/><a href="data/nyct/turnstile/turnstile_101211.txt">Saturday, December 11, 2010</a><br/><a href="data/nyct/turnstile/turnstile_101204.txt">Saturday, December 04, 2010</a><br/><a href="data/nyct/turnstile/turnstile_101127.txt">Saturday, November 27, 2010</a><br/><a href="data/nyct/turnstile/turnstile_101120.txt">Saturday, November 20, 2010</a><br/><a href="data/nyct/turnstile/turnstile_101113.txt">Saturday, November 13, 2010</a><br/><a href="data/nyct/turnstile/turnstile_101106.txt">Saturday, November 06, 2010</a><br/><a href="data/nyct/turnstile/turnstile_101030.txt">Saturday, October 30, 2010</a><br/><a href="data/nyct/turnstile/turnstile_101023.txt">Saturday, October 23, 2010</a><br/><a href="data/nyct/turnstile/turnstile_101016.txt">Saturday, October 16, 2010</a><br/><a href="data/nyct/turnstile/turnstile_101009.txt">Saturday, October 09, 2010</a><br/><a href="data/nyct/turnstile/turnstile_101002.txt">Saturday, October 02, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100925.txt">Saturday, September 25, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100918.txt">Saturday, September 18, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100911.txt">Saturday, September 11, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100904.txt">Saturday, September 04, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100828.txt">Saturday, August 28, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100821.txt">Saturday, August 21, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100814.txt">Saturday, August 14, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100807.txt">Saturday, August 07, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100731.txt">Saturday, July 31, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100724.txt">Saturday, July 24, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100717.txt">Saturday, July 17, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100710.txt">Saturday, July 10, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100703.txt">Saturday, July 03, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100626.txt">Saturday, June 26, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100619.txt">Saturday, June 19, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100612.txt">Saturday, June 12, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100605.txt">Saturday, June 05, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100522.txt">Saturday, May 22, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100515.txt">Saturday, May 15, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100508.txt">Saturday, May 08, 2010</a><br/><a href="data/nyct/turnstile/turnstile_100505.txt">Wednesday, May 05, 2010</a><br/> </div>
    </div>
    <!-- End Content -->
    </div> <!-- close contentbox -->
    <!-- JavaScript Includes -->
    <script src="/js/csshorizontalmenu.js" type="text/javascript"></script>
    <script type="text/javascript">
    $(document).ready(function() {
    $("#printfriendly").click(function() {
    var s = document.location.search;
    if (!s)
    window.open(document.location.pathname + '?print=1', '', 'scrollbars=1');
    else
    window.open(document.location.pathname + s + '&print=1', '', 'scrollbars=1');
    return false;
    });
    });
    </script>
    <div class="container clear">
    <div class="span-15" style="text-align: left;margin-right: 12px;">
    <div id="translate">
    <div id="google_translate_element">
    <div class="span-15" id="temp_GT">
    <ul style="margin: 0;">
    <li class="list_f last_list_f first_list_f"><span style="color: #0055AA; font-weight: bold; margin-right: 5px;">Google Translate</span><img alt="" src="/siteimages/google_logo.png" style="vertical-align: baseline;"/></li>
    </ul>
    </div>
    </div><!-- close google_translate_element -->
    </div><!-- close translate -->
    </div><!-- close span-14 last -->
    </div> <!-- Close of Container -->
    <script>
    function googleTranslateElementInit() {
    new google.translate.TranslateElement({
    pageLanguage: 'en',
    layout: google.translate.TranslateElement.InlineLayout.SIMPLE
    }, 'google_translate_element');
    }
    
    $("#temp_GT").click(function() {
    var fileref = document.createElement('script');
    fileref.setAttribute("type", "text/javascript");
    fileref.setAttribute("src", "http://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit");
    
    document.getElementsByTagName("head")[0].appendChild(fileref);
    $("#temp_GT").hide();
    });
    </script>
    <script src="/js/webtrends.load.js" type="text/javascript"></script>
    <script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
    
    ga('create', 'UA-51590636-1', 'mta.info');
    ga('send', 'pageview');
    </script>
    <script type="text/javascript">
    /* <![CDATA[ */
    var google_conversion_id = 970467739;
    var google_custom_params = window.google_tag_params;
    var google_remarketing_only = true;
    /* ]]> */
    </script>
    <script src="//www.googleadservices.com/pagead/conversion.js" type="text/javascript">
    </script>
    <noscript>
    <div style="display:inline;">
    <img alt="" height="1" src="//googleads.g.doubleclick.net/pagead/viewthroughconversion/970467739/?guid=ON&amp;script=0" style="border-style:none;" width="1"/>
    </div>
    </noscript></div> <!-- close mainbox -->
    </body></html>
    '''
#--------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------#



