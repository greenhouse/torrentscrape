print('GO discord_util.py -> starting IMPORTs')
from utilities import * #imports 'from sites import *'

'''
# https://discordapp.com/developers/applications/
# https://discordapp.com/oauth2/authorize?client_id=<sites/__init__.py>&scope=bot&permissions=8
#NOTE: '$ pip3' == '$ python3.6 -m pip'
    $ pip3 install discord.py
    $ python3.7 -m pip install discord.py
'''
import discord

filename = 'discord_util.py'
logenter(filename, "\n IMPORTs complete:- STARTING -> file '%s' . . . " % filename, simpleprint=False, tprint=True)

def userDictFromDiscordMem(member):
    strUserFull = str(member)
    strUserName = str(member.name)
    strUserHashTagId = getUserHashTagIdFromFull(strUserFull)
    strUserHashId = getUserHashTagIdFromFull(strUserFull, False)
    strUserHash = str(hash(member))
    strUserId = str(member.id)
    return {'userFull':strUserFull,
            'userName':strUserName,
            'userHashTagId':strUserHashTagId,
            'userHashId':strUserHashId,
            'userHash':strUserHash,
            'userId':strUserId}

def getSupportMembersForGuid(guild, lstSupportHashTagIds):
    funcname = '(%s) getSupportMembersForGuid' % filename
    logenter(funcname, '(guild=%s)' % str(guild), simpleprint=False, tprint=False)
    lstMembers = []
    for member in guild.members:
        strUserFull = str(member)
        strUserName = str(member.name)
        strUserHashTagId = getUserHashTagIdFromFull(strUserFull)
        if strUserHashTagId in lstSupportHashTagIds:
            lstMembers.append(member)

    return lstMembers

def getUserHashTagIdFromFull(strUserFull, withHashTag=True):
    funcname = '(%s) getUserHashTagIdFromFull' % filename
    logenter(funcname, '(strUserFull=%s, withHashTag=%i)' % (strUserFull, withHashTag), simpleprint=False, tprint=False)
    if not strUserFull:
        logerror(filename, "'strUserFull' is nil; returning None", simpleprint=False)
        return None
    
    idxHash = strUserFull.index('#')
    strhashid = strUserFull[idxHash:]
    if not withHashTag:
        strhashid = strUserFull[idxHash+1:]

    return strhashid

def getChannelForName(strName, lstChannels):
    funcname = '(%s) getChannelForName' % filename
    logenter(funcname, '(strName=%s)' % strName, simpleprint=False, tprint=False)
    if not lstChannels:
        logerror(filename, "'lstChannels' is nil; returning None", simpleprint=False)
        return None
    
    for channel in lstChannels:
        if channel.name == strName:
            loginfo(funcname, 'found channel.name: %s' % strName, simpleprint=True, tprint=False)
            return channel

    logwarning(funcname, 'channel.name: %s NOT FOUND; returning None' % strName, simpleprint=False)
    return None

def printMemberData(member):
    funcname = '(%s) printMemberData' % filename
    logenter(funcname, simpleprint=False, tprint=False)
    
    strUserFull = str(member)
    strUserName = str(member.name)
    strUserHashTagId = getUserHashTagIdFromFull(strUserFull)
    strUserHash = str(hash(member))
    strUserId = str(member.id)

    loginfo(filename, ' member: %s' % strUserFull, simpleprint=True)
    loginfo(filename, ' member.name: %s' % strUserName, simpleprint=True)
    loginfo(filename, ' member hashTagId: %s' % strUserHashTagId, simpleprint=True)
    loginfo(filename, ' member.id: %s' % strUserId, simpleprint=True)
    loginfo(filename, ' hash(member): %s' % strUserHash, simpleprint=True)

def printCmdReceived(channel, member, strCmd, strMsgContent, strMsgContentOrig):
    funcname = '(%s) printCmdReceived' % filename
    logenter(funcname, simpleprint=False, tprint=False)

    #strChanName = channel.recipient.name if channel.type == discord.ChannelType.private else channel.name
    strChanName = "~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ DM ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~" if channel.type == discord.ChannelType.private else channel.name
    
    loginfo(filename, 'CMD Message Received... (%s)' % strCmd, simpleprint=True)
    loginfo(filename, ' channel.name: %s' % strChanName, simpleprint=True)
    printMemberData(member)
    loginfo(filename, ' strCmd: %s' % strCmd, simpleprint=True)
    loginfo(filename, ' strMsgContent: %s' % strMsgContent, simpleprint=True)
    loginfo(filename, ' strMsgContentOrig: %s' % strMsgContentOrig, simpleprint=True)

def printSupportRequestNotificationSent(toMember, forMember):
    funcname = '(%s) printSupportRequestNotificationSent' % filename
    logenter(funcname, simpleprint=False, tprint=False)

    loginfo(filename, cStrDivider, simpleprint=True)
    loginfo(filename, 'LIVE SUPPORT Request Notification Sent...', simpleprint=True)
    loginfo(filename, ' to member: %s' % toMember, simpleprint=True)
    loginfo(filename, ' for member: %s' % forMember, simpleprint=True)
    loginfo(filename, cStrDivider, simpleprint=True)

def getChannelsForGuild(guild):
    funcname = '(%s) getChannelsForGuild' % filename
    logenter(funcname, '(guild=%s)' % str(guild), simpleprint=False, tprint=True)
    lstChannels = []
    for channel in guild.channels:
        lstChannels.append(channel)

    return lstChannels

loginfo(filename, "\n CLASSES & FUNCTIONS initialized:- STARTING -> additional '%s' run scripts (if applicable) . . . \n\n" % filename, simpleprint=True)


#print('\n')
#print('#======================================================================#')
#loginfo(filename, "\n  DONE Executing additional '%s' run scripts ... \n" % filename, simpleprint=True)


