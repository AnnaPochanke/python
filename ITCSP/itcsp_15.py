#
# Exercise 15
# Write a program that counts the vowels in a string.
# The program should allow the user to enter a word using the input() function.

# INPUT: str
# OUTPUT: str

# Use input() function
# vowels = 'aeiou'

# The exemplary input:
# Enter a word ...

# The exemplary output in  terminal should be:
# You have 6 vowels in a word "Appalachicola"
# Tests:
# VOWELS -> 2 vowels
# vowels -> 2 vowels
# Appalachicola -> 6 vowels


# Counting vowels in a string
vowels = "aeiouy"
# vowelCount = 0


while True:
    vowelCount = 0
    word = input("Enter a word ...")
    if word.lower() == 'exit':
        break
    for letter in word:
        if letter.lower() in vowels:
            vowelCount += 1
    print("You have", vowelCount, "vowels in a word", word)
