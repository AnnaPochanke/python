# D = int(input( D = ) )
# print(f'{a} * {b} = {mult(a,b)}')

print(0/0)

#######
# print('TYPES OF EXCEPTIONS')
# t
# # 01, IndexError
# numbers = [1, 2, 3]
# print(numbers[3])
# print('Here I am')

# # 02, TypeError
# L = [1, 7, 4]
# print(int(L))

# # 03, TypeError
# print('a'/4)

# # 04, NameError
# print(a)

#######

# # 02, TypeError
# L = [1, 7, 4]
# print(int(L))

# # 03, TypeError
# print('a'/4)

# # 04, NameError
# print(a)

# # 05, ValueError
# num = int(input('Enter the integer numer: .. ')) # input a
# print(f'Our number is {num}')

# # 06, IOError-> FileNotFoundError
# file = open('ztest.py')
# print('File is opened')

#
# print('TYPES OF EXCEPTIONS')

# # 01, IndexError
# numbers = [1, 2, 3]
# print(numbers[3])
# print('Here I am')

# print('Here I am')

# # 02, TypeError
# L = [1, 7, 4]
# print(int(L))

# # 03, TypeError
# print('a'/4)

# # 04, NameError
# print(a)

# # 05, ValueError
num = int(input('Enter the integer numer: .. '))
print(f'Our number is {num}')

# # 06, IOError-> FileNotFoundError
# file = open('ztest.py')
# print('File is opened')
# file.close()

# # 07, FileNotFoundError, IndexError
# file = open('test.py')
# numbers = [1, 2, 3]
# print(numbers[3])

# input a

# print('HANDLING EXCEPTIONS')
#############################

# numbers = [1, 2, 3]
# print(numbers[3])
# print('Here I am not')

# # 01, handling IndexError
try:
numbers = [1, 2, 3] I
print(numbers[3])
print('Here I am not')
except IndexError:
print('Wrong Index !!! ')
print('Program continues')

# # # 05 how to handle it (ValueError) ?
# try:

num = int(input('Enter the integer numer: .. '))  # input a
print(f'Our number is: {num}')
# except ValueError:
print('You didn\'t enter the valid number!')
DEBUG CONSOLE

#

#

OUTPUT

TERMINAL

PORTS

the integer numer: ... a

# # ol, nandiing indextrror
# try:
#

numbers = [1, 2, 3]
print(numbers[3])
print('Here I am not')
# except IndexError:
print('Wrong Index !!! ')
# print('Program continues')


# # # 05 how to handle it (ValueError) ?
try:
num = int(input('Enter the integer numer: .. '))  # input a
print(f'Our number is: {num}')
except ValueError:
print('You didn\'t enter the valid number!')

#

# # 05 how to handle it (ValueError) ? a, 1, 0
# try:
a = int(input('Enter the integer numer \'a\': _ '))
b = int(input('Enter the integer numer \'b\': .. '))
num = a / b
print(f'The result of division {a} / {b} = {num}')
# except ValueError:
print('You didn\'t enter the valid number!')

#

#
# # # 05 how to handle it (ValueError) ?
# try:
num = int(input('Enter the integer numer: .. '))
print(f'our number is: {num}')
# except ValueError:
print('You didn\'t enter the valid number!')

#

# input a

# # 05 how to handle it (ValueError) ? a, 1, 0
try:
a = int(input('Enter the integer numer \'a\': _ '))
b = int(input('Enter the integer numer \'b\': ..
num = a / b
print(f'The result of division {a} / {b} = {num}')
except ValueError:
print('You didn\'t enter the valid number!')

# # 05 how to handle it (ValueError, ZeroDivisionError) ? a, 1, 0
# try:
a = int(input('Enter the integer numer \'a\': ..
b = int(input('Enter the integer numer \'b\': _
num = a / b
print(f'The result of division {a} / {b} = {num}')
# except ValueError:
print('You didn\'t enter the valid number!')

#

#

##
#
#

if a < 0 or b <= 0:
# print("You didn't enter the valid number!")
raise ValueError("You didn't enter the valid number!")
return a/b

I
a = int(input('Enter the integer numer \'a\': ..
b = int(input('Enter the integer numer \'b\': _. "))
print(f'The result of division {a} / {b} = {divide(a,b)}')
except ValueError as error:
print(error)
except ZeroDivisionError:
print('You can\'t divide by 0!')
print("Program terminated")

try:

# def get_positive_int(prompt):
while True:
number = int(input(prompt))
if number < 0:
raise ValueError("Number should be greater than 0")
return number

#

#

#

# def get greater than o int(prompt):

#

#

IT number < 0:
raise ValueError("Number should be greater equall 0!")
return number
except ValueError as err:
print("Invalid number entered, please try again. " + str(err))

#

#

#

#

# try: I
# .... a .=. get_greater_than_0_int('Please.enter.the first.number.')
#. .... b .=. get_greater_than_0_int('Please.enter.the.second.number.')
print(f"Division a / b = {a/b}")
# except ZeroDivisionError:
print("Can't divide by 0")
# except:
print("Something wrong !!! ")
# else:
print("Code without exceptions.")
print(f"Multiplying a x b = {a*b}.")
# finally:
print("The try ... except block is finished. Always. Useful for cleaning up resources that are used in the try block")

# def get_positive_int(prompt):
while True:
except valuetrror as err:
print("Invalid number entered, please try again. " + str(err))

try:

a = get_greater_than_0_int('Please enter the first number ')
')

b = get_greater_than_0_int('Please enter the second number
print(f"Division a / b = {a/b}")
except ZeroDivisionError:
print("can't divide by 0")
except Exception as err:
print("Something wrong ! !! ")
else:
print("Code without exceptions.")
print(f"Multiplying a x b = {a*b}.")
finally:
print("The try ... except block is finished. Always. Useful for cleaning up resources that are used in the try block")

# def get_positive_int(prompt):
while True:
try:
number = int(input(prompt))
assert number > 0, "Number should be greater 0"
return numher

#

#

#
#

except ValueError as err:
print("Invalid number entered, please try again. " + str(err))

v try:
a = get_greater_than_0_int('Please enter the first number ')
b = get_greater_than_o_int('Please enter the second number
print(f"Division a / b = {a/b}")
v except ZeroDivisionError:
print("Can't divide by 0")
v except Exception as err:
print("Something wrong !!! " + str(err))
v else:
print("Code without exceptions.")
print(f"Multiplying a x b = {a*b}.")
v finally:
print("The try ... except block is finished. Always. Useful for cleaning up resources that are used in the try block")

# def get_positive_int(prompt):
while True:
try:
number = int(input(prompt))
assert number > 0, "Number should be greater 0"
return number

#

# # # #

#

#
num = None
print('You can\'t divide by 0 !')
# print('Program continues
# print(f'The result of division {a} / {b} = {num}' if num != None else '')

...

')

####
# COMMAND LINE

# sys.argv

# ## 01

L1 = sys.argv
print(L1)

# python pp_classes.py this
# python pp_classes.py this is my class

# # 01.1, text
# sentence = svs.argy[1l