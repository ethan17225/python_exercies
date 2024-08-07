# Number Analysis update status variables without using if-else statements
# Author: Amandeep Patti

# input an integer number
num = int(input("Enter an integer number: "))

# set status variables to false
isPositive = isNegative = isZero = is_even = is_odd = False

# set variable isPositive to true if number is positive otherwise false

# set variable isNegative to true if number is negative otherwise false

# set variable isZero to true if number is zero otherwise false

# set variable is_even to true if number is even otherwise false

# set variable is_odd to true if number is odd otherwise false

# perform following operations based on status variables
# print result without storing in a variable

# Positive Even numbers must be divided to half
if isPositive and is_even:
    print("Positive Even number")
    print("Divide by 2: ", num / 2)

# Negative Even numbers must be doubled
if isNegative and is_even:
    print("Negative Even number")
    print("Double it: ", num * 2)

# Positive Odd must be incremented by 10
if isPositive and is_odd:
    print("Positive Odd number")
    print("Increment by 10: ", num + 10)

# Negative Odd must be decremented by 10
if isNegative and is_odd:
    print("Negative Odd number")
    print("Decrement by 10: ", num - 10)
