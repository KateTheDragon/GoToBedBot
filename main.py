import discord
import os

from keepAlive import keep_alive
from bed import goToBed
from eat import goEat
from go import goDoThings
import nicknames

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
     return

  msg = message.content
  author = str(message.author.id)

  if not msg.startswith('!'):
    return

  if msg.startswith('!bed'):
    quote = goToBed(getName(message, '!bed'))
    await message.channel.send(quote)
  
  if msg.startswith('!eat'):
    quote = goEat(getName(message, '!eat'))
    await message.channel.send(quote)
  
  if msg.startswith('!go'):
    quote = goDoThings(getName(message, '!go'))
    await message.channel.send(quote)

  if msg.startswith('!nickname'):
    nickname = msg.split('!nickname ', 1)[1]
    nicknames.addNickname(author, nickname)
    await message.channel.send("Added nickname "+nickname+" to "+message.author.display_name)
  
  if msg.startswith('!removeNickname'):
    nickname = msg.split('!removeNickname ', 1)[1]
    nicknames.removeNickname(author, nickname)
    await message.channel.send("Removed nickname "+nickname+" from "+message.author.display_name)
  
  if msg.startswith('!clearNicknames'):
    list = nicknames.clearNicknames(author)
    await message.channel.send("Cleared the following nicknames from "+message.author.display_name+": "+list)
  
  if msg.startswith('!showNicknames'):
    list = nicknames.showNicknames(author)
    await message.channel.send(message.author.display_name+" has the following nicknames: "+list)

def getName(message, start):
  if len(message.mentions) > 0:
    name = message.mentions[0].display_name
  else:
    name = message.author.display_name
  return name

keep_alive()
client.run(os.getenv('TOKEN'))