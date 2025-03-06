# Exercise 12
# Write a program that prompts the user to enter an integer, called x.
# If x is divisible by 2 and 3, print "divisible by 2 and 3."
# If x is divisible by 2 but not by 3, print "divisible by 2 and not by 3."
# If x is divisible by 3 but not by 2, print "divisible by 3 and not by 2."
# If x is not divisible by 2 or 3, print "not divisible by 2 or 3."
# Use modulo division to perform the necessary checks.

x = int(input("Enter the integer number "))

if x % 2 == 0 and x % 3 == 0:
    print("divisible by 2 and 3.")
elif x % 2 == 0 and x % 3 != 0:
    print("divisible by 2 and not by 3.")
elif x % 2 != 0 and x % 3 == 0:
    print("divisible by 3 and not by 2.")
else:
    print("not divisible by 2 or 3")
