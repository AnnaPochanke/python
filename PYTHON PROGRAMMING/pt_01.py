'''
Programming task 01, file pt_01.py, 20 min.
Grade : 5 points

Write a program that will remove punctuation from any string, optionally (default arguments) it should remove spaces.
Implement the function definition

Expected exemplary result:
Here is a text without punctuations: 'Wow Thats amazing How did you do it Im so impressed Youre awesome brilliant and talented Congratulations Well done Bravo'

Send to Teams !!!

Don't use translate() function. Think about iterative way or list comprehension
'''


sample_text = "Wow! That's amazing. How did you do it? I'm so impressed. You're awesome, brilliant, and talented. Congratulations! Well done. Bravo!"


def remove_punctuation(text: str, remove_space: bool = False) -> str:
    '''
    Function removes punctuations !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ optionally it can remove spaces

    Parameters:
        text: any text
        remove_space: if True, spaces are removed, if False, spaces are not removed
    Returns:
        text without punctuation, optionally spaces.
    '''
    import string
    punct = string.punctuation
    if remove_space:
        punct += ' '
    return ''.join([char for char in text if char not in punct])


print(
    f"Here is a text without punctuations: '{remove_punctuation(sample_text)}'")
print(
    f"Here is a text without punctuations and spaces: '{remove_punctuation(sample_text, True)}'")
