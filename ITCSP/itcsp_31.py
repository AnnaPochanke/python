# Exercise 31 (modify exercise 15)
# Write a program that counts vowels in a string
# The program should implement the possibility for the user to enter any word.

# INPUT: str
# OUTPUT: str

# DEFINE YOUR OWN FUNCTION:
#     count_vowels(text:str)->int
#     remember about docstring

# Details:
# use input() function to enter text
# invoke count_vowels function
# use f-string formatting together with print function

# vowels = 'aeiou'

# The exemplary input:
# Enter a word ...

# The exemplary output in  terminal should be:
# You have 6 vowels in the word "Appalachicola"
# Tests:
# VOWELS -> 2 vowels
# vowels -> 2 vowels
# Appalachicola -> 6 vowels

vowels = "aeiouy"
# vowelCount = 0


def count_vowels(text: str) -> int:
    return sum(1 for ch in text.lower() if ch in vowels)


while True:
    word = input("Enter a word:")
    if word.lower() == 'exit':
        break
    num_vowels = count_vowels(word)
    print(f'You have {num_vowels} vowels in the word "{word}".')
# count_vowels()
