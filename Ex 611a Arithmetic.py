# Using UDF create a calculator
# Author: Amandeep Patti


# Objective(s):
# UDF with Arguments and Return Values


# def function sum
# which takes two parameters a and b
# and returns a + b
def sum(a, b):
    return a + b


# def function subtract
# which takes two parameters a and b
# and returns a - b


# def function multiply
# which takes two parameters a and b
# and returns a * b


# def function divide
# which takes two parameters a and b
# and returns a / b


# def function main
# In a loop ask user to enter two numbers
# Perform all arithmetic operations using UDFs
# Ask user if they want to continue
# If user enters n break the loop


def main():
    while True:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        # print sum, subtract, multiply, divide
        # in separate lines
        # using functions sum, subtract, multiply, divide

        print(sum(a, b))

        # ask user if they want to continue
        # if user enters n break the loop
        if input("Do you want to continue? (y/n): ") == "n":
            break


# call function main
main()
