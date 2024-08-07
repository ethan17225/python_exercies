# Using UDF print Hi and Bye
# Author: Amandeep Patti

# Objective(s):
# Implement main udf as starting point of program


# Function named get_name to get name of user and return it
def get_name():
    name = input("Enter your name: ")
    return name

# Function named say_hi to print "Hi" and name of user passed as argument


def say_hi(name):
    print("Hi", name)

# Function named say_bye to print "Bye" and name of user passed as argument


def say_bye(name):
    print("Bye", name)


# Define udf main to manage flow of program as
# Get name of user by calling function get_name
# Call function say_hi with argument user
# Call function say_bye with argument user


# Call function main
