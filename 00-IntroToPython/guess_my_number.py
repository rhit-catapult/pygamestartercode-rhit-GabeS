import random
print("Guess My Number")
print("I'm thinking of a number between 1 and 100")
print("Try to guess it in as few attempts as possible")

secret_number = random.randint(1, 100)
attempts = 0

play = True

while True:
  attempts += 1
  guess = int(input("Take a guess: "))
  if guess < secret_number:
    print("You guessed too low guess higher")
  elif guess > secret_number:
    print("You guessed too high guess lower")
  else:
    print(f"You guessed the number which was {secret_number}")
    print(f"It took you {attempts} attempts to guess the number")
    break