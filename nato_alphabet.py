import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for index, row in data.iterrows()}
print(new_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    word = input("Enter a word: ").upper()
    try:
        nato_phonetic = [new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, please provide only letters in the alphabet")
    else:
        print(nato_phonetic)
