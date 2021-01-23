from replit import db

def addNickname(user, nickname):
  if user in db.keys():
    list = db[user]
    list.append(nickname)
    db[user] = list
    print(user+", "+nickname+" added")
  else:
    db[user] = [nickname]
    print(user+", "+nickname+" started")
  print(db[user])

def removeNickname(user, nickname):
  if user in db.keys():
    if nickname in db[user]:
      list = db[user]
      list.remove(nickname)
      db[user] = list
      print(user+", "+nickname+" removed")
    else:
      print(user+", "+nickname+" not found")
    print(db[user])
  else:
    print(user+" not found")

def clearNicknames(user):
  list = []
  if user in db.keys():
    list = db[user].copy()
    print(user+", "+str(list)+" removed")
  db[user] = []
  return list

def getNicknames(user):
  list = []
  if user in db.keys():
    list = db[user]
    print(user+", "+str(list)+" shown")
  return list