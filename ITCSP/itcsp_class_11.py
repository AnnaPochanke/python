# s1 = "value1,value2,value3"
# L = s1.split(",")
# print(L)

# s = "Hello world"
# L = list(s)
# print(L)

# L = ['a', 'b', 'c', 'd']
# text = '*'.join(L)
# print(text)

# L = ["H", "e", "l", "l", "o"]
# text = ''.join(L)
# print(text)

L = [6, 5, 4, 10, 15, 2]
# L.sort()
# print(L)
# L.sort(reverse=True)
# print(L)
# L1 = sorted(L, reverse=True)
# print(L1)

# L.reverse() #only mutating
# print(L)

# L1 = [1, 2, 3, ['a', 'Jason', 'Brown'], 'c']
# print(L1[3][1])

# L1 = [1, 2, 3, 4]
# print(1 in L1)

# print(dir(list))
# help(list.append)
# help(list.reserve)
print(L.count(6))

# print(len(L))
# print(L1[1]) #single element
# print(L1[1:3])
# print(L1[1:2]) #list with single elements

########################################################

# TUPLES
# immutable, similar to strings
########################################################

# t1 = ()  # empty tuple
# t2 = (1, "two", 3.25)
# print(t2)
# t3 = ("one",)
# print(t3)
# t4 = ("one")
# print(t4)
# print(type(t4))

# t4 = t2+t3
# print(t4)

a = enumerate("Hello")
print(a)
