print('GO seedfeed.py -> starting IMPORTs')
#from sites import *
from utilities import *
from discordts import *
#from mydiscord import *
#from mydiscord.db_dm4c import *
#from mydiscord.discord_util import *
#from mydiscord.cmd_deposit import *
#from mydiscord.cmd_email import *


'''
# https://discordapp.com/developers/applications/
# https://discordapp.com/oauth2/authorize?client_id=<sites/__init__.py>&scope=bot&permissions=8
#NOTE: '$ pip3' == '$ python3.6 -m pip'
    $ pip3 install discord.py
    $ python3.6 -m pip install discord.py
'''
import discord
# $ python3 seedfeed.py

filename = 'seedfeed.py'
logenter(filename, "\n IMPORTs complete:- STARTING -> file '%s' . . . " % filename, simpleprint=False, tprint=True)

TOKEN = sites.cDiscordTOKEN
client = discord.Client()

#====================================================#
# globals                                            #
#====================================================#
#lst_supportHashTagIds = ['#1892', '#6245', '#8552'] # house#1892, Nx2#6245, BlckPhantom#8552     <- DM4C server
lst_supportHashTagIds = ['#1892', '#6785', '#8985'] # house#1892, NAD010286#6785, afrosatoshi#8985 <- torrent seed server
#lst_supportHashTagIds = ['#1892']
str_thisGuildName = 'BitContent'
str_userName = None
i_userId = None
i_totGuildCnt = None
this_guild = None
lst_channels = None
lst_guildSupportMems = None


#====================================================#
##              support                             ##
#====================================================#
def printThisGuildDetails():
    funcname = '(%s) printThisGuildDetails' % filename
    logenter(funcname, simpleprint=False, tprint=False)
    if not this_guild or not lst_channels:
        logerror(filename, "'this_guild' or 'lst_channels' is nil; returning", simpleprint=False)
        return

    for member in lst_guildSupportMems:
        loginfo(filename, " found support member: '%s'" % member, simpleprint=True)

    for channel in lst_channels:
        loginfo(filename, " found channel: '%s'" % channel.name, simpleprint=True)

def getThisGuild(guilds):
    funcname = '(%s) getThisGuild' % filename
    logenter(funcname, '(guilds=%s)' % str(guilds), simpleprint=False, tprint=True)
    for guild in guilds:
        if guild.name == str_thisGuildName:
            return guild


#====================================================#
##              database support                    ##
#====================================================#
def DBQueryMemberJoin(member):
    user = userDictFromDiscordMem(member)
    dict = {cColPlayerDiscIdFull:user['userFull'],
            cColPlayerDiscIdName:user['userName'],
            cColPlayerDiscIdTag:user['userHashTagId'],
            cColPlayerFirstIpAddr:'no-ip-record'}
    player_id = procCallMemberServerJoin(dbQueryDict=dict)

def DBQueryMemberRemove(member):
    user = userDictFromDiscordMem(member)
    dict = {cColPlayerDiscIdFull:user['userFull'],
            cColPlayerDiscIdTag:user['userHashTagId'],
            cColPlayerFirstIpAddr:'no-ip-record'}
    player_id = procCallMemberServerRemove(dbQueryDict=dict)

def DBQueryMemberMsg(member, strMsgContent):
    user = userDictFromDiscordMem(member)
    dict = {cColPlayerDiscIdFull:user['userFull'],
            cColPlayerDiscIdTag:user['userHashTagId'],
            cColEventDescr    : strMsgContent,
            cColPlayerFirstIpAddr:'no-ip-record'}
    player_id = procCallMemberMsgReceived(dbQueryDict=dict)

def DBQueryMemberBalance(member):
    user = userDictFromDiscordMem(member)
    dict = {cColEventDiscIdTag: user['userHashTagId']}
    balance = procCallMemberGetBalanceDHT(dbQueryDict=dict)
    return balance


#====================================================#
##              aync support                        ##
#====================================================#
async def sendMemberJoinPrivateMsg(member):
    msg = "hello, welcome to DM4C . . . I will be your guide for this server..."
    await member.send(msg)
    
    msg = "please use ``!help`` for more details, or ``!deposit`` to start a deposit"
    await member.send(msg)

async def sendMemberLeavePrivateMsg(member):
    strMention = member.mention
    msg = "%s Bye... see ya!" % strMention
    await member.send(msg)

async def sendMemberJoinPublicChannelMsg(member, channel):
    strMention = member.mention
    msg = "hey %s thanks for joining DM4C . . . ```please use \"!help\" for more details```" % strMention
    await channel.send(msg)

async def sendMemberLeavePublicChannelMsg(member, channel):
    strMention = member.mention
    msg = "%s Bye... see ya!" % strMention
    await channel.send(msg)

async def sendPublicAckReponse(channel, message, strCmd):
    if channel.type != discord.ChannelType.private:
        msgPublic = "Hi {0.author.mention} . . . please check your DMs for your ``%s`` response".format(message) % strCmd
        await channel.send(msgPublic)

async def sendPrivateAckResponse(channel, member, message, strCmd):
    if channel.type == discord.ChannelType.private:
        msgPrivate = "Hi {0.author.mention}, here is your ``%s`` response . . . ".format(message) % strCmd
        await member.send(msgPrivate)
    else:
        msgPrivate = "Hi {0.author.mention}, here is your ``%s`` response . . . ".format(message) % strCmd
        await member.send(msgPrivate)

async def sendLiveSupportRequests(forMember):
    if not lst_guildSupportMems or len(lst_guildSupportMems) < 1:
        logerror(filename, "'lst_guildSupportMems' is nil or empty; FAILED to send support request; returning", simpleprint=False)
        return

    for supMem in lst_guildSupportMems:
        msg = "```Live support has been requested from user: \"%s\" \n This user is currently expecting a DM```" % forMember
        msg = "Hey {0.mention}... %s".format(supMem) % msg
        await supMem.send(msg)
        printSupportRequestNotificationSent(supMem, forMember)


#====================================================#
##              event handling support              ##
#====================================================#
@client.event
async def on_member_join(member):
    # print initial member server join data
    loginfo(filename, cStrDivider, simpleprint=True)
    loginfo(filename, 'User JOINED the server...', simpleprint=True)
    printMemberData(member)
    
    # send 'welcome' channel message
    channel = getChannelForName(cStrChanWelcome, lst_channels)
    await sendMemberJoinPublicChannelMsg(member, channel)

    # send private intro message
    await sendMemberJoinPrivateMsg(member)

    # QUERY DATABASE PLAYER -> MEMBER JOINED
    DBQueryMemberJoin(member)
    loginfo(filename, cStrDivider, simpleprint=True)

@client.event
async def on_member_remove(member):
    # print member server leave data
    loginfo(filename, cStrDivider, simpleprint=True)
    loginfo(filename, 'User REMOVED (left|kicked) from server...', simpleprint=True)
    printMemberData(member)

    # send 'welcome' channel message
    channel = getChannelForName(cStrChanWelcome, lst_channels)
    await sendMemberLeavePublicChannelMsg(member, channel)

    # QUERY DATABASE PLAYER -> MEMBER REMOVED(left|kicked)
    DBQueryMemberRemove(member)
    loginfo(filename, cStrDivider, simpleprint=True)

    # send private exit message
    #await sendMemberLeavePrivateMsg(member)

@client.event
async def on_message(message):
    strUserFull = str(message.author)
    strMsgContentOrig = str(message.content)
    strMsgContent = str(message.content).lower()
    member = message.author
    channel = message.channel
    
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # CATCH BOT INSULTS
    strEndCatch = 'fucking stupid ass bot'
    if strMsgContent.endswith(strEndCatch):
        loginfo(filename, cStrDivider, simpleprint=True)
        msg = "{0.author.mention}, YOU'RE a %s : /".format(message) % strEndCatch
        await channel.send(msg)
        printCmdReceived(channel, member, strEndCatch, strMsgContent, strMsgContentOrig)
        loginfo(filename, cStrDivider, simpleprint=True)
        return

    # check if a command was sent
    if not strMsgContent.startswith('!'):
        return


    loginfo(filename, cStrDivider, simpleprint=True)

    # GET COMMAND
    lstMsgContent = strMsgContent.split(' ')
    strCmd = lstMsgContent[0]

    # PRINT/LOG COMMAND
    printCmdReceived(channel, member, strCmd, strMsgContent, strMsgContentOrig)

    # QUERY DATABASE EVENT -> LOG MSG/COMMAND RECEIVED
    DBQueryMemberMsg(member, strMsgContent)

    # CATCH BOT COMPLIMENTS
    if strCmd == '!bestbotever':
        msg = "Aww... shucks {0.author.mention}, you are too kind : )".format(message)
        await channel.send(msg)
        loginfo(filename, cStrDivider, simpleprint=True)
        return

    # SEND CMD PUBLIC ACKNOWLEDGE
    await sendPublicAckReponse(channel, message, strCmd)

    if strCmd == '!hello':
        msg = "Hello {0.author.mention} ```please use \"!help\" and check your DMs for more details```".format(message)
        await member.send(msg)
        loginfo(filename, cStrDivider, simpleprint=True)
        return

    if strCmd == '!help':
        msg = 'Hi {0.author.mention}... you requested some help?'.format(message)
        await member.send(msg)

        usage = ("!help \n"
                 "!deposit \n"
                 "!withdraw \n"
                 "!balance \n"
                 "!RegisterEmail \n"
                 "!LiveSupport \n")

        msg = "The following is a list of commands you may use ```%s```" % usage
        await member.send(msg)
        loginfo(filename, cStrDivider, simpleprint=True)
        return

    # SEND CMD PRIVATE ACKNOWLEDGE
    await sendPrivateAckResponse(channel, member, message, strCmd)

    if strCmd == '!livesupport':
        msg = "Hi {0.author.mention}... ```you requested to speak with a live person, please stand-by and someone will DM you shortly!```".format(message)
        await member.send(msg)
        await sendLiveSupportRequests(member)
        loginfo(filename, cStrDivider, simpleprint=True)
        return

    if strCmd == '!balance':
        # QUERY DATABASE PLAYER -> GET BALANCE
        balance = DBQueryMemberBalance(member)
        msg = f"```your current balance is {balance}```"
        await member.send(msg)
        loginfo(filename, cStrDivider, simpleprint=True)
        return

    if strCmd == '!deposit':
        msg = CMD_deposit(member, lstMsgContent)
        await member.send(msg)
        loginfo(filename, cStrDivider, simpleprint=True)
        return

    if strCmd == '!registeremail':
        msg = CMD_email(member, lstMsgContent)
        await member.send(msg)
        loginfo(filename, cStrDivider, simpleprint=True)
        return

    loginfo(filename, cStrDivider, simpleprint=True)

@client.event
async def on_ready():
    global str_thisGuildName, str_userName, i_totGuildCnt, this_guild, lst_channels, lst_guildSupportMems

    str_userName = client.user.name
    i_userId = client.user.id
    i_totGuildCnt = len(client.guilds)
    this_guild = getThisGuild(client.guilds)
    lst_channels = getChannelsForGuild(this_guild)
    lst_guildSupportMems = getSupportMembersForGuid(this_guild, lst_supportHashTagIds)

    # print initial connection data
    loginfo(filename, cStrDivider, simpleprint=True)
    loginfo(filename, 'Logged in as...', simpleprint=True)
    loginfo(filename, ' userName: %s _ userId: %i' % (str_userName, i_userId), simpleprint=True)
    loginfo(filename, ' i_totGuildCnt: %i \n' % i_totGuildCnt, simpleprint=True)
    loginfo(filename, "Guild/Server name: '%s' _ total channel cnt: %i _ total support cnt: %i" % (this_guild.name, len(lst_channels), len(lst_guildSupportMems)), simpleprint=True)
    printThisGuildDetails()
    loginfo(filename, cStrDivider, simpleprint=True)

#    server_deposit.setDiscordClient(client)

loginfo(filename, "\n CLASSES & FUNCTIONS initialized:- STARTING -> additional '%s' run scripts (if applicable) . . . \n\n" % filename, simpleprint=True)

client.run(TOKEN)

#print('\n')
#print('#======================================================================#')
#loginfo(filename, "\n  DONE Executing additional '%s' run scripts ... \n" % filename, simpleprint=True)


