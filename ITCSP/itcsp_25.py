# Exercise 25
# Your task is to swap the values of x and y and print them.
# Add between #...# the code needed

# INPUT: int
# x = 3
# y = 2
# OUTPUT: int
# x = 2 y = 3

# use temporary variable


while True:
    x = input("Input your x or type 'exit' to quit: ")
    if x.lower() == "exit":
        break
    y = input("Input your y or type 'exit' to quit: ")
    if y.lower() == "exit":
        break
    x = int(x)
    y = int(y)
    # ...#
    z = x
    x = y
    y = z
    # ...#
    print("Your new x is", x, "and your new y is", z)
