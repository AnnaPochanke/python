# Exercise 21
# For any entered string. Write a program that will reverse the order of the letters and print to the console.
# e.g., for "Hello world", printed result should be 'dlrow olleH
# Typing in an "exit" should break the loop end exit the program
# INPUT: str
# OUTPUT: str

# Use while loop, input(), use methods reverse(), join()


while True:
    text = input("Enter any string: ...")
    if text.lower() == "exit":
        break
    L = list(text)
    L.reverse()
    text = ''.join(L)
    print(text)
