import random

from formatting import formatMessage

goDoHomeworkMessages = [
  "{NAME} BRAIN. IT IS TIME TO WORK!",
  "{NAME} GO DO HOMEWORK",
  "{Name}! Go do your homework!",
  "{Name} it is time for the homework"
  "{Name}, please do your homework",
  "GO DO HOMEWORK",
  "Go do your homework!"
  "Go work!",
  "GO WORK",
  "It's time to do your homework, {Name}.",
  "Try doing just a little bit of homework, then you can take a break.",
  "Dear {Name} brain, I know homework is dumb and hard and boring but {Name} is in school for a reason. {They} have goals and aspirations and in order to reach them, {they} must graduate, and in order to graduate {they} must pass this class, and in order to pass this class {they} must do {their} homework. So please settle in and do the thing.",
  "I believe in you! You can do this homework and pass this class and make your dreams come true!",
  "https://www.tiktok.com/@hankgreen1/video/6915591031358508289"
]

def goDoHomework(name):
  quote = formatMessage(random.choice(goDoHomeworkMessages), name)
  return quote