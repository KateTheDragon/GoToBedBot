import random

goMessages = [
  "Brennjamin K. Mooney will you please go now",
  "Brenn!!! pls move",
  "Brenn!!!",
  "***BRENN GO DO THINGS***",
  "Hi welcome to {server} we'll be your substitute executive function for the evening",
  "GO BRENN GO",
  "***BRENN GO***",
  "don't make me come over there and kick ur ass",
  "***DON'T MAKE ME COME OVER THERE***"
]

def goDoThings():
  quote = random.choice(goMessages)
  return quote