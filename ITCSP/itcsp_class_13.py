# name = 'Anna'
# print(f'My name is {name} :)')
# var1 = 2
# var2 = 5
# print(f'var1 multiplied by var2 equals:{var1*var2}')
# age = 37
# print(f'My age is {age}')
# str = 'var1 multiplied by var2 equals:' + str(var1*var2)
# str = f'var1 multiplied by var2 equals: {var1*var2}'
# str = f'{var1} multiplied by {var2} equals: {var1*var2}'
# print(str)

########## FUNCTIONS ################
# def is_even(i):
#     return i % 2 == 0


# print(is_even(3))
# print(is_even.__doc__)

def is_even(i):
    return i % 2 == 0


# print(is_even(3))
# print(is_even.__doc__)
# print(str.strip.__doc__)

# def greet():
#     print('Hello')
#     print('How are you')


# # greet()

# number = 2
# result = is_even(number)
# print(result)
# greet()

# def send_greetings(name):
#     print(f'Hello {name}')


# send_greetings('Anna')

# def send_greetings(name: str) -> None:
#     print(f'Hello {name}')


# send_greetings('Jess')
# send_greetings('Bill')
# send_greetings('Ann')


def send_self_presentation(name, surname, birth_year, current_year):
    age = current_year - birth_year
    return f'Hello, my name is {name} {surname} and I am {age} years old.'


print(send_self_presentation('Jessica', 'Jones', 1998, 2023))
print(send_self_presentation('Anna', 'Pochanke', 1987, 2025))
print(send_self_presentation('Tosia', 'Sekula', 2008, 2025))
