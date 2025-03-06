# Exercise 22
# Write a program, which removes all 'banana' elements from the list and print the new list to the terminal
L = ['banana', 'pineapple', 'orange', 'banana',
     'banana', 'apple', 'strawberry', 'mango', 'figs']

# use iteration, range() function and count() method
number = L.count('banana')
for fruit in range(number):
    L.remove('banana')
print(L)
