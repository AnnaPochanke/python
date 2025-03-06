# L1 = [1, 3, 2, 7, 5]
# L2 = ["Hello", "World", "Smile"]
# L3 = [[1, 2, 7, 3], "Warsaw", 5]
# L4 = [[1, 2, 7, 3], [14, 9, 15, 6]]
# L5 = []  # empty list
# print(L3)

# len(L1)
# i = 2
# L2[i-1]

first_list = [2, "cat", 5.0, True]
# print(first_list[0])
# print(first_list[1])
# print(first_list[2])
# print(first_list[3])
# print(len(first_list))
# print(first_list[i-1])


# Lists are mutable

# print('LISTS ARE MUTABLE')
# print(first_list)
# first_list[0] = 3
# print(first_list)

# print('STRINGS ARE IMMUTABLE')
# text = "Hello"
# print(text)
# print(id(text))
# print(hex(id(text)))
# # text[0] = "M"  # ERROR
# # text[5] = "!"  # ERROR


# text = "World"
# print(text)
# print(id(text))
# print(hex(id(text)))

# print("Iterating over the list ver 01")
L = [1, 2, 9, 5]
# for i in L:
#     print(i)

# L = [1, 2, 9, 5]
# for i in range(len(L)):
#     print(L[i])

# print(id(L))
# sum = 0
# for i in L:
#     sum = + i
# print(sum)

# for i in range(len(L)):
#     sum += L[i]
# print(sum)

# L = [1, 2, 9, 5]
# print(id(L))
L.append(9)
# print(id(L))
# print(hex(id(L)))
print(L)


# L1 = [2, 6, 3]
# L2 = [8, 7, 3]
# L3 = L1+L2

# L1.extend(L2)
# L1.extend([8, 7, 3])
# print(L1)
# print(L2)
# print(L3)


# L1.extend([8, 7, 3])
# print(L1)

# L = ['apple', 'banana', 'cherry', 'banana']
# L.remove('banana')
# print(L)
# L.remove('pineapple')


L.pop(1)
print(L)
# print(L.pop())
# print(L)

# L.pop(1)
# print(L)
# L.pop()
# print(L.pop(1))

# L.clear()
# print(L)
# del (L[1])
# print(L)

s1 = "Hello World!"
# L = list(s1)
# print(L)

# COPY A LIST
# L1 = L.copy()
# L[0] = "A"
# print(L)
# print(L1)

# split the string into a list
L = s1.split()
print(L)
