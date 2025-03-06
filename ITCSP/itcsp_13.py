# Write a program that prompts the user to enter three positive integers: x, y, and z.
# The program should then calculate and print the least number among them.
# Use the input() function to receive input from the user and conditional statements to determine the smallest number.
# INPUT: int
# OUTPUT: int


x = int(input("Enter the positive integer number called x: "))
y = int(input("Enter the positive integer number called y: "))
z = int(input("Enter the positive integer number called z: "))

if x <= y and x <= z:
    print("The smallest number is " + str(x))
elif z <= y and z <= z:
    print("The smallest number is " + str(z))
elif y <= x and y <= z:
    print("The smallest number is " + str(y))
