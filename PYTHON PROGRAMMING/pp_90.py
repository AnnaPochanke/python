'''
Exercise 90, file pp_90.py

Write a function to check whether a word or sentence is a palindrome.

1. Remove punctuation marks and spaces.
2. Use an iterative method (loop) to verify if it is a palindrome.

These are palindromes, test with them:
Dad 
Evil olive.
Never odd or even.
Amore, Roma.

Not palindromes:
test
ad
a
'''


def is_palindrome(text: str) -> bool:
    '''
    Function checks if any text is palindrome or not

    Parameters:
        text: any text
    Returns:
        True: if text is palindrome
        False: if text is not a palindrome
    '''
    # your code below
    text = text.lower()
    text = text.replace(' ', '')
    text = text.replace(',', '')
    text = text.replace('.', '')
    return text == text[::-1]


print(is_palindrome('Dad'))
print(is_palindrome('Evil olive.'))
print(is_palindrome('Never odd or even.'))
print(is_palindrome('Amore, Roma.'))
print(is_palindrome('test'))
print(is_palindrome('ad'))
print(is_palindrome('a'))
