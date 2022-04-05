"""
Write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
"""
import random
choice = random.randint(0, 1)
print(choice)

if choice == 0:
    print("Heads")
else:
    print("Tails")
