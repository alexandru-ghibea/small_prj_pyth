print('\n'
      '*******************************************************************************\n'
      '          |                   |                  |                     |\n'
      ' _________|________________.=""_;=.______________|_____________________|_______\n'
      '|                   |  ,-"_,=""     `"=.|                  |\n'
      '|___________________|__"=._o`"-._        `"=.______________|___________________\n'
      '          |                `"=._o`"=._      _`"=._                     |\n'
      ' _________|_____________________:=._o "=._."_.-="\'"=.__________________|_______\n'
      '|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |\n'
      '|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". \'__|___________________\n'
      '          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |\n'
      ' _________|___________| ;`-.o`"=._; ." ` \'`."\` . "-._ /_______________|_______\n'
      '|                   | |o;    `"-.o`"=._``  \'` " ,__.--o;   |\n'
      '|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________\n'
      '____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____\n'
      '/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_\n'
      '____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____\n'
      '/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_\n'
      '____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____\n'
      '/______/______/______/______/______/______/______/______/______/______/_____ /\n'
      '*******************************************************************************\n')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
decision1 = input("Choose where you would like to move: Left or Right ?").lower()
while True:
    print("You've reached a lake. There's no way to go around it.")
    try:
        if decision1 == "left":
            decision2 = input("Do you want to SWIM or WAIT ? ").lower()
        else:
            print("Fall into a hole.")
        if decision2 == "wait":
            print("Three doors appears in front of you...")
            decision3 = input("Which door would you choose ? Red, BLue or Yellow? Choose carefully ! ").lower()
        else:
            print("Attacked by TROUT! .")
        if decision3 == "red":
            print("Burned by FIRE! GAME OVER")
        elif decision3 == "blue":
            print("Eaten by BEASTS! GAME OVER ")
        elif decision3 == "yellow":
            print("Hurray !!! You have found the treasure!")
        else:
            print("Game Over!")

    except NameError:
        print("Game Over")
    break
