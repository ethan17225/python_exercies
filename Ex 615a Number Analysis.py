# Using UDF perform simple number analysis
# Author: Amandeep Patti

# Objective(s):


# def function get_number
# which takes no parameters
# and returns a number entered by user


# def function display_number
# which takes one parameter x
# and prints x


# def function is_even
# which takes one parameter x
# returns True if x is even otherwise False


# def function is_odd
# which takes one parameter x
# returns True if x is odd otherwise False


# def function half_it
# which takes one parameter x
# returns x//2


# def function double_it
# which takes one parameter x
# returns x*2


# def function main


def main():
    # get a number from user using get_number udf
    n = get_number()

    # display the number using display_number udf
    display_number(n)

    # if number is even half it, use is_even and half_it udfs
    if is_even(n):
        n = half_it(n)

    # if number is odd double it, use is_odd and double_it udfs
    if is_odd(n):
        n = double_it(n)

    display_number(n)


# call main function
main()
