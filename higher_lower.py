import random
from accounts import data


def account_a():
    first_choice = random.choice(data)
    for k, v in first_choice.items():
        if k == "follower_count":
            return v
        else:
            print("Compare A: " + first_choice["name"] + " a " + first_choice["description"] + " from " + first_choice["country"])


def account_b():
    second_choice = random.choice(data)
    for h, v in second_choice.items():
        if h == "follower_count":
            return v
        else:
            print("Against B: " + second_choice["name"] + " a " + second_choice["description"] + " from " + second_choice["country"])


def replay():
    answer = ["Y", "N"]
    choice = input("Do you want to play again Y or N: ")
    while choice not in answer:
        choice = input("Sorry, please select  Y or N: ")
    if choice == "Y":
        return True
    else:
        return False


def game():
    score = 0
    while True:
        A = account_a()
        B = account_b()
        answer = ['a','b']
        choice = input("Who has more followers? Type A or B ").lower()
        while choice not in answer:
            choice = input("Sorry,Type A or B ").lower()
        if choice == "a":
            if A > B:
                score += 1
                print(f'Current score is  {score}')
            else:
                print(f'Sorry, that was wrong. Final score : {score}')
                break
        elif choice == "b":
            if B > A:
                score += 1
                print(f'Current score is  {score}')
            else:
                print(f'Sorry, that was wrong. Final score : {score}')
                break


game()

