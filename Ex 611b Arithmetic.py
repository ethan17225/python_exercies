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

# def function main
# In a loop ask user to enter two numbers and an operator
# Perform the operation based on the operator
# Note: use if elif else statements
# ask user if they want to continue
# if user enters n break the loop


def main():
    while True:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        operator = input("Enter operator: ")

        # print sum, subtract, multiply, divide
        # in separate lines
        # using functions sum, subtract, multiply, divide
        # based on the operator
        # if operator is + call function sum and print result
        # if operator is - call function subtract and print result
        # if operator is * call function multiply and print result
        # if operator is / call function divide and print result
        # if operator is anything else print "Invalid operator"

        # ask user if they want to continue
        # if user enters n break the loop
        if input("Do you want to continue? (y/n): ") == "n":
            break


# call function main
main()
