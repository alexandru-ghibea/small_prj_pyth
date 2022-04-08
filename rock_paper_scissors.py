import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
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
            print("Tie Game")
    else:
        print("Please select: Rock,Paper,Scissors")
        user_input = input("What do you choose? Rock, Paper or scissors.").lower()
