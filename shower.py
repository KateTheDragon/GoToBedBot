import random

from formatting import formatMessage

goShowerMessages = [
  "{NAME} GO SHOWER",
  "{Name}! Go get clean!",
  "{Name} u stinky go shower"
  "{Name}, please clean yourself",
  "GO SHOWER",
  "Go shower!",
  "GO IN THE SHOWER",
  "Go in the shower!",
  "GO GET CLEAN",
  "Go get clean!",
  "Go to the shower, {Name}",
  "GO TAKE A SHOWER",
  "Go take a shower!",
  "Go shower stinky :P",
  "Perhaps consider a nice relaxing bath?",
  "Don't be a stinky {Name}, go take a shower."
]

def goShower(name):
  quote = formatMessage(random.choice(goShowerMessages), name)
  return quote