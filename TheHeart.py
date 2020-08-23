#https://discord.com/api/oauth2/authorize?client_id=745670425811353690&permissions=121920&scope=bot

import discord

import gifRender


client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
    massage_content = message.content
    split = massage_content.split()
    if message.author == client.user:
        return
    
    if split[0] == "g!":
        await message.channel.send(gifRender
.gif_link(split[1]))
        
        


client.run(Your Token Goes here)
