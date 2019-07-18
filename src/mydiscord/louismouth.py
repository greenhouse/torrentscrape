# Work with Python 3.6
print('GO louismouth.py -> starting IMPORTs')
import discord

TOKEN = 'NTY4MjQ2ODU5MzA3Njc5NzQ0.XLfTYQ.ShlDQ-J8I4xPLvZo-uCd0Fb4s3s'

client = discord.Client()

hashIdLouis = '#5743'
hashIdHouse = '#1892'

lst_badBoys = [hashIdLouis,
               hashIdHouse]
lst_badWords = ['fuck',
                'fucking',
                'fuckin',
                'fuk',
                'fuc',
                'fuker',
                'fukr',
                'fukre',
                'shit',
                'cock',
                'cok',
                'cocksucker',
                'coksucker',
                'coksuker',
                'ass',
                'ass-hole',
                'asshole',
                'retarded',
                'retarted',
                'fucker',
                'balls',
                'suck',
                'sucks',
                'sucker',
                'lick',
                'piss',
                'cunt',
                'gay',
                'fag',
                'fagg',
                'faggot',
                'faggit',
                'dick',
                'stink']

lst_annoyWords = ['hahaha','hahahah','haha']

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
#    if message.author == client.user:
#        return
#
#    if message.content.startswith('!hello'):
#        msg = 'Hello {0.author.mention}'.format(message)
#        channel = message.channel
#        #await client.send_message(message.channel, msg)
#        await channel.send(msg)



    strfullhand = str(message.author)
    strMsgContent = str(message.content).lower()
    strMsgArr = strMsgContent.split(' ')
    
    idxHash = strfullhand.index('#')
    strhashid = strfullhand[idxHash:]

    if strhashid in lst_badBoys:
        print('message.author: %s' % strfullhand)
        print('message.content: %s' % strMsgContent)
        print('idxHash: %i' % idxHash)
        print('strhashid: %s' % strhashid)
        for strWord in strMsgArr:
            if strWord in lst_badWords:
                msg = "Whoopsy!! So Sorry! \nMy mother taught me better than to use words like '%s' \nI will certainly try harder to watch my language in front of the laddies : ) \n" % strWord
                channel = message.channel
                await channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
