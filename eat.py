import random

goEatMessages = [
  "As your Mother, I would very much like you to ingest things that will keep you alive",
  "***BRENN GO EAT A FOOD***",
  "Brenn, please feed yourself",
  "Brenn, please put foods inside of your eat-hole",
  "GO EAT",
  "IT IS TIME FOR THE EATING OF HEALTHY FOODS",
  "***BRENN GO EAT SOMETHING DONT MAKE ME COME OVER THERE***"
]

def goEat():
  quote = random.choice(goEatMessages)
  return quote