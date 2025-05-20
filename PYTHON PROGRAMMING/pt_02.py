# '''
# **Programming Task 02**
# File: pt_02.py
# Score: 10 points, 15 min

# ### Learning Dictionary Comprehension

# Write a program that prints a list of tuples, where each tuple contains the most frequent character(s) in the given sentence(s) along with their frequency. The list should be sorted in descending order based on frequency.

# To complete this task:

# 1. Define a function:

# def get_character_freq(sentence):
#     characters_freq = {}
#     # Your code here
#     return sorted_characters_freq


# 2. Define another function:

# def remove_punctuation(text: str, remove_space: bool = False) -> str:
#     # Your code here


# 3. Use a dictionary as the primary data structure.
# 4. Ignore spaces, commas, periods, and other punctuation marks. Convert all characters to lowercase before analysis.
# 5. Use the `count()` method of the string class to count character occurrences.

# Expected result:
# [('e', 66), ('t', 56), ('h', 49), ('o', 48), ('s', 39), ('a', 38), ('r', 30), ('n', 27), ('d', 24), ('u', 22), ('l', 22), ('i', 21), ('w', 16), ('\n', 15), ('m', 13), ('c', 13), ('y', 13), ('f', 12), ('b', 8), ('g', 5), ('p', 4), ('v', 4), ('k', 2)]
# '''

def get_character_freq(sentence):
    characters_freq = {}
    # Your code here
    for char in sentence:
        if char.isalpha():
            char = char.lower()
            if char in characters_freq:
                characters_freq[char] += 1
            else:
                characters_freq[char] = 1

    sorted_characters_freq = sorted(
        characters_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_characters_freq


def remove_punctuation(text: str, remove_space: bool = False) -> str:
    import string
    if remove_space:
        text = text.replace(" ", "")
    return text.translate(str.maketrans("", "", string.punctuation))


# Example usage
if __name__ == "__main__":
    # Example sentence
    sentence = "This is a test sentence. Let's count the characters."

    # Remove punctuation and spaces
    cleaned_sentence = remove_punctuation(sentence, remove_space=True)

    # Get character frequency
    result = get_character_freq(cleaned_sentence)

    # Print the result
    print(result)
