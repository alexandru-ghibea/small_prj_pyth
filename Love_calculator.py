"""
Program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for
the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2-digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

e.g.

name1 = "Angela Yu"

name2 = "Jack Bauer"

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

Example Input 1

name1 = "Kanye West"

name2 = "Kim Kardashian"

Example Output 1

Your score is 42, you are alright together.
"""

import collections


def love_calculator():
    print("Welcome to the love calculator ")
    name1 = input("What is your name?: ")
    name2 = input("what is their name? ")
    word1 = "True"
    word2 = "Love"
    output1 = []
    output2 = []
    combined = name1 + name2
    for letter in combined.lower():
        if letter in word1.lower():
            output1.append(letter)
    print(output1)
    print(collections.Counter(output1))
    love_score1 = sum(collections.Counter(output1).values())
    print("Total Love_score1: ", love_score1)
    for letter in combined.lower():
        if letter in word2.lower():
            output2.append(letter)
    print(collections.Counter(output2))
    love_score2 = sum(collections.Counter(output2).values())
    print("Total Love_score2: ", love_score2)
    total_love_score: object = eval(f"{love_score1}{love_score2}")
    print(total_love_score)
    if total_love_score < 10 or total_love_score > 90:
        print(f"Your score is {total_love_score}, you go together like coke and mentos.")
    elif total_love_score >= 40 <= 50:
        print(f"Your score is {total_love_score}, you are alright together.")
    else:
        print(f"Your score is {total_love_score}")


love_calculator()
