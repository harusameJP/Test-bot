import discord

client = discord.Client(NjE3NjMyNDYyOTYwNDU5Nzc5.XWt9SA.IdhKFxURxyygPDwKxwzRTE72x5g)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('NjE3NjMyNDYyOTYwNDU5Nzc5.XWt9SA.IdhKFxURxyygPDwKxwzRTE72x5g')
