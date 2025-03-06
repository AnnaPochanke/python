# Exercise 18
# Write a program that prints first 10 primes, separated by a comma.
# (Use a while loop and a break statement in your solution.)
# INPUT: prime_count = 10
# OUTPUT: str. e.g., 2,3,5,7,11,13,17,19,23,29
# Hint: what is a prime numer
# https://thirdspacelearning.com/blog/what-is-a-prime-number/
import math
L = []
prime_count = 10
i = 2
while len(L) < prime_count:
    is_prime = True
    for divisor in range(2, int((math.sqrt(i)+1))):
        # print("Dzielę", i, "przez", divisor)
        if i % divisor == 0:
            is_prime = False
            # print(i, "is not prime")
    if is_prime == True:
        L.append(str(i))
    i += 1

prime_numbers = ",".join(L)
print(prime_numbers)
print(type(prime_numbers))
