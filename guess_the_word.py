import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
    display.append("_")
print(display)
no_of_guesses = len(chosen_word) + 1
game_on = True
while game_on:
    print("Number of guesses remaining:", no_of_guesses)
    guess = input("Guess a letter: ").lower()
    index = 0
    for letter2 in chosen_word:
        if guess == letter2:
            display[index] = letter2
        index += 1
    no_of_guesses -= 1

    print(display)
    if no_of_guesses < 0:
        print("You loose.Word was:", chosen_word)
        game_on = False
        break
    if "".join(display) == chosen_word:
        print("You won. Word was:", chosen_word)
        game_on = False
