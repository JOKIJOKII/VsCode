# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('{0.user} Tá Online BB!'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Acorda Sunga'):
        await message.channel.send('vai toma no seu cu viado')
      
    if message.author == client.user:
        return

      # Responder "Bom dia" se o usuário digitar "Bom dia"
    if message.content.lower() == "bom dia":
        await message.channel.send("Bom dia! https://cdn.discordapp.com/attachments/1221241667064037516/1221881341990277322/IMG-20240325-WA0053.jpg?ex=661430ad&is=6601bbad&hm=e7217555da4ae49563b344b7c21f9ac36da1b84c8ff553eacabaef8c9ea803a5&")

    if message.author == client.user:
      return

    if message.content.lower() == "S Aula":
        await message.channel.send("https://cdn.discordapp.com/attachments/1221241667064037516/1221881341990277322/IMG-20240325-WA0053.jpg?ex=661430ad&is=6601bbad&hm=e7217555da4ae49563b344b7c21f9ac36da1b84c8ff553eacabaef8c9ea803a5&")
        await message.channel.send("se liga nas aula pae")


try:
  token = ("MTEyMzc1NjI0NjM5NTI1Njg1Mg.GvFLrC.s0nKCv5AD3DdJH7cTAjBH-RttcVoyBr2UZUlPg") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
