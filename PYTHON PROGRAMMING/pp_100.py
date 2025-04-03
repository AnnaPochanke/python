# '''
# Exercise 100, file pp_100.py
# Write a program that computes the value of n factorial - n!
# Use iterative implementation
# Expected results
# -10! => ERROR
# 0! = 1
# 1! = 1
# 2! = 1 * 2 = 2
# 3! = 1 * 2 * 3 = 6
# 4! = 1 * 2 * 3 * 4
# 10! = 3628800
# 32! = 263130836933693530167218012160000000
# n! = 1 * 2 * 3 * .... * n

# '''


def factorial(n: int) -> int:
    # '''
    # Functions calculates the factiorial of n

    # Parameters:
    #     n: number, positive int
    # Returns:
    #     The factorial

    # '''
    if n < 0:
        raise ValueError('ERROR')
    elif n == 0:
        return 1
    else:
        fact = 1

        for i in range(1, n + 1):
            fact *= i
        return fact


print(factorial(-10))
# print(factorial(0))
# print(factorial(1))
# print(factorial(2))
# print(factorial(3))
# print(factorial(4))

# print(factorial(10))
# print(factorial(32))
# print(factorial(100))
