# counter = 0
# while counter < 6:
#     print(counter)
#     counter += 1

# print('INFINITE LOOP')
# counter = 0
# while counter < 6: # in while loop you always need to initialize it
#     print(counter)


# x = range(5)
# print(x)


# for i in range(5): #no need to initialize "i" separately
#     print(i)

# for i in range(3, 7):
#     print(i)

# for i in range(3, 20, 2):
#     print(i)

# for i in range(3, 20, -2):
#     print(i)

# for i in range(20, 3, -2):
#     print(i)

# for i in "Appalachicola": # to get each character
#     print(i)

# mysum = 0
# for i in range(0, 21):
#     mysum += i
# print("The sum of numbers 0-20 is", mysum)

# i = 0
# mysum = 0
# while i <= 20:
#     mysum += i
#     i += 1
# print("The sum of numbers 0-20 is", mysum)


# while True:  # always true
#     text = input("Enter any text ...")

# while True:
#     text = input("Enter any text ...")
#     if text == 'exit':
#         break

# rows = 5

# for i in range(1, rows+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     print() #it creates a new row


# Counting vowels in a string
vowels = "aeiouy"
vowelCount = 0
word = input("Enter a word ...")

for letter in word:
    if letter.lower() in vowels:
        vowelCount += 1
print("You have", vowelCount, "vowels in a word", word)
