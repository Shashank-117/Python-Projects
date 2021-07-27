
import pandas

#TODO 1. Create a dictionary in this format:
df = pandas.read_csv('nato_phonetic_alphabet.csv')
call_signs = {row.letter: row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input('Enter Word: ')
name = name.upper()
result = [call_signs[n] for n in name]
print(result)