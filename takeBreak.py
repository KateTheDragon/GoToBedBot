import random

from formatting import formatMessage

takeABreakMessages = [
  "{Name}!!! Rest is important!!!",
  "{Name}! Take a break!",
  "{NAME} TAKE BREAK",
  "TAKE BREAK {NAME}",
  "Take a break, {Name}",
  "Time to rest for a bit, {Name}",
  "{Name}, it is time for a rest",
  "Rest now, {Name}. Your work will still be there later.",
  "Ok, {Name}, it's time for a brain break!",
  "Rest is important!!!",
  "TAKE BREAK",
  "Take a break!",
  "Time to rest for a bit",
  "It is time for a rest",
  "Listen, {Name} brain. {Their} work is important, but {they} cannot work without rest. {They} can take a little break and then return to work refreshed and ready."
]

def takeABreak(name):
  quote = formatMessage(random.choice(takeABreakMessages), name)
  return quote