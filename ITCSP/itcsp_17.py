# ex 17 no list, no slicing, only own iteration
# Exercise 17
# For any entered string, write a program that reverses the order of the letters and prints the result to the console.
# For example, if the input is 'Hello, world', the output should be 'dlrow ,olleH'.
# Typing 'exit' should break the loop and exit the program. Use the input() function.
# INPUT: str
# OUTPUT: str

# Use while & for loop, don't use [::-1]
# abcd
# dcba


while True:
    word = input("Enter a string...")
    length = len(word)
    x = 0
    y = length-1
    old_value = word[x]
    new_word = ""
    if word.lower() == 'exit':
        break
    for letter in word:
        new_value = word[y]
        new_word += new_value
        y -= 1
    print(new_word)
