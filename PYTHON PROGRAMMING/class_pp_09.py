#######################################################
# RE part II
#######################################################

# 17 Search for a sequence that starts with "h", followed by 0 or more  'e' characters, and an "o" at the end
# test with "hello world", "heeeo world"

import re
test_list = ['hello world', 'heeeo world']
pattern = r"he*o"
for s in test_list:
    # 'he*o' - matches 'h', followed by 0 or more 'e' characters, and an 'o' at the end
    # re.search() returns a match object if the pattern is found, otherwise it returns None
    if re.search(pattern, s):
        print(f'{s}->a match')
    else:
        print(f'{s} -> no match')

for s in test_list:
    # 'he*o' - matches 'h', followed by 0 or more 'e' characters, and an 'o' at the end
    # re.search() returns a match object if the pattern is found, otherwise it returns None
    x = re.search(pattern, s)
    print(s + '-->' + str(x))

# # 18

test_list = ['green', 'gren', 'trap']
# '+' matches 'r', followed by 1 or more 'e' characters, and 'n' at the end
pattern = r"re+n"
for s in test_list:
    # 'he*o' - matches 'h', followed by 0 or more 'e' characters, and an 'o' at the end
    if re.search(pattern, s):
        print(f'{s}->a match')
    else:
        print(f'{s} -> no match')

# 19 Search for a sequence that starts with "h", followed by 0 or more  (any) characters, and an "o" at the end
# precise what was matched
l_txt = [
    'hello world',
    'gghemmmmmo world',
    'hellhghio world and planet'
]
print('\n')
for s in l_txt:
    x = re.search("he.*o", s)
    print(s + '-->' + str(x))


for s in ('ana', 'mana', 'manab'):
    # \Z - matches the end of the string
    # \z - matches the end of the string, but not before a newline
    # \b - matches the empty string at the beginning or end of a word
    # \B - matches the empty string, but not at the beginning or end of a word
    if re.search('ana\Z', s):
        print('a match')
    else:
        print('no match')


##################################
# RE USEFUL FUNCTIONS
##################################


# 100. findall() function
# findall() returns a list of all matches of the pattern in the string

for s in ('aaaa', 'aaa', 'aa', 'aba', 'aab'):
    # re.findall() returns a list of all matches of the pattern in the string
    # r'aa' - matches 'aa' literally
    # re.findall() returns an empty list if there are no matches
    matches = re.findall(r'aa', s)
    if matches:
        print(f'{s} -> a match: {matches}')
    else:
        print(f'{s} -> no match')


# 110. findall() find list of instances: banana
txt = "This is banana. Banana is very good. \n I like banana very much. Here are other fruits: strawberries, raspberries, pineapples."
L1 = re.findall('banana', txt)
L1 = re.findall('banana', txt.lower())
L1 = re.findall('[Bb]anana', txt)

print(L1)

'--------------------------------'

# 120. findall() with regex, let's find phone numbers
# '\d' - matches any digit, equivalent to [0-9]
# '\d{3}-\d{3}-\d{4}' - matches phone numbers in the format 123-456-7890
# import re

text = "My phone number is 123-456-7890 and my office number is 987-654-3210. \n You can also reach me at 555-123-4567 or 111-222-3333."
pattern = r'\d{3}-\d{3}-\d{4}'  # this matches phone numbers

matches = re.findall(pattern, text)
print(matches)

'--------------------------------'

# 130. findall() with regex, let's find all words that start with a capital letter in a sentence. We can use a pattern like this:
# import re
# \b[A-Z][a-z]*\b - matches a word that starts with a capital letter
'''
\b is a word boundary. It ensures the match starts and ends at the edge of a word.

[A-Z] means the word starts with a capital letter.

[a-z]* means it can be followed by zero or more lowercase letters.
'''

text = "Alice went to Paris to meet Dr. Smith and Professor Oak.\n She also met Mr. Johnson and Ms. Davis."
pattern = r'\b[A-Z][a-z]*\b'

matches = re.findall(pattern, text)
print(matches)

'--------------------------------'

# 140. findall() with regex, let's find all email addresses in a text
# import re
# email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
# email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}'


'''
Part 1: [a-zA-Z0-9_.+-]+
This matches the username part before the @.
a-zA-Z → any lowercase or uppercase letter
0-9 → any digit
_ → underscore is allowed
. → dot (period) is allowed
+ → plus sign is allowed
- → hyphen is allowed
[ ... ] → defines a character set

+ after the set means one or more of the allowed characters

Example matches: john, john.doe, alice_smith+test

Part 2: @
This matches the literal "@" symbol that separates the username from the domain.

Part 3: [a-zA-Z0-9-]+
This matches the domain name, like example or company.
Letters and digits are allowed
Hyphens (-) are allowed

No dots here yet — that comes next

Part 4: \.
This matches the literal dot between the domain and the domain extension (like .com or .org). 
The backslash \ is needed to escape the dot, because . in regex normally means "any character".

Part 5: [a-zA-Z0-9-.]+
This matches the domain extension, like com, org, co.uk, etc.

Letters, digits, hyphens, and even extra dots (for multi-level domains) are allowed here

The + allows for extensions like co.uk, name.info, site.company.io
{2,} means at least 2 characters for the extension (like .com, .org, etc.)

Summary Example
With this regex, the following would all match:

john.doe@example.com

support@company.org

a.b-c_d+1@sub-domain.example.co.uk


\w  ≡  [a-zA-Z0-9_]
'''


text = """You can contact me at john.doe@example.com. This is just a random sentence.
Please send updates to support@company.org before Friday or a.b-c_d+1@sub-domain.example.co.uk."""

# Define the email address pattern

email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}'


# Use findall to extract all email addresses
emails = re.findall(email_pattern, text)

print("Email addresses found:")
for email in emails:
    print("-", email)

'--------------------------------'

# 150.  split() function, # splits a string into a list based on a specified delimiter
# Pattern: [;,.]\s*
# [;,.] → split on ;, ,, or .
# \s* → optionally include trailing whitespace
# import re

text = "apple, banana; orange. pineapple"
# # Example: Splitting a string by commas, semicolons, or periods

parts = re.split(r'[;,.]\s*', text)

parts = re.split(r'[.!?]\s*', text)
parts = re.split(r'(?<=[.!?])\s*', text)
# .!? are removed, but the split is done at the end of the sentence
print('1. ',  parts)

# # comparing with str.split()
parts_str_split = text.split()
print('2. ',  parts_str_split)

parts_str_split = text.split(', ')
print('3. ',  parts_str_split)

parts_str_split = text.split(',.;')
# no split, because there is no such delimiter in the string
print('4. ', parts_str_split)

'--------------------------------'

# 160.  split() function, let's split a string into sentences
# import re
# Example: Splitting a string into sentences using regex
# Pattern: (?<=[.!?])\s*
# (?<=[.!?]) → lookbehind assertion to find a position after ., !, or ?
# Uses a lookbehind (?<=...), which:
# - Matches positions after the punctuation
# - Does not consume the punctuation mark itself
# - Only removes the whitespace after the punctuation
# \s* → optionally include trailing whitespace


text = "This is the first sentence. This is the second sentence! Is it really? Yes, it is.\nHere is another one."
sentences = re.split(r'(?<=[.!?])\s*', text)  # with punctuation
# compare with the previous one (now without punctuation)
# sentences = re.split(r'[.!?]\s*', text)
print('Sentences:', sentences)
# # sentences = [s for s in sentences if s]  # Remove empty strings if any
for s in sentences:
    print("-", s)

'--------------------------------'

# 170.  split() function, let's split a string into words, with removing punctuation
# import re
# Example: Splitting a string into words, removing punctuation
# Pattern: \W+ → matches one or more non-word characters (anything that is not a letter, digit, or underscore)
# \W is equivalent to [^a-zA-Z0-9_]

text = "Hello! This is a test — of punctuation, numbers (123), and symbols like $ or #. \nLet's see how it works. This-is-hyphenated."

# Remove punctuation by splitting on anything that's NOT a word character or digit
words = re.split(r'\W+', text)
# remove empty strings, clean up empty results with a list comprehension
words = [word for word in words if word]

# # Treat hyphenated words as a single word by splitting on non-word characters except hyphen
# words = re.split(r'[^\w-]+', text)
# words = [word for word in words if word]

print("Words:")
print(words)

'--------------------------------'

# 180. Lets's extract website addresses (URLs) from a block of text using re.findall()

# Example: Extracting URLs from a block of text
# Pattern: r'(https?://[^\s]+|www\.[^\s]+)
# https? → matches "http" or "https"
# :// → matches the "://" part of the URL
# [^\s]+ → matches one or more characters that are not whitespace (the rest of the URL)
# # | → OR operator, allows matching either a full URL or one starting with "www."
# www\.[^\s]+ → matches URLs starting with "www." followed by non-whitespace characters
# import re

text = """
Visit our site at https://www.example.com for more info.
You can also check http://blog.example.org or our partner site at www.partner-site.net.
Don't forget https://sub.domain.co.uk/page?query=123 too!
"""

# Simple pattern to match most website URLs
url_pattern = r'(https?://[^\s]+|www\.[^\s]+)'

urls = re.findall(url_pattern, text)

print("Websites found:")
for url in urls:
    print("-", url)
