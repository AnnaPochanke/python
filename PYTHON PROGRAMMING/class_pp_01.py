# def add_profile(index, ix, iy, area):
#     print(
#         f'Adding profile {index} with moments of inertia Ix={ix} cm4, Iy={iy} cm4 and area {area} cm2')


# add_profile('MC014', 166.9, 23.6, 14.99)
# add_profile(index='MC014', ix=166.9, iy=23.6, area=14.99)
# add_profile('MC014', iy=23.6, ix=166.9, area=14.99)


# print('1_line', 'Hello', sep='', end=' ')
# print('2_line', 'World', sep='')
# print('1_line', 'Hello')
# print('1_line', 'World')

# # default arguments in function definition
# def add_item(item_name, quantity=1):
#    print(f' {quantity} units of {item_name} was added')

# add_item(' bread' )
# add_item(' apples', 2)

# def print_numbers(*numbers):
#     print(numbers)


# def print_numbers(*numbers):
#     for n in numbers:
#         print(n)


# print_numbers(1, 2, 3, 4, 5, 6, 7)


# def summarize(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n
#     return sum


# print(summarize(1, 2, 3, 4, 5, 6, 7))

# def show_user(**user: dict) -> None:
#     print(type(user))
#     print(user)


# show_user(id=1, name='John', age=25, surname='kowalski')

# def add_user(L: list, **user: dict) -> None:
#     L.append(user)


# add_user(L, id=1, name='John', age=25, surname='kowalski')
# add_user(L, id=2, name='Anna', age=30, surname='Nowak')
# add_user(L, id=3, name='Tom', age=35, surname='Smith')
# print(L)


# def add_user(**user: dict) -> None:
#     L.append(user)


# L = []

# add_user(id=1, name='John', age=25, surname='kowalski')
# add_user(id=2, name='Anna', age=30, surname='Nowak')
# add_user(id=3, name='Tom', age=35, surname='Smith')
# print(L)
message = 'a'  # global variable
# global variable is avaialble in local scope
# local variable is not available in global scope


# def my_func():
#     print(message)


# my_func()

# def my_func():
#     message = 'b'


# my_func()
# print(message)

# def my_func():
#     global message
#     message = 'b'


# my_func()
# print(message)

# num = 1

# def my_func():
#     num += 1 #ERROR, it is local, it can't be used before it's assigned

# my_func()
# print(num)


# num = 1

# def my_func():
#     global num
#     num += 1
# my_func()
# print(num)


# num = 1


# def my_func(num):
#     num += 1
#     return num


# num = my_func(num)
# print(num)

colors = ['red','green','blue']

var1, var2, var3 = colors
