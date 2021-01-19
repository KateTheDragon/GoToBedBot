import random

from formatting import formatMessage

goEatMessages = [
  "As your Mother, I would very much like you to ingest things that will keep you alive",
  "{NAME} GO EAT A FOOD",
  "{NAME} GO EAT SOMETHING DONT MAKE ME COME OVER THERE",
  "{Name}, please feed yourself",
  "{Name}, please put foods inside of your eat-hole",
  "GO EAT",
  "It is time for the eating of healthy foods"
]

def goEat(name):
  quote = formatMessage(random.choice(goEatMessages), name)
  return quote