'''
Exercise 190

Using RE shakespeare.txt find all the 5-characters length words

Think about the following Special Sequences
\b
\w
{}


'''
import re
import sys


def get_text(file_path: str, start_line: int) -> str:

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # Join lines starting from start_line to the end
            text = ''.join(lines[start_line - 1:])
        return text
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)  # Exit the program if the file is not found
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


def find_five_char_words(text: str) -> list[str]:
    '''
    Function finds all the 5-characters length words in the text

    Parameters:
        text: text to be analyzed
    Returns:
        list of 5-characters length words
    '''
    pattern = r'\b\w{5}\b'  # Matches exactly 5 word characters (letters, digits, or underscores)
    return re.findall(pattern, text)


def main():
    file_path = 'shakespeare.txt'  # Path to your text file
    start_line = 1  # Line number to start reading from

    # Get the text from the file
    text = get_text(file_path, start_line)

    # Find all 5-characters length words
    five_char_words = find_five_char_words(text)

    # Print the results
    print(f"Found {len(five_char_words)} five-character words:")
    for word in five_char_words:
        print(word)


if __name__ == "__main__":
    main()
