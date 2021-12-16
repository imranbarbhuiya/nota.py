import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nota_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Enter a word: ").upper()

nota_list = [nota_dict[letter] for letter in user_input]

print(nota_list)
