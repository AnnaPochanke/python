
# Exercise 10, file pp_10.py
# Write a Python function named fizz_buzz(num) that:
# Returns the string 'Fizz' if the num parameter is divisible by 3.
# Returns the string 'Buzz' if the num parameter is divisible by 5.
# Returns the string 'FizzBuzz' if the num parameter is divisible by both 3 and 5.
# Returns num for any other number.
# The function should include a docstring.
# Additionally, the program should allow the user to enter a number multiple times during runtime.
# Typing "q" should quit the program. Use keyword arguments where appropriate.
def fizz_buzz(num):
    """
    Returns 'Fizz' if num is divisible by 3,
    'Buzz' if num is divisible by 5,
    'FizzBuzz' if num is divisible by both 3 and 5,
    and num otherwise.
    """
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num


def main():
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        try:
            num = int(user_input)
            print(fizz_buzz(num))
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()

