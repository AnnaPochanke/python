####

# # so far in loop section we nad lists
# # now let's try with dictionary
# # have to use items() method
product_price_dic = {
Bread': 10,
Butter': 20,
'Chocolate dark': 15,
Chocolate white': 17,
'Cakes': 19

items_view = product_price_dic.items()
for i in items_view:
print(i)

product_price_increased = {k: v*1.2 for k, v in product_price_dic.items()}

print(product_price_increased)I

# SORTING DICTIONARIES ON VALUE
# If we want to get a sorted copy of the entire dictionary, we need to use the dictionary items() method
# which pass in the entire dictionary as the iterable to the sorted() function:
##

# shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field,
# words = shakespeare.replace(',', '').replace('.','').split()
{word: len(word) for word in words}
# word length = 1W

# print(product_price_increased)

# SORTING DICTIONARIES ON VALUE
# If we want to get a sorted copy of the entire dictionary, we need to use the dictionary items() method
# which pass in the entire dictionary as the iterable to the sorted() function:
##

shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field, .... '
words = shakespeare.replace(',', '').replace('.','').split()
word_length = {word: len(word) for word in words}
sorted_word_length = sorted(
word_length.items(), key=lambda item: item[1], reverse=True)
print(sorted_word_length)
# print(dict(sorted_word_length))

#

##
# print("TERNARY OPERATOR")
###
# var_1 = statement_if_true if condition else statement_if_false
# a, b = 11, 15
# # # 1 scenario
# if a < b:
min = a
# a, b = 11, 15
# min = a+b if a < b else a-b
# print(min)

# print("pass statement")
##
for i in range(1, 5):
pass

# a, b = 11, 15
# if a < b:
#
# print(a)

##
# escape characters

#

pass

#

# \'

# \n
# \t
# 11

# s = 'Hey, what's up?'
# 5 = 'Hey, what\'s up?'

# s = "His name is "John""
# s = "His name is \"John\""

# s = "His name is 'John'"

# print(s)

# ###
# print("Multiline strings\ncan be created\nusing escape sequences.")

# #####
print("C:\Users\Robert\Desktop") # ERROR
# print("C:\\Users\\Robert\\Desktop")
# print(r"C:\Users\Robert\Desktop")

#
# print("ITERABLES - SUMMARY")
#
# # # 1. range

#####

# print(iter(L1)) # it means works with loops
# print(dir(L1)) # see all methods
# for x in ['a', 1, 2, 'b']:
print(x)

# # 4. tuples
# for x in ('c', 1, 2, 'd'):
print(x)

# # # 5. dictionary
dic = {'a': 1, 'b': 2, 'c': 3}
# print(iter(dic))
# print(dir(dic))
# for x in dic:
print(x)
# over keys()
# for x in dic.keys():
print(x)
# # # over values()
o add a breakpoint . values () :
print(x)
# # # over items() -- > view object
for x in dic.items():
print(x)

# # unnacking iterable

#
# # #

#
# # #

#

#