import random
from nicknames import getNicknames
from pronouns import getPronouns

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

  string = string.replace("{Server}", user.guild.name)

  pronoun = random.choice(getPronouns(user))

  string = string.replace("{they}", pronoun.Subject.lower())
  string = string.replace("{They}", pronoun.Subject)
  string = string.replace("{THEY}", pronoun.Subject.upper())

  string = string.replace("{them}", pronoun.Object.lower())
  string = string.replace("{Them}", pronoun.Object)
  string = string.replace("{THEM}", pronoun.Object.upper())

  string = string.replace("{their}", pronoun.PossessiveAdjective.lower())
  string = string.replace("{Their}", pronoun.PossessiveAdjective)
  string = string.replace("{THEIR}", pronoun.PossessiveAdjective.upper())

  string = string.replace("{theirs}", pronoun.PossessiveNoun.lower())
  string = string.replace("{Theirs}", pronoun.PossessiveNoun)
  string = string.replace("{THEIRS}", pronoun.PossessiveNoun.upper())
  
  while "{" in string:
    firstPart = string.split("{", 1)[0]
    string = string.split("{", 1)[1]
    midPart = string.split("}", 1)[0]
    lastPart = string.split("}", 1)[1]
    if pronoun.plural:
      midPart = midPart.split("/")[0]
    else:
      midPart = midPart.split("/")[1]
    string = firstPart + midPart + lastPart

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