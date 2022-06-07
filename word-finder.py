import random

list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "/", '"', ";", "[", "]", "-", "=", "_", "+", "{", "}", "\\", "|", "'", ":", "?", ".", ",", "`", "~", " "]
wordGoal = "1234"
wordSize = 4
word = ""
finished = False
attempts = 1

while True:
  for _ in range(wordSize):
      word = word + random.choice(list)
  print(word + "   " + str(attempts))
  if word == wordGoal:
      break
  attempts += 1
  word = ""
