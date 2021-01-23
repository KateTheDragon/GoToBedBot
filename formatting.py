import random
from nicknames import getNicknames

underline = ["", "__"]
italics = ["", "*"]
bold = ["", "**"]


def formatMessage(string, user):
  while ("{name}" in string):
    string = string.replace("{name}", chooseNickname(user).lower(), 1)
  while ("{Name}" in string):
    string = string.replace("{Name}", chooseNickname(user), 1)
  while ("{NAME}" in string):
    string = string.replace("{NAME}", chooseNickname(user).upper(), 1)
  
  stringTemp = randomizeEmphasis(string.split("http")[0])
  if (len(string.split("http")) > 1):
    string = stringTemp + " http" + string.split("http")[1]
  else:
    string = stringTemp
  return string

def randomizeEmphasis(string):
  italicsString = random.choice(italics)
  boldString = random.choice(bold)
  underlineString = random.choice(underline)
  string = underlineString + boldString + italicsString + string + italicsString + boldString + underlineString
  caps = random.randint(0, 2)
  if (caps == 0):
    string = string.upper()
  elif (caps == 1):
    string = string.lower()
  return string

def chooseNickname(user):
  list = getNicknames(str(user.id))
  list.append(user.display_name)
  return random.choice(list)