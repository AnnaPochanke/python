# The following list is given.

items = ['P-1', 'A-2', 'D-6', 'Z-8']

# Using the map() function, the lambda expression and replace() function, transform the given list in such a way as to get rid of the '-' character from each element.

# WRITE ONLY ONE LINE COMMAND, WITHOUT UNNECESSARY SPACES, WITHOUT ASSIGNING TO A VARIABLE, WITHOUT PRINT COMMAND.
# To enable a grader proper functioning use 'item' and 'items'.

# Expected result:
# ['P1', 'A2', 'D6', 'Z8']
items = list(map(lambda item: item.replace('-', ''), items))


print(items)
