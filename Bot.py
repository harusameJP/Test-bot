import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("おはよう"):
        if client.user != message.author:
            m = "おはようございます" + message.author.name + "さん！"
            await message.channel.send(m)

client.run("NjEyNDEzMTExODQzOTQ2NTQ5.XViEDw.CGzgaFMosLWK-bZqd9tEtjMN4a4
")
