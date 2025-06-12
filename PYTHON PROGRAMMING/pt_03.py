# Programming Task 03c

# **Topic: ** Fix My Code & Explain Yourself
# **Level: ** Intermediate Python
# **Points: ** 15

# # Exercise Title: Fix My Code & Explain Yourself

# # Context:

# You are working for a fictional bookstore system in Poznań that stores books and tracks prices in Polish złoty(zł).

# # Task:

# You receive the following broken Python function written by a former intern. Your job is to:

# 1. Fix the function, so it works as intended.
# 2. Write a short explanation(2 - 3 sentences):

#     * What was wrong with the original code?
#     * What did you change and why does it work now?

# # Requirements:

# * The function should reduce the price by a given percentage (e.g., 90 % means a 10 % discount).
# * Final prices must be rounded to 2 decimal places (round() function).
# * The function should not mutate the original list `book_list`.
# * You must explain your fix.

# # What You'll Be Graded On:

# * Correctness of the fixed function(5 pts)
# * Proper handling of rounding 2 pts)
# * Clear explanation of the bug and solution(5 pts)
# * Price formatting function(up to 3 pts)

# Add a function `format_prices(books)` that returns a list of strings like:

# ["Zrozumieć Pythona: 72.00 zł", "Algorytmy i struktury danych: 90.00 zł"]

# '''
# # Broken code


# def apply_discount(books, discount):
#     for book in books:
#         book["price"] = book["price"] * discount
#     return books


# # Intended usage:
# book_list_changed = apply_discount(book_list, 0.90)


def apply_discount(books, discount):
    # Create a new list to store the discounted books
    discounted_books = []

    for book in books:
        # Calculate the new price with discount and round it to 2 decimal places
        new_price = round(book["price"] * discount, 2)
        # Create a new dictionary for the discounted book
        discounted_book = {"title": book["title"], "price": new_price}
        # Append the discounted book to the new list
        discounted_books.append(discounted_book)

    return discounted_books


def format_prices(books):
    formatted_prices = []
    for book in books:
        # Format the price to 2 decimal places and append to the list
        formatted_prices.append(f"{book['title']}: {book['price']:.2f} zł")
    return formatted_prices


# Sample input:
book_list = [
    {"title": "Zrozumieć Pythona", "price": 80},
    {"title": "Algorytmy i struktury danych", "price": 100}
]
# Intended usage:
book_list_changed = apply_discount(book_list, 0.90)
# Print the formatted prices
formatted_prices = format_prices(book_list_changed)
for price in formatted_prices:
    print(price)
# Explanation:
# The original code had a bug where it directly modified the prices in the input list, which is not allowed as per the requirements.
# I fixed it by creating a new list `discounted_books` to store the modified books without changing the original list.
# I also ensured that the prices are rounded to 2 decimal places using the `round()` function.
# The `format_prices` function formats the book titles and prices as required.
# The function now works correctly, applying the discount and formatting the prices as specified.
