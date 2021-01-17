import discord
import os

from keepAlive import keep_alive
from bed import goToBed
from eat import goEat
from go import goDoThings

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
     return

  if message.content.startswith('!bed'):
    quote = goToBed()
    await message.channel.send(quote)
  
  if message.content.startswith('!eat'):
    quote = goEat()
    await message.channel.send(quote)
  
  if message.content.startswith('!go'):
    quote = goDoThings()
    await message.channel.send(quote)

keep_alive()
client.run(os.getenv('TOKEN'))