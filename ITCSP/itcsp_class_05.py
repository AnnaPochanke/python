# In IDE we have to use print() statement to see the result
# print(type(3)) # integer
# a = 3.14
# print(type(a)) # float

############################################
# Conversion
# print(float(1))
# print(int(3.9))
# print(int(3.1))
# print(bool(1))

############################################
# Expressions
# x = 5
# print(x)
# x = x + 6
# print(x)
# x += 6
# print(x)

#############################################
# Operations
i = 5
j = 7
# print(i/j)
# print(i//j)
# print(i % j)
# print(type(6/3))

# i = 2**3*2+1
# print(i)

# i = 1+2**3*2
# print(i)

##############################################
# Boolean expressions
# Comparison operators

# print(i > j)
# print(i >= j)
# print(i < j)
# print(i <= j)
# print(i == j)
# print(i != j)

# Logical operators
# truth table

# print("and operator")
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# print("or operator")
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# print("negation operator")
# print(not True)
# print(not False)

# Logical expresions - Examples
# expression_01 = 2 > 1
# expression_02 = 5 > 6

# print(expression_01)
# print(expression_02)
# print(expression_01 and expression_02)
# print(expression_01 or expression_02)
# print(not expression_01)

meal = "sandwich"
money = 5
# since the precedence of and is higher than or
# McDonald's rule
# is_lunch_delivered = meal == "fruit" or meal == "sandwich" and money >= 2
is_lunch_delivered = (meal == "fruit" or meal == "sandwich") and money >= 2
print(is_lunch_delivered)
