import random

from formatting import formatMessage

goToBedMessages = [
  "{NAME} BRAIN. LET MY {NAME} SLEEP. {They} {need/needs} to sleep!! {They} {deserve/deserves} comfort and rest. {They} {have/has} earned it, and you need to let {them} have it",
  "{NAME} GO SLEEP",
  "{Name}! Go to bed!",
  "{Name} it is time for the sleeping"
  "{Name}, please sleep",
  "GO BED",
  "Go bed!",
  "GO IN THE BED",
  "Go in the bed!",
  "GO SLEEP",
  "Go sleep!",
  "GO TO BED",
  "Go to bed!",
  "GO TO SLEEP",
  "Go to sleep!",
  "Go to the bed, {Name}",
  "Goodnight {Name}",
  "https://cdn.discordapp.com/attachments/687387583768166486/793307047264518154/t9wj0wukeby01.jpg",
  "It is the sleepy time, it is the time for the sleep https://www.youtube.com/watch?v=OKdzW6gUn10"
]

def goToBed(name):
  quote = formatMessage(random.choice(goToBedMessages), name)
  return quote