# Imagine you are a young entrepreneur who has decided to start a shop. Write a program to manage the assortment of your store. Implement the following functionalities:

# Adding a product
# Changing the name of a product
# Deleting a product
# Displaying all products on the terminal screen
# First, decide which data structure you will use to store your product names.

# Program-User Interaction
# I envision the program-user interaction as follows (please format the terminal output as shown below):

# =========================================
# Store Management Software, Version 1.0.0
# =========================================
# Please select the operation you want to perform:
# 1. Add a product
# 2. Change the name of a product
# 3. Remove a product
# 4. Show all products
# 5. Exit the program
# --> ...


# Detailed Functionalities
# Adding a Product
# Selecting option 1 should display a message like this:

# --> Enter the name of the product you want to add ...
# (The user should enter the name of the new product, and the program should add this name to the data structure.)

# Changing the Name of a Product
# Selecting option 2 should display a message like this:

# --> Enter the product number you want to rename ...
# (The user should enter the product number, and the program should prompt them to enter a new name for the selected product.)

# Removing a Product
# Selecting option 3 should display a message like this:

# --> Enter the product number you want to remove ...
# (The user should enter the product number, and the program should remove the corresponding product from the data structure.)

# Displaying All Products
# Selecting option 4 should display a list of all products entered so far, along with their indexes (starting from 1). For example:

# My products:
# 1. Bananas
# 2. Oranges
# 3. Apples
# 4. Figs
# 5. Strawberries
# ===== Finished

# Exiting the Program
# Selecting option 5 should terminate the program.

# Implementation Details
# Use a variable named products to store the product names.
# Implement the "Show all products" operation as a function:


# def show_products(products: list) -> None:
#     ...
# This function should be invoked when the user selects the corresponding option.

# Implement Error Handling
# - Invalid menu options
# - Attempting to rename or delete a product when the list is empty

# '''


# def show_products(products: list) -> None:
#     '''
#     Function prints all products

#     Parameters :
#         products: list of products
#         eg. 1. Orange
#             2. Bananas
#     '''
#     # your code


# start = '''
# =========================================
# Store management software, version 1.0.0
# ========================================='''
# products = []
# menu = '''
#     Please select the operation you want to perform:
#     1. Add a product
#     2. Change the name of the product
#     3. Remove the product
#     4. Show all products
#     5. Exit the program
#     '''

# print(start)
# while True:
#     print(menu)
#     # your code


def show_products(products: list) -> None:
    '''
    Function prints all products

    Parameters : 
        products: list of products
    '''
    if not products:
        print("No products available.")
    else:
        print("My products:")
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product}")
    print("===== Finished")


def main():
    start = '''
    =========================================
    Store management software, version 1.0.0
    ========================================='''

    products = []
    menu = '''
    Please select the operation you want to perform:
    1. Add a product
    2. Change the name of a product
    3. Remove a product
    4. Show all products
    5. Exit the program
    '''

    print(start)

    while True:
        print(menu)
        choice = input("--> ")

        if choice.isdigit():
            choice = int(choice)

            if choice == 1:
                product_name = input(
                    "--> Enter the name of the product you want to add: ")
                products.append(product_name)
                print(f"Product '{product_name}' added successfully.")

            elif choice == 2:
                if not products:
                    print("No products available to rename.")
                else:
                    product_number = input(
                        "--> Enter the product number you want to rename: ")
                    if product_number.isdigit():
                        product_number = int(product_number)
                        if 1 <= product_number <= len(products):
                            new_name = input(
                                "--> Enter the new name for the product: ")
                            products[product_number - 1] = new_name
                            print(f"Product renamed to '{new_name}'.")
                        else:
                            print("Invalid product number.")
                    else:
                        print("Please enter a valid number for the product.")

            elif choice == 3:
                if not products:
                    print("No products available to remove.")
                else:
                    product_number = input(
                        "--> Enter the product number you want to remove: ")
                    if product_number.isdigit():
                        product_number = int(product_number)
                        if 1 <= product_number <= len(products):
                            removed_product = products.pop(product_number - 1)
                            print(f"Product '{
                                  removed_product}' removed successfully.")
                        else:
                            print("Invalid product number.")
                    else:
                        print("Please enter a valid number for the product.")

            elif choice == 4:
                show_products(products)

            elif choice == 5:
                print("Exiting the program.")
                break

            else:
                print("Invalid option. Please select a valid operation.")

        else:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
