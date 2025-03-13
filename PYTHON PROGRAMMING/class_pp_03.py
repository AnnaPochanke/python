# L1 = [5, 3, 6, 2, 7, 8]
# L1.sort()
# print(L1)


# L2 = sorted(L1, reverse=True)
# print(L1)
# print(L2)

L1 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Chocolate dark', 15),
    ('Chocolate white', 17),
    ('Cakes', 19)
]
# print(L1)
# L1.sort(reverse=True)  # alphabetically sorted
# print(L1)

# sorting on price


# def sort_product(item):
#     return item[1]


# # L1.sort(key=sort_product)
# L1.sort(key=sort_product, reverse=True)
# print(L1)

# anonynumous function doesn't have a name. We use it as a parameter in another function

# L1.sort(key=lambda item: item[1])
# print(L1)

# map function has two parameters: function and iterable. func is lambda expression or pointer to a function, which is applied to each element of the iterables

# transforming the list -> interested only in prices
# L2 = list(map(lambda item: item[1], L1))
# print(L2)

# prices = []
# for l in L1:
#     prices.append
# print


##########
# map with function
# def get_item_1(item):
#     return item[1]


# # transforming the list -> interested only in prices
# L2 = list(map(get_item_1, L1))
# print(L2)

# transforming the list -> interested only in prices
# L2 = list(map(lambda item: item[1], L1))
# print(L2)

# increasing the prices for 20%
# L2 = list(map(lambda item: item[1] * 1.2, L1))
# print(L2)
