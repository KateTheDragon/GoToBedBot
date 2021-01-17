import random

from formatting import formatMessage

goEatMessages = [
  "As your Mother, I would very much like you to ingest things that will keep you alive",
  "BRENN GO EAT A FOOD",
  "BRENN GO EAT SOMETHING DONT MAKE ME COME OVER THERE",
  "Brenn, please feed yourself",
  "Brenn, please put foods inside of your eat-hole",
  "GO EAT",
  "It is time for the eating of healthy foods"
]

def goEat():
  quote = formatMessage(random.choice(goEatMessages))
  return quote