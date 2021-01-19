import random

underline = ["", "__"]
italics = ["", "*"]
bold = ["", "**"]


def formatMessage(string, name):
  string = string.replace("{name}", name.lower())
  string = string.replace("{Name}", name)
  string = string.replace("{NAME}", name.upper())
  stringTemp = randomizeEmphasis(string.split("http")[0])
  if (len(string.split("http")) > 1):
    string = stringTemp + "http" + string.split("http")[1]
  else:
    string = stringTemp
  return string

def randomizeEmphasis(string):
  formattingString = random.choice(italics) + random.choice(bold) + random.choice(underline)
  string = formattingString + string + formattingString
  caps = random.randint(0, 2)
  if (caps == 0):
    string = string.upper()
  elif (caps == 1):
    string = string.lower()
  return string