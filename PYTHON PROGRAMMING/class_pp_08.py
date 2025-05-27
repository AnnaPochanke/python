import re
text = 'Artificial Intelligence (AI) is a rapidly evolving field that involves the development of computer systems capable of performing tasks that typically require human intelligence such as visual perception, speech recognition, and decision-making. AI systems can be trained using large amounts of data to recognize patterns and make predictions. Machine learning is a subfield of AI that focuses on the development of algorithms that can learn from and make predictions based on data. The use of AI is becoming widespread across various industries,including healthcare, finance, transportation, and retail. While AI has the potential to bring about significant positive change in our society, it also raises ethical and social issues. For example, the use of AI in decision-making could perpetuate existing biases and lead to unfair outcomes. There are also concerns about job displacement as AI systems become more capable of performing tasks that were previously done by humans. To address these challenges, there is a growing need for responsible and ethical AI development and deployment. This involves creating systems that are transparent, explainable, and accountable, as well as investing in education and training to ensure that individuals have the skills and knowledge to participate in the AI-driven economy. In conclusion, AI is a rapidly evolving field that has the potential to bring about significant positive change, but it is important that we approach its development and deployment with caution and responsibility.'

# 'Check if the string contains the sentence which starts with "The" and ends with "retail"'

# def contains_the_to_retail(text):
#     # This pattern looks for a sentence that starts with "The" and ends with "retail"
# #      're.DOTALL flag to re.search() or re.findall() allows the . in the regex pattern to match any character including newlines.'
#     pattern = r'\bThe\b.*?\bretail\b[.!?]?'

#     match = re.search(pattern, text, re.DOTALL)
#     return bool(match)


# print(contains_the_to_retail(text))  # Output: True

######


# def extract_sentence_the_to_retail(text):
#     # Pattern to find a sentence that starts with 'The' and ends with 'retail' optionally followed by punctuation
#     # 're.DOTALL flag to re.search() or re.findall() allows the . in the regex pattern to match any character including newlines.'

#     pattern = r'\bThe\b.*?\bretail\b[.!?]?'

#     match = re.search(pattern, text, re.DOTALL)
#     if match:
#         return match.group()
#     else:
#         return None


# result = extract_sentence_the_to_retail(text)

# if result:
#     print("Found sentence:", result)
# else:
#     print("No matching sentence found.")


def contains_the_to_retail(text):
    # This pattern looks for a sentence that starts with "The" and ends with "retail"
    # 're.DOTALL flag to re.search() or re.findall() allows the . in the regex pattern to match any character including newlines.'
    pattern = r'\bThe\b.*?\bretail\b[.!?]'

    match = re.search(pattern, text, re.DOTALL)
    return bool(match)


print(contains_the_to_retail(text))  # Output: True


def extract_sentence_the_to_retail(text):
    # Pattern to find a sentence that starts with 'The' and ends with 'retail' optionally followed by punctuation
    # 're.DOTALL flag to re.search() or re.findall() allows the . in the regex pattern to match any character including newlines.'

    pattern = r'\bThe\b.*?\bretail\b[.!?]'

    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group()
    else:
        return None


result = extract_sentence_the_to_retail(text)
if result:
    print("Found sentence:", result)
else:
    print("No matching sentence found.")
