'''
Exercise 60 (file "pp_60.py")
Write a program that will display a list of tuples consisting of the most frequent characters in a sentence and their frequency, sorted in descending order.

To complete the task:

Define a function def most_freq_character(sentence):
Use a dictionary as the data structure and loop for specifying characters and its amount.
Ignore spaces in your analysis.
For testing purposes, use the sentence: "The robbed that smiles, steals something from the thief."

Expected result: [('t', 7), ('e', 7), ('h', 5), ('s', 5), ('o', 3), ('m', 3), ('i', 3), ('r', 2), ('b', 2), ('a', 2), ('l', 2), ('f', 2), ('d', 1), (',', 1), ('n', 1), ('g', 1), ('.', 1)]

'''


def most_freq_character(sentence):
    '''
    Function returns list of characters together with its length

    Parameters:
        sentence: any text
    Returns:
        List of tuples (character, its length)'
        '''
    char_dict = {}
    for char in sentence:
        if char != ' ':
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)


print(most_freq_character("The robbed that smiles, steals something from the thief."))
