# Test Prime Number using for loop
# Author: Amandeep Patti

# a number is prime if it is divisible by 1 and itself
# 1 is not a prime number
# 2 is the only even prime number

# get input from user and store it in num
num = int(input("Enter a positive integer number : "))

# assuming number is prime, initialize flag to True
is_prime = True

# even numbers are not prime except 2,
# set flag to False
# otherwise test whether num is divisible by 2

if 
    
else:
    # loop from 2 to num - 1
    for i in range(2, num):

        # if num is divisible by i, set flag to False and break out of loop
        if (num % i == 0):
            is_prime = False
            break

# print whether num is prime
if (is_prime):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
