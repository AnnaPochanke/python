
# ### **Task Description**
# This task is similar to **Exercise 40**, where you need to find the longest word in a given text. However, in this exercise, you must also implement a function called `get_text()`.

# The new function should read and return the text from a file.

# ### **Requirements**
# 1. Write a program with a function called `map_longest()`, which takes a text as a parameter and returns a **tuple** containing:
#    - The longest word in the text
#    - Its length

# 2. The program should produce an output message, for example:
#    - **After punctuation removal:**
#      `"The longest word in the file 'shakespeare.txt' is 'internethartvmdcsouiucedu' with a length of 25 characters."`  shakespeare.txt is in my working directory.
#    - **Without punctuation removal:**
#      `"The longest word in the file 'shakespeare.txt' is '>internet:hart@.vmd.cso.uiuc.edu' with a length of 32 characters."`

# 3. Use the `map()` function together with lambda expressions.
# 4. Implement **exception handling** to manage potential errors.

import string


def get_text(filename):
    """Reads and returns the content of a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""
    except IOError as e:
        print(f"IOError while reading the file: {e}")
        return ""


def map_longest(text):
    """Finds the longest word in the given text using map() and lambda."""
    words = text.split()
    word_lengths = list(map(lambda w: (w, len(w)), words))
    return max(word_lengths, key=lambda t: t[1]) if word_lengths else ("", 0)


if __name__ == "__main__":
    filename = 'shakespeare.txt'
    text = get_text(filename)

    if text:
        # Without punctuation removal
        word, length = map_longest(text)
        print(
            f"Without punctuation removal:\nThe longest word in the file '{filename}' is '{word}' with a length of {length} characters.\n")

        # With punctuation removal
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = text.translate(translator)
        word_clean, length_clean = map_longest(cleaned_text)
        print(
            f"After punctuation removal:\nThe longest word in the file '{filename}' is '{word_clean}' with a length of {length_clean} characters.")
