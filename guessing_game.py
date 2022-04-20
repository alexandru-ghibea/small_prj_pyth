import random
print("Welcome to the guessing game")
print("I am thinking of a number between 1 and 100")
secret_number = random.choice(list(range(1, 101)))
game_on = True

while game_on:
    answer = ["easy", "hard"]
    choice = input("Select the level: easy or hard \n")
    while choice not in answer:
        choice = input("Sorry, please select  easy or hard: ")
    if choice == "easy":
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess:"))
        while guess:
            if guess > secret_number:
                attempts -= 1
                print("To high, guess again!")
                print(f'You have {attempts} remaining to guess the number.')
                guess = int(input("Make a guess:"))
            elif guess < secret_number:
                attempts -=1
                print("To low, guess again")
                print(f'You have {attempts} remaining to guess the number.')
                guess = int(input("Make a guess:"))
            elif guess == secret_number:
                print("You win")
                break
    else:
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess:"))
        while guess:
            if guess > secret_number:
                attempts -= 1
                print("To high, guess again!")
                print(f'You have {attempts} remaining to guess the number.')
                guess = int(input("Make a guess:"))
            elif guess < secret_number:
                attempts -= 1
                print("To low, guess again")
                print(f'You have {attempts} remaining to guess the number.')
                guess = int(input("Make a guess:"))
            elif guess == secret_number:
                print("You win")
                break

