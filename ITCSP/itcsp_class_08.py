# isinstance function
# number = 5
# if isinstance(number, str):
#     print("Yes")
# else:
#     print("No")

# # ternary operator
# a, b = 11, 15
# min = a if a < b else b
# print(min)

# number = 5
# print("yes") if isinstance(number, int) else print("no")

# print("hat" == "hat")
# print("Hat" == "hat")
# print("HAT" > "hat")
# print("T" > "t")
# print("c" > "C")

##################################################
# import string
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.ascii_letters)
# print(string.hexdigits)
# print(string.whitespace) #useful in text processing
# print(string.punctuation)


# print(ord('H'))
# print(ord('h'))
# print(ord('c'))
# print(ord('ł'))
# print(bin(ord("ł")))

# print(ord("l"))

# upper and lower function

# s = "Hi there"
# print(s.lower())
# print(s)
# s2 = s.lower()
# print(s2)

# s = "Hi there"
# print(s.upper())
# print(s)
# s2 = s.upper()
# print(s2)


# capitalize method
# s = "Hi there"
# print(s.capitalize())

# # title method
# print(s.title())

# lstrip(character)

# s = "ssnsssssshello"
# print(s.lstrip("sn"))

# find(value)
s = "he lives in Poznan"
# print(s.find("i"))
# print(s.find("b"))
# print(s.index("i"))

# replace(old_value,new_value,count)
# print(s.replace("i", "B"))
# print(s.replace("i", "B", 1)) #only first occurence will be replaced
# print(s.replace("i", ""))  # removing all instances of "i"
print(s.replace(" ", ""))  # removing all spaces
