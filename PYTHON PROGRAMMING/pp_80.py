'''
Exercise 80, file "pp_80.py"
The text is given:
shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field, ....'

Write a program that finds and prints the longest word in the text to the terminal. 
To achieve this, implement a function that removes all periods ('.') and commas (','), extracts a list of all words, 
creates a dictionary of word-length pairs using dictionary comprehension, and uses the sorted() function.

Expected result:
The longest word is 'trenches' with the length 8 characters.

'''


def get_longest_word(text: str) -> tuple[str, int]:
    '''
    Function returns the longest word together with its length

    Parameters:
        text: any text
    Returns:

    Exemplary result:
    ('trenches',8)
    '''
    text = text.replace(',', '').replace('.', '')
    words = text.split()
    word_length = {word: len(word) for word in words}
    sorted_word_length = sorted(
        word_length.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_length[0]


shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field,'
print(get_longest_word(shakespeare))
