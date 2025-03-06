# Exercise 30 (modify exercise 25)
# Write a program that swaps the values of x and y and prints the result to the terminal.
# For this purpose create a function
# swap_two_values(x:int, y:int)->None.

# INPUT: int x, y
# OUTPUT:
# e.g., x = 2, y = 3

# use f-string, function, invoke the function with examplary data


# while True:
#     x = input("Input your x or type 'exit' to quit: ")
#     if x.lower() == "exit":
#         break
#     y = input("Input your y or type 'exit' to quit: ")
#     if y.lower() == "exit":
#         break
#     x = int(x)
#     y = int(y)
def swap_two_values(x: int, y: int) -> None:
    z = x
    x = y
    y = z
    # ...#
    print(f'Your new x is {x} and your new y is {z}')


swap_two_values(2, 8)
