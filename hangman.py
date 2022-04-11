import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print("Welcome to hangman game!")
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
lives = 6
game_on = True
for letter in chosen_word:
    display.append("_")
print(display)

print(f"You have {lives} lives.")

while game_on:
    guess = input("Guess a letter: ").lower()
    index = 0
    for letter2 in chosen_word:
        if guess == letter2:
            display[index] = letter2
        index += 1
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess. Number of lives remaining {lives}")
    if lives == 0:
        game_on = False
        print("You loose.Word was:", chosen_word)
    if "".join(display) == chosen_word:
        print("You won. Word was:", chosen_word)
        game_on = False
    print(stages[lives])

