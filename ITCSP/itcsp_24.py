# Exercise 24
# Modify exercise 22.
# Additionally implement the possibility of creating the list manually, using input(), entering 'q' should finish list creation.
# Finally, implement the possibility of choosing element to be removed (input() function )
# The old list and the new list should be printed to the terminal


while True:
    user_input = input(
        "Enter a sequence of word that will create a list: ")
    if user_input.lower() == "q":
        break
    user_input = user_input.replace(",", "")
    L = list(user_input.split())
    print("Your list looks like this: ", L)
    removing = input("Choose which element do you want to remove ...")
    if removing not in L:
        print("This element is not a part of your list. You list looks like this: ", L)
    else:
        L.remove(removing)
    print("You removed", "'", removing, "' "
          "and your modified list looks now like this ", L)
