# Exercise 230 (file pp_230.py)

# Create a class (TextIO) responsible for reading text from a file and writing text to a file.

# Class data attributes:
# - filepath: str — the path to the file
# - start_line: int — the line number from which to start reading the file
# - _text: str — the text that was read from the file


# Implement the following class methods:
# - def __init__(self, filepath, startline=0):
# - def get_text(self) -> str:
# - def read_from_file(self) -> None:
# - def write_to_file(self, text: str, f_path: str, mode: str = 'w') -> None:

# Exception handling should be implemented.

# Use the input() function to enter the file path and the start line number.

# For testing purposes, use the "shakespeare.txt" file to read text from it, starting from the specified line number (247).

# Create a clas TextAnalyzer
# Class data attributes:
# - _text: str — the text to analyze
# - _sorted_list_of_words = []

# Class methods:
# - def __init__(self, text: str):
# - def get_text(self) -> str:
# - def get_sorted_list_of_words(self, number_of_words: int) -> list   (10 most frequent words in the text, with it's frequency, should be written to a file)
# - def set_sorted_list_of_words(self) -> None: (word: frequency) )

import re
from collections import Counter


class TextIO:
    def __init__(self, filepath: str, start_line: int = 0):
        self.filepath = filepath
        self.start_line = start_line
        self._text = ""

    def get_text(self) -> str:
        return self._text

    def read_from_file(self) -> None:
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                self._text = ''.join(lines[self.start_line:])
        except FileNotFoundError:
            print(f"Error: File '{self.filepath}' not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

    def write_to_file(self, text: str, f_path: str, mode: str = 'w') -> None:
        try:
            with open(f_path, mode, encoding='utf-8') as file:
                file.write(text)
        except Exception as e:
            print(f"An error occurred while writing to file: {e}")


class TextAnalyzer:
    def __init__(self, text: str):
        self._text = text
        self._sorted_list_of_words = []

    def get_text(self) -> str:
        return self._text

    def set_sorted_list_of_words(self) -> None:
        words = re.findall(r'\b\w+\b', self._text.lower())
        freq = Counter(words)
        self._sorted_list_of_words = freq.most_common()

    def get_sorted_list_of_words(self, number_of_words: int) -> list:
        if not self._sorted_list_of_words:
            self.set_sorted_list_of_words()
        return self._sorted_list_of_words[:number_of_words]


# --- Example usage ---

if __name__ == "__main__":
    # User input
    filepath = input("Enter file path: ")
    try:
        start_line = int(input("Enter start line number: "))
    except ValueError:
        print("Invalid line number. Defaulting to 0.")
        start_line = 0

    # Read file
    reader = TextIO(filepath, start_line)
    reader.read_from_file()
    text = reader.get_text()

    # Analyze text
    analyzer = TextAnalyzer(text)
    top_words = analyzer.get_sorted_list_of_words(10)

    # Format results
    output_text = '\n'.join([f"{word}: {count}" for word, count in top_words])
    print("Top 10 words:\n", output_text)

    # Save results
    reader.write_to_file(output_text, "top_10_words.txt")
