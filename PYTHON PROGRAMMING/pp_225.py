# Task: Introduction to Object-Oriented Programming

# Objective:
# Create a simple class to understand the basics of object-oriented programming, including defining a class, creating instances, and using methods and properties.

# Task Description:

# Define a class named Book with the following properties:

# title: a string representing the title of the book

# author: a string representing the author of the book

# year: an integer representing the year of publication

# Implement an __init__ method to initialize these properties when a new Book object is created.

# Add a method called get_description that returns a string in the format "Title: {title}, Author: {author}, Year: {year}".

# Create at least two instances of the Book class with different data and print their descriptions using the get_description method.

# Demonstrate how to access and modify the properties of one of the instances.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_description(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'


# Create instances of the Book class
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
# Print descriptions of the books
print(book1.get_description())
print(book2.get_description())
# Access and modify properties of book1
book1.year = 1950  # Changing the year of publication

print(f'Updated {book1.get_description()}')  # Print updated description
