# '''
# Exercise 40, pp_40.py

# Task is very similar to the exercise 30 but additionally you have to write & use a function removing punctuation.
# Write a program with functions called map_longest(), remove_punctuation() that takes a text as a parameter and returns the longest word contained in that text along with its length as a tuple.
# The result of the program should be a message, e.g., 'The longest word in the text is 'decision-making' with a length of 15 characters.'

# Use map function together with lambda + remove punctuation
# '''


# def remove_punctuation(word: str) -> str:
#     '''
#     Function removes punctuation from the given string

#     Parameters:
#         word: any string with or without the punctuation
#     Returns:
#         string without punctuation
#     '''


# def map_longest(text: str) -> tuple:
#     '''
#     Function returns the longest word in the text and it's length

#     Parameters:
#         text: any text

#     Returns:
#         tuple: a tuple containing the logest word and it's length

#     '''


text = '''
 Artificial Intelligence (AI) is a rapidly evolving field that involves the development of computer systems capable of performing tasks that typically require human intelligence such as
visual perception, speech recognition, and decision-making. AI systems can be trained using large amounts of data to recognize patterns and make predictions. Machine learning is a
subfield of AI that focuses on the development of algorithms that can learn from and make predictions based on data. The use of AI is becoming widespread across various industries, including healthcare, finance, transportation, and retail. While AI has the potential to bring about significant positive change in our society, it also raises ethical and social issues.
For example, the use of AI in decision-making could perpetuate existing biases and lead to unfair outcomes. There are also concerns about job displacement as AI systems become more capable
 of performing tasks that were previously done by humans. To address these challenges, there is a growing need for responsible and ethical AI development and deployment.
 This involves creating systems that are transparent, explainable, and accountable, as well as investing in education and training to ensure that individuals have the skills and knowledge
to participate in the AI-driven economy. In conclusion, AI is a rapidly evolving field that has the potential to bring about significant positive change, but it is important that we approach
 its development and deployment with caution and responsibility.
'''


def remove_punctuation(word):
    return word.replace(',', '').replace('.', '').replace('(', '').replace(')', '')


def map_longest(text: str) -> tuple:
    words = text.split()
    words = (map(remove_punctuation, words))
    L1 = (map(lambda item: (item, len(item)), words))
    longest_word = max(L1, key=lambda item: item[1])
    return longest_word


longest_word, length = map_longest(text)
print(
    f'The longest word in the text is {longest_word}, with a length of {length} characters.')
