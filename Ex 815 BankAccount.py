# BankAccount Class
# Author: Amandeep Patti

# ToDo:
# 1. Create a BankAccount class with the following properties:
#   - account_number
#   - account_holder
#   - balance
# 2. Create a constructor that initializes the properties
# 3. Create a method called deposit that takes in an amount as a parameter
#    and adds it to the balance
# 4. Create a method called withdraw that takes in an amount as a parameter
#    and subtracts it from the balance
# 5. Create a method called display_balance that displays the account number,
#    account holder and balance
# 6. Create a main function that does the following:
#   - Create a BankAccount object with the following information:
#       Account Number: 123456789
#       Account Holder: Amandeep Patti
#       Balance: 1000
#   - Using a loop, prompt the user which banking operation to perform
#   - Display a menu with the following options:
#       1. Deposit
#       2. Withdraw
#       3. Display Balance
#       0. Exit
#   - Based on the user input, perform the operation
#   - If the user enters 0, exit the loop
#   - If the user enters an invalid choice, display "Invalid choice"

# Sample Output:
# What operation would you like to perform?
# 1. Deposit
# 2. Withdraw
# 3. Display Balance
# 0. Exit
# Enter your choice: 1
# Enter the amount to deposit: 500
# What operation would you like to perform?
# 1. Deposit
# 2. Withdraw
# 3. Display Balance
# 0. Exit
# Enter your choice: 3
# Account Number: 123456789
# Account Holder: Amandeep Patti
# Balance: 1500
# What operation would you like to perform?
# 1. Deposit
# 2. Withdraw
# 3. Display Balance
# 0. Exit
# Enter your choice: 2
# Enter the amount to withdraw: 2000
# Insufficient funds
# What operation would you like to perform?
# 1. Deposit
# 2. Withdraw
# 3. Display Balance
# 0. Exit
# Enter your choice: 2
# Enter the amount to withdraw: 500
# What operation would you like to perform?
# 1. Deposit
# 2. Withdraw
# 3. Display Balance
# 0. Exit
# Enter your choice: 3
# Account Number: 123456789
# Account Holder: Amandeep Patti
# Balance: 1000
# What operation would you like to perform?
# 1. Deposit
# 2. Withdraw
# 3. Display Balance
# 0. Exit
# Enter your choice: 0


# Define a class called BankAccount to represent a bank account

    # Initialize the BankAccount object with
    # a given account number, account holder and balance



    # Deposit amount to the bank account
    # Add a method called deposit
    # that takes in an amount as a parameter
    # if the amount is greater than or equal to 0 add it to the balance
    # otherwise print "Invalid amount"



    # Withdraw amount from the bank account
    # Add a method called withdraw
    # that takes in an amount as a parameter
    # if the amount is greater than 0 and less than the balance
    # subtract it from the balance
    # otherwise print "Insufficient funds" if the amount is greater than the balance
    # otherwise print "Invalid amount" if the amount is less than or equal to 0



    # display the account information
    # Add a method called display_balance
    # that displays the account number, account holder and balance



# define main function and test the BankAccount class
def main():
    # Create a BankAccount object with the following information:
    # Account Number: 123456789
    # Account Holder: Amandeep Patti
    # Balance: 1000

    

    # Using a loop, prompt the user which banking operation to perform
    # Display a menu with the following options:
    # 1. Deposit
    # 2. Withdraw
    # 3. Display Balance
    # 0. Exit
    # Based on the user input, perform the operation
    # Note: Use match case to perform the operation based on the user input
    # If the user enters 0, exit the loop
    # If the user enters an invalid choice, display "Invalid choice"
    while True:

        print("\n\nWhat operation would you like to perform?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                amount = float(input("Enter the amount to deposit: "))
                
                
            case 2:
                amount = float(input("Enter the amount to withdraw: "))
                

            case 3:
                
            case 0:
                break
            case _:
                print("Invalid choice")


# call main function
main()
