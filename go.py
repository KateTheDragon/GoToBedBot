import random

from formatting import formatMessage

goMessages = [
  "{NAME} GO",
  "{NAME} GO DO THINGS",
  "{Name} K. Mooney will you please go now",
  "{Name}!!!",
  "{Name}!!! pls move",
  "Don't make me come over there and kick ur ass",
  "Don't make me come over there",
  "GO {NAME} GO",
  "Hi welcome to Homo Hotel, we'll be your substitute executive function for the evening"
]

def goDoThings(name):
  quote = formatMessage(random.choice(goMessages), name)
  return quote