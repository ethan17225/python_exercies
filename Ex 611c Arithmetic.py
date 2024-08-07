# Using UDF create a calculator
# Author: Amandeep Patti


# Objective(s):
# UDF chaining


# def function sum
# which takes two parameters a and b
# and returns a + b
def sum(a, b):
    return a + b


# def function subtract
# which takes two parameters a and b
# and returns a - b
def subtract(a, b):
    return a - b


# def function multiply
# which takes two parameters a and b
# and returns a * b
def multiply(a, b):
    return a * b


# def function divide
# which takes two parameters a and b
# and returns a / b
def divide(a, b):
    return a / b

# def function calc
# which takes three parameters op1, op2 and op
# and returns result based on operator
# by calling functions sum, subtract, multiply, divide
# Note: use if elif else statements


# def function main
# In a loop ask user to enter two numbers and an operator
# Perform the operation using calc udf
# ask user if they want to continue
# if user enters n break the loop


def main():
    while True:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        operator = input("Enter operator: ")

        # print result by using function calc

        # ask user if they want to continue
        # if user enters n break the loop
        if input("Do you want to continue? (y/n): ") == "n":
            break


# call function main
main()
