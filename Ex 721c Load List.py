# Load a list
# Author: Amandeep Patti

# Objective(s):
# Loading list values using list comprehension
# based on a condition tested using a function

def is_even(n):
    return n % 2 == 0


def is_prime(x):
    if is_even(x):
        return False

    for d in range(3, x//2, 2):
        if x % d == 0:
            return False

    return True

# def main


def main():
    # using list comprehension load the list with prime numbers from 0 to 100
    # Note use is_prime function to check if a number is prime
    prime_number_list = 

    # print the list
    print(prime_number_list)


main()
