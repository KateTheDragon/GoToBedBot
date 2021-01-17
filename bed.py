import random

from formatting import formatMessage

goToBedMessages = [
  "BRENN BRAIN. LET MY SON SLEEP. He needs to sleep!! He deserves comfort and rest. He has earned it, and you need to let him have it",
  "BRENN GO SLEEP",
  "Brenn! Go to bed!",
  "GO BED",
  "Go bed!",
  "GO IN THE BED",
  "Go in the bed!",
  "GO SLEEP",
  "Go sleep!"
  "GO TO BED",
  "Go to bed!",
  "GO TO SLEEP",
  "Go to sleep!"
  "Goodnight fucker",
  "https://cdn.discordapp.com/attachments/687387583768166486/793307047264518154/t9wj0wukeby01.jpg",
  "It is the sleepy time, it is the time for the sleep https://www.youtube.com/watch?v=OKdzW6gUn10",
  "Son, please sleep"
]

def goToBed():
  quote = random.choice(goToBedMessages)
  quoteTemp = formatMessage(quote.split("http")[0])
  if (len(quote.split("http")) > 1):
    quote = quoteTemp + "http" + quote.split("http")[1]
  else:
    quote = quoteTemp
  return quote