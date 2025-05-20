# git checkout
# git log
# git switch main

# print("FILTERING DATA STRUCTURES")
# print("using filter function")

# filtering a simple collection
# L1 = [1, 2, 4, 2, 9, 11, 12]

# def filter_list(item):
# return item > 10

# # # # func parameter as a function object which means that you need to pass a function without calling it (without a pair of par
# filtered_list = list(filter(filter_list, L1))
# print(filtered_list)

# ###

# # filtering + lambda, recommended
# L1 = [
# ('Bread', 10),
# ('Butter', 20),
# ('Chocolate dark', 15),
# ('Chocolate white', 17),
# ('Cakes', 19)

# criteria = 15
# filtered_list = list(filter(lambda item: item[1] > criteria, L1))
# print(filtered_list)

# #
# #

# # # filtering + lambda, dictionary
# # L2 = [
# {'Name': 'Bread', 'Price': 10},
# {'Name': 'Butter', 'Price': 20},
# {'Name': 'Chocolate dark', 'Price': 15},
# {'Name': 'Chocolate white', 'Price': 17},
# {'Name': 'Cakes', 'Price': 19}

# # filtered_list = list(filter(lambda item: item['Price'] > 15, L2))
# # print(filtered_list)

# #

# # filtering + lambda, dictipnary
L2 = [
{'Name': 'Bread', 'Price': 10},
{'Name': 'Butter', 'Price': 20},
{'Name': 'Chocolate dark', 'Price': 15},
{'Name': 'Chocolate white', 'Price': 17},
{'Name': 'Cakes', 'Price': 19}

filtered_list= list(filter(lambda item: item['Price'] > 15, L2))
print(filtered_list)

]

words = ['data', 'science', 'machine', 'learning']
word_length = list(map(lambda item: len(item), words))
print(word_length)


word_length = list(map(lambda item: (item, len(item)), words))
print(word_length)

# print("LIST COMPREHENSION")
#

# words = ['data', 'science', 'machine', 'learning' ]
# word_length = [len(word) for word in words]
# print(word_length)

# word_length = [len(word) for word in words]
# print(word_length)

# word_length = list(map(lambda item: len(item), words))
# print(word_length)

# MORE COMPLEX DATA STRUCTURES

# list pf prices
L1 = [
('Bread', 10),
('Butter', 20),
('Chocolate dark', 15),
('Chocolate white', 17),
('Cakes', 19)

]

prices = [item[1] for item in L1]
print(prices)

# increase price for 20% for filtered items, but only if the price > 15 (firstly filtered later price is increased)

L1 = [
('Bread', 10),
('Butter', 20),
('chocolate dark', 15),
('chocolate white', 17),
('Cakes', 19)]

prices = [(item[0], item[1]*1.2) for item in L1 if item[1] > 15]
print(prices)

# DICTIONARY REVISITED
# (word length dictionary)# increase price for 20% for filtered items, but only if the price > 15 (firstly filtered later price is increased)

# DICTIONARY REVISITED
# (word length dictionary)

words = ['data', 'science', 'machine', 'learning']
word_length = {}
for word in words:
word_length[word] = len(word)
print(word_length)

# (shakespeare text length analyzer)
# work with 'chaining'

# shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field,
# shakespeare = shakespeare.replace(',', '').replace('.', "')
# words = shakespeare. split()
# word_length = {}
# for word in words:
word_length[word] = len(word)
# print(word length)

######

...

#

# (shakespeare text length analyzer)
# work with 'chaining'

shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field,
shakespeare = shakespeare.replace(',', '').replace('.', "')
words = shakespeare. split()
word_length = {}
for word in words:
word_length[word] = len(word)
print(word_length)

....

# print("DICTIONARY COMPREHENSION")
# # # (word: length dictionary)

shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches i
words = shakespeare.replace(',', '').replace('.', '').split()
word_legth = {word: len(word) for word in words}
print(word_legth)

##
# # so far in loop section we had lists
# # now let's try with dictionary
# # have to use items() method
# product_price_dic = {
Bread': 10,
'Butter': 20,
'Chocolate dark': 15,
'Chocolate white': 17,
'Cakes': 19

# items_view = product_price_dic.items()
# for i in items_view:
print(i)

# product_price_increased = {k: v*1.2 for k, v in product_price_dic.items()}

#

#

#

# 1

#