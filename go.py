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
  "Don't make me come over there, {Name}",
  "GO {NAME} GO",
  "Hi welcome to {Server}, we'll be your substitute executive function for the evening",
  "Go do the thing, {Name}"
]

def goDoThings(name):
  quote = formatMessage(random.choice(goMessages), name)
  return quote