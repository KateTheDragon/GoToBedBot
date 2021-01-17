import random

underline = ["", "__"]
italics = ["", "*"]
bold = ["", "**"]


def formatMessage(string):
  formattingString = random.choice(underline) + random.choice(italics) + random.choice(bold)
  string = formattingString + string + formattingString
  caps = random.randint(0, 2)
  if (caps == 0):
    string = string.upper()
  elif (caps == 1):
    string = string.lower()
  return string