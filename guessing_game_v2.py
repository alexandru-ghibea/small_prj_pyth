import random
easy_level = 5
hard_level = 10


def select_level():
    answer = ["easy", "hard"]
    choice = input("Select level: easy or hard\n ")
    while choice not in answer:
        choice = (input("Sorry, please select  easy or hard :\n"))
    if choice == "easy":
        return easy_level
    else:
        return hard_level


def check_answer(turns, guess, secret_number):
    if guess > secret_number:
        print("To high. Guess again")
        return turns - 1
    elif guess < secret_number:
        print("To low. Guess again.")
        return turns - 1
    else:
        print(f"You win, answer was {secret_number}")


def game_on():
    print("Welcome to the Guessing Game!")
    print("I am think on a number between 1 and 100")
    turns = select_level()
    secret_number = random.randint(1, 100)
    guess = 0
    while guess != secret_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(turns, guess, secret_number)
        if turns == 0:
            print(f"You've run out of guesses, you lose. Number was {secret_number}")
            return
        elif guess != secret_number:
            print("Guess again.")


game_on()
