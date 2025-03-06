# Exercise 16

# Write a program that prompts the user to enter a file name along with its extension (e.g., "document.txt").
# The program should extract and print out the file extension.
# If the entered file name does not contain an extension, the program should display an appropriate error message.

# Input: A string representing the file name (e.g., "Enter the file name: ").
# Output: The file extension or an error message if no extension is found
# (e.g., "The file extension is: txt." or "Error: No file extension found.").
# use:
# input()
# string slicing

# tests:
# file01.docx, myBook.pdf, file02.2s
# '''
# # enter a filename

# # find the index of "." which separates filename and it's extension

# # specify the index of the first character of your extension

# # write the conditional (if statement), using string slicing, substring your extension and print messages

# # for advanced -> use ternary operator
file_name = input("Enter the file name together with its extension: ")
extension_index = file_name.find(".")
extension = file_name[extension_index+1:]
print("The file extension is: " + extension) if file_name.find(
    ".") > 0 else print("Error: no file extension found")
