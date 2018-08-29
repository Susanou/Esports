import discord
import asyncio
import re

TOKEN = 'NDg0MTgwOTkwNDIwNTgyNDEx.DmeSqQ.Fcy5qNyhU_57Ky5MmgmGWqDwo2U'

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def get_member_role(serv):
    member_role = discord.utils.get(serv.roles, name="cwru")
    return(member_role)

@client.event
async def on_message(message):
    if message.author.name.endswith("Bot"):
        print("me")
        return None
    elif message.channel.name == "introductions":

        cwru = discord.utils.get(message.server.roles, name = "cwru")

        if message.author.roles:
            for value in message.author.roles:
                if value == cwru:
                    return None
        if name_formatted(message.author.nick):
            await client.send_message(message.channel, "Welcome {}, give me a second to flip some bits and you should be able to use our channels.".format(message.author.mention))
            role = await get_member_role(message.server)
            await client.add_roles(message.author, role)
        else:
            await client.send_message(message.channel, "Hi {}, please edit your nickname to our server's standard [real name] ([in-game name]) and post your introduction again.".format(message.author.mention))

def name_formatted(name):
    print(name)
    if name == None:
        return

    pattern = re.compile("^.+\(.+\)$")
    if pattern.match(name):
        return(True)
    else:
        return(False)

#@client.event
#async def on_message(message):
#    print(new_member_role)
#    if message.content.startswith('!text'):
#        counter=0
#        tmp = await client.send_message(message.channel, 'Calculating messages...')
#        async for log in client.logs_from(message.channel, limit=100):
#            if log.author == message.author:
#                counter += 1
#
#        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
#    elif message.content.startswith('!sleep'):
#        await asyncio.sleep(5)
#        await client.send_message(message.channel, 'Done sleeping')

client.run(TOKEN)
