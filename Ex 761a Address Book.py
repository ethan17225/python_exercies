# Address Book
# Author : Amandeep Patti

# Objective(s):
# 1. Read structured content from a file
# 2. Write structured content to a file
# 3. Use with statement to open a file

# Todo:
# 1. Create a file named "addressbook.txt"
# 2. Ask the user to enter the name, email and phone number of a person
# 3. Write the name, email and phone number separated by a comma to the file
# 4. Ask the user if he/she wants to add another person
# 5. If the user enters n, then break the loop
# 6. Display the content of the file as it is
# 7. Display the content of the file as address book
# Note: Use with statement to open a file

# Sample Output:
# Enter the name of the person: John
# Enter the email of the person: john@example
# Enter the phone number of the person: 1234567890
# Do you want to add another person (y/n): y
# Enter the name of the person: Jane
# Enter the email of the person: jane@example
# Enter the phone number of the person: 1234567891
# Do you want to add another person (y/n): n
#
# Content of the file as it is:
# John,john@example,1234567890
# Jane,jane@example,1234567891
#
# Content of the file as address book:
# Name  : John
# Email : john@example
# Phone : 1234567890
# Name  : Jane
# Email : jane@example
# Phone : 1234567891

# Open the file in write mode using with statement
with 

    while True:

        # Get the name, email, phone of the person
        name = input("Enter the name of the person: ")
        email = input("Enter the email of the person: ")
        phone = input("Enter the phone number of the person: ")

        # Write the name, email and phone number separated by a comma to the file
        

        # Ask the user if he/she wants to add another person
        choice = input("Do you want to add another person (y/n): ")

        # If the user enters n, then break the loop
        if choice == "n":
            break

        print()

# Open the file in read mode using with statement
with 

    # Read the entire content of the file and strip the trailing whitespaces
    content = 
    print("Content of the file as it is:")
    print(
    print()

    print("Content of the file as address book:")
    # Split the content of the file by newline character
    for entry in content.spl
        # Split the entry by comma
        data = 
        # Display the name, email and phone number
        print("Name  : " + 
        print("Email : " + 
        print("Phone : " + 
        print()
