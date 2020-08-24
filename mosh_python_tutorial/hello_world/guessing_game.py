guess = -1
secret = 9
attempts = 0

while guess != secret and attempts < 3:
  guess = int(input("Guess: "))
  attempts += 1

if guess == secret:
  print("You win!")
else:
  print("You loose.")