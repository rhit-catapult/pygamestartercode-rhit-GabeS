import random
print("Guess my word")

def update_display_word(guess, secret_word, display_word):
  result = ""
  for k in range(len(display_word)):
    if guess == secret_word[k]:
      result += guess
    else:
      result += display_word[k]
  return result

word = ["catapult", "funishment", "rose", "hulman", "gabe"]
secret_word = random.choice(word)
display_word = "*" * len(secret_word)
print(display_word)
guessed_letters = []

while True:
  print()
  guess = input("Guess a letter: ")
  if guess in guessed_letters:
    print("You already guessed that letter")
    continue
  guessed_letters.append(guess)
  display_word = update_display_word(guess, secret_word, display_word)
  print(f"guesses so far {guessed_letters}")
  print(f"word so far {display_word}")
  if display_word == secret_word:
    print("You guessed the word")
    break

