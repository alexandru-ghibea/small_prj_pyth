import random

while True:
    computer = random.choice(game_images)
    user_input = input("What do you choose? Rock, Paper or scissors.").lower()
    if user_input == "rock":
        user_input = rock
        if computer == rock:
            print("TIE GAME")
        elif computer == paper:
            print("Computer Wins")
        else:
            computer = scissors
            print("User wins")
    elif user_input == "paper":
        user_input = paper
        if computer == rock:
            print("User wins")
        elif computer == paper:
            print("TIE GAME")
        else:
            computer = scissors
            print("Computer wins")
    elif user_input == "scissors":
        user_input = scissors
        if computer == rock:
            print("Computer wins")
        elif computer == paper:
            print("User wins")
        else:
            computer = scissors
            print("TIE GAME")
    else:
        print("Please select: Rock,Paper or Scissors")
        user_input = input("What do you choose? Rock, Paper or scissors.").lower()
