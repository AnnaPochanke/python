'''
Exercise 70, file "pp_70.py"

LEARNING DICTIONARY COMPREHESION

Write a program that will display a list of tuples consisting of the most frequent characters in a sentence and their frequency, sorted in descending order.

To complete the task:

Define a function def most_freq_character(sentence):
Use a dictionary as the data structure and dictionary comprehension.
Use count() method of string class to count characters.
Ignore spaces, coma, dots in your analysis.

For testing purposes, use the sentence: "The robbed that smiles, steals something from the thief."

Expected result: [('t', 7), ('e', 7), ('h', 5), ('s', 5), ('o', 3), ('m', 3), ('i', 3), ('r', 2), ('b', 2), ('a', 2), ('l', 2), ('f', 2), ('d', 1), ('n', 1), ('g', 1)]

'''


def most_freq_character(sentence: str) -> list[tuple[str, int]]:
    '''
    Function returns list of characters together with its length

    Parameters:
        sentence: any text
    Returns:
        List of tuples (character, its length)'
        '''
    char_dict = {char: sentence.count(
        char) for char in sentence if char not in [' ', ',', '.']}
    return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)


print(most_freq_character("The robbed that smiles, steals something from the thief."))
