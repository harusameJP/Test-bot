import Discord

TOKEN = 'NjE3NjMyNDYyOTYwNDU5Nzc5.XWt9SA.IdhKFxURxyygPDwKxwzRTE72x5g'

client = discord.Client()

@client.event
async def on_ready():
    print('LoginSuccess!')

@client.event
async def on_ready():
    
    if message.author.bot:
    return
if message.content == '/help':
    await message.channel.send('このbotはテスト用です。')
    
    client.run('NjE3NjMyNDYyOTYwNDU5Nzc5.XWt9SA.IdhKFxURxyygPDwKxwzRTE72x5g')