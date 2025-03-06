# Exercise 14

# Write a program that prompts the user to enter a file name along with its extension
# (for example, "file01.docx" or "mybook.pdf").
# The program should check if the entered file name has a ".pdf" extension and display an appropriate message.

# Input: A string representing the file name (e.g., "Enter the file name: ").
# Output: A message indicating whether the file is of type pdf or not
# (e.g., "Your file is of type pdf." or "Your file is not of type pdf.").

# use:
# input()
# string slicing
# ternary operator

file_name = input("Enter the file name together with its extension: ")
# length = len(file_name)
# print(file_name[length-3:])
print("Your file is of type pdf") if file_name[-3:] == "pdf" else print(
    "Your file is not of type pdf")
