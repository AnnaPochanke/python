# A dictionary is given:
# stocks = {'Playway': 35, 'CD Projekt': 150, 'Boombit': 320}
# Using the dictionary comprehension, extract from the dictionary key-value pairs with a value above 100.
# Use drag and drop method. Not all choices are correct.
# EXPECTED RESULT:
# stocks = {'CD Projekt': 150, 'Boombit': 320}
# '''
stocks = {'Playway': 35, 'CD Projekt': 150, 'Boombit': 320}
d = {k: v for k, v in stocks.items() if v > 100}
print(d)
