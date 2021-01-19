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

  if not message.content.startswith('!'):
    return

  if message.content.startswith('!bed'):
    quote = goToBed(getName(message, '!bed'))
    await message.channel.send(quote)
  
  if message.content.startswith('!eat'):
    quote = goEat(getName(message, '!eat'))
    await message.channel.send(quote)
  
  if message.content.startswith('!go'):
    quote = goDoThings(getName(message, '!go'))
    await message.channel.send(quote)

def getName(message, start):
  if len(message.mentions) > 0:
    name = message.mentions[0].display_name
  else:
    name = message.author.display_name
  return name

keep_alive()
client.run(os.getenv('TOKEN'))