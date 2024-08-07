# Using UDF perform simple number analysis
# Author: Amandeep Patti

# Objective(s):


# def function get_number
# which takes a prompt as parameter
# Note prompt is optional with default value "Enter a number: "
# and returns a number entered by user
# and returns a number entered by user
def get_number(prompt="Enter a number: "):
    return int(input(prompt))


# def function display_number
# which takes one parameter x
# and prints x
def display_number(x):
    print(x)

# def function is_even
# which takes one parameter x
# returns True if x is even otherwise False


def is_even(x):
    return x % 2 == 0

# def function is_odd
# which takes one parameter x
# returns True if x is odd otherwise False


def is_odd(x):
    return x % 2 != 0

# def function half_it
# which takes one parameter x
# returns x//2


# define function is_prime which takes one parameter x
# returns True if x is prime otherwise False

def is_prime(x):
    if is_even(x):
        return False

    for d in range(3, x//2, 2):
        if x % d == 0:
            return False

    return True

# def function is_armstrong which takes one parameter x
# returns True if x is Armstrong otherwise False


def is_armstrong(x):

    p = len(str(x))

    temp = x
    sum = 0

    while temp > 0:
        sum += (temp % 10) ** p
        temp //= 10

    return x == sum

# def function reverse which takes one parameter x
# returns reverse of x


def reverse(x):
    rev = 0

    while x > 0:
        rev = rev * 10 + x % 10
        x = x//10

    return rev


# def function is_palindrome which takes one parameter x
# returns True if x is Palindrome otherwise False
# Note: use reverse udf
def is_palindrome(x):
    return x == reverse(x)


# def function selectedNumbers
# which takes three parameters start, end and type
# and return a string having all number between start and end (inclusive)
# matching the type (type can be prime, armstrong or palindrome)
# Note: use is_prime / is_armstrong / is_palindrome udf


# def function main


def main():
    # get starting of range get_number udf
    start = get_number("Start of the Range: ")

    # get ending of range get_number udf
    end = get_number("End of the Range: ")

    # for each number in range, print all prime numbers using selectedNumbers udf
    print(selected_numbers(start, end, "prime"))

    # for each number in range, print all armstrong numbers using selectedNumbers udf

    # for each number in range, print all palindrome numbers using selectedNumbers udf


# call main function
main()
