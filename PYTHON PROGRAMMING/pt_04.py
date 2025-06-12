# Programming Task 04c: TextIO Utility Class
# Objective
# Create a Python class called TextIO that allows users to read from and write to a text file.

# Requirements (Functionality)
# Implement a class TextIO with the following methods:

# 1. __init__(self, filename: str)
# Stores the filename as an instance attribute.

# 2. write_text(self, text: str)
# Opens the file in write mode ('w') and writes the given text.

# Closes the file after writing (with ... statement).

# 3. append_text(self, text: str)
# Opens the file in append mode ('a') and appends the given text.

# Closes the file after appending.

# 4. read_text(self) -> str
# Opens the file in read mode ('r') and returns its contents as a string.

# Closes the file after reading.

# Suggested Usage / Sample Scenario

# Create a TextIO object with a file name results.txt.

# Use write_text() to write a short paragraph to the file.

# Use append_text() to add an extra line at the end.

# Use read_text() to read and display the final content.

# Time Limit: 30 minutes

# Score: 15 points

# | Criteria                                            | Max Points |
# | --------------------------------------------------- | ---------- |
# | Correct class definition & `__init__()`             | 2          |
# | `write_text()` method works as intended             | 3          |
# | `append_text()` method works as intended            | 3          |
# | `read_text()` method works and returns full content | 3          |
# | Proper use of file context manager (`with`)         | 2          |
# | Demonstrates usage with a short test                | 2          |

# --> Remember to handle exceptions gracefully, such as file not found errors or exception issues.
# Use try-except blocks where appropriate to ensure the program does not crash unexpectedly.
# --> Remember to include comments and docstrings for clarity.

# '''
class TextIO:
    def __init__(self, filename: str):
        self.filename = filename

    def write_text(self, text: str):
        """Writes the given text to the file."""
        with open(self.filename, 'w') as file:
            file.write(text)

    def append_text(self, text: str):
        """Appends the given text to the file."""
        with open(self.filename, 'a') as file:
            file.write(text)

    def read_text(self) -> str:
        """Reads the contents of the file and returns it as a string."""
        with open(self.filename, 'r') as file:
            return file.read()


# Example usage
if __name__ == "__main__":
    text_io = TextIO("results.txt")

    text_io.write_text("This is a test.")
    text_io.append_text("\nThis is an appended line.")
    content = text_io.read_text()
    print("File content:")
    print(content)
