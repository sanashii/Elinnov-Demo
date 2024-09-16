# Made by: Andrea Baulita
# Date: 09-16-2024
# Description: A python program for checking if a given number is prime or not and finding the factorial of that given number.
#              This program makes use of custom tkinter GUI for user input and output.

import math # used for square root function
import time # used to time the functions for efficiency

# function to check if a number is prime or not
def prime_number_check(num):
    # a prime number must be greater than 1, so we return False if numbers <= 1
    if num <= 1:
        return False
    
    # we only need to check divisors up to the square root of the number for efficiency
    # if a number has a divisor greater than its square root, it will also have a divisor less than the square root
    for i in range(2, int(math.sqrt(num)) + 1):
        # if num is divisible by any number between 2 and sqrt(num), it is not prime so we return False in that case
        if num % i == 0:
            return False
    
    # if no divisors were found, the number is prime
    return True

# function to calculate the factorial of a number
def factorial_of_number(num):
    # initializing the result to 1, as factorial starts with multiplying by 1
    result = 1
    
    # loop through all numbers from 2 to num and multiply the result by each number
    for i in range(2, num + 1):
        result *= i
    
    # return the final result which is the factorial of the number
    return result







# # ***** initial sample test for logic check *****
# num =128

# # checking the runtime of the prime number check & factorial functions for efficiency
# start_time = time.time()
# is_prime = prime_number_check(num)
# end_time = time.time()

# start_time = time.time()
# factorial_result = factorial_of_number(num)
# end_time = time.time()

# print(f"Prime Check: {is_prime}, Time Taken: {end_time - start_time:.6f} seconds")
# print(f"Factorial: {factorial_result}, Time Taken: {end_time - start_time:.6f} seconds")

