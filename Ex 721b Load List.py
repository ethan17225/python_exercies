# Load a list
# Author: Amandeep Patti

# Objective(s):
# Loading list values using a while loop
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

# define main function


def main():
    i = 0
    prime_number_list = []

    # using a while loop load the list with prime numbers from 0 to 100
    # Note use is_prime function to check if a number is prime
    # and then add it to the list
    while i < 100:

        i += 1

    # print the list
    print(prime_number_list)


# call main function
main()
