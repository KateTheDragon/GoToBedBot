class Pronoun:
  def __init__(self, subject = "they", object = "them", possessiveAdjective = "their", possessiveNoun = "theirs", plural = True):
    self.Subject = subject
    self.Object = object
    self.PossessiveAdjective = possessiveAdjective
    self.PossessiveNoun = possessiveNoun
    self.plural = plural
  
  def __eq__(self, other):
    return self.subject == other.subject

def getPronouns(user):
  roles = []
  for role in user.roles:
    roles.append(role.name)
  pronouns = []
  if "he/him" in roles:
    pronouns.append(Pronoun("He", "Him", "His", "His"))
  if "she/her" in roles:
    pronouns.append(Pronoun("She","Her", "Her", "Hers"))
  if "they/them" in roles:
    pronouns.append(Pronoun("They", "Them", "Their", "Theirs"))
  if len(pronouns) == 0:
    pronouns.append(Pronoun("They", "Them", "Their", "Theirs"))
  return pronouns