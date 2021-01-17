import random

from formatting import formatMessage

goMessages = [
  "BRENN GO",
  "BRENN GO DO THINGS",
  "Brennjamin K. Mooney will you please go now",
  "Brenn!!!",
  "Brenn!!! pls move",
  "Don't make me come over there and kick ur ass",
  "Don't make me come over there",
  "GO BRENN GO",
  "Hi welcome to Homo Hotel, we'll be your substitute executive function for the evening"
]

def goDoThings():
  quote = formatMessage(random.choice(goMessages))
  return quote