print("Welcome to the roller coaster !! ")
height = int(input("What is your height(in cm) ?: "))
if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age ?:"))
    if age < 12:
        bill = 5
        print("Child tickets are 5$")
    if age <= 18:
        bill = 7
        print("Adults tickets are 7$")
    else:
        bill = 12
        print('Youth tickets are 12$')
else:
    print("You cannot ride the roller coaster! ")
photo = input("Would you like to purchase a photo from the roller coaster? Yes or No ")
if photo == "Yes":
    bill +=3
    print(f"Your total bill is {bill}")

