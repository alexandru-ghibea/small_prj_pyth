import random


def deal_card():
    """
    Create a deal_card() function that uses the List below to *return* a random card.
    #11 is the Ace.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    Create a function called calculate_score() that takes a List of cards as input
    #and returns the score
    1.Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score.
    0 will represent a blackjack in our game
    """
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    """
    Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace
    it with a 1
    """
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_scores(user_score, computer_score):
    """
    Create a function called compare() and pass in the user_score and computer_score.
    If the computer and user both have the same score, then it's a draw.
    If the computer has a blackjack (0), then the user loses.
    If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses.
    If the computer_score is over 21, then the computer loses.
    If none of the above, then the player with the highest score wins.
    """
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    user_hand = []
    computer_hand = []
    game_on = True
    for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())
    while game_on:
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)
        print(f"   Your cards: {user_hand}, current score: {user_score}")
        print(f"   Computer's first card: {computer_hand[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_on = False
        else:
            choice = input("Do you want to draw another card? Y or N: ").lower()
            if choice == "y":
                user_hand.append(deal_card())
            if choice == "n":
                game_on = False
    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)
    print(f"   Your final hand: {user_hand}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()

