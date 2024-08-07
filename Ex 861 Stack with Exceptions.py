# Stack with Exceptions Class
# Author: Amandeep Patti

# Objective(s):
# 1. Create a Stack class with the following properties:
#   - items
# 2. Create a constructor that initializes the items property to an empty list
# 3. Create a method called push that takes in an item and adds it to the end of the list
# 4. Create a method called pop that removes and returns the last item from the list
# 5. Create a method called is_empty that returns True if the stack is empty, False otherwise
# 6. Create a method called size that returns the number of items in the stack
# 7. Create a method called peek that returns the last item from the list
# 8. Create a main function that does the following:
#   - Create a Stack object
#   - Prompt the user to input few items and push those onto the stack
#   - Pop an item from the stack and display it
#   - Peek at the top item of the stack and display it
#   - Display the number of items in the stack
#   - Check if the stack is empty and display the result

# Sample Output:
#   What Operation Would You Like to Perform on Stack?
#       1. Push an item onto the stack
#       2. Pop an item from the stack
#       3. Peek at the top item of the stack
#       4. Display the number of items in the stack
#       5. Check if the stack is empty
#       0. Quit
# Enter your choice: 1
# Enter an item to push onto the stack: Item1

# Enter your choice: 1
# Enter an item to push onto the stack: Item2

# Enter your choice: 1
# Enter an item to push onto the stack: Item3

# Enter your choice: 2
# The item popped from the stack is: Item3

# Enter your choice: 3
# The item peeked from the stack is: Item2

# Enter your choice: 4
# The number of items in the stack is: 2

# Enter your choice: 5
# Is the stack empty? False

# Enter your choice: 2
# The item popped from the stack is: Item2

# Enter your choice: 2
# The item popped from the stack is: Item1

# Enter your choice: 5
# Is the stack empty? True

# Enter your choice: 2
# Cannot pop from an empty stack.

# Enter your choice: 3
# Cannot peek in an empty stack.

# Enter your choice: 0
# Goodbye!


'''
+--------------------------------+
|           Stack                |
+--------------------------------+
| - items: list                  |
+--------------------------------+
| + __init__()                   |
| + push(item: Any)              |
| + pop() -> Any                 |
| + is_empty() -> bool           |
| + size() -> int                |
| + peek() -> Any                |
+--------------------------------+
'''

# Define a class called Stack to implement a stack data structure



    # Initialize the stack with an empty list to store items



    # Push an item onto the stack
    # The item is added to the end of the list
    # def method push that takes in an item and adds it to the end of the list



    # Pop (remove and return) an item from the top of stack
    # The item is removed from the end of the list
    # def method pop that removes and returns the last item from the list
    # Raise an exception if the stack is empty
    
        if self.is_empty():
            raise Exception("Cannot pop from an empty stack.")


    # Check if the stack is empty
    # def method is_empty that returns True if the stack is empty, False otherwise



    # Get the number of items in the stack
    # def method size that returns the number of items in the stack
 
 

    # Peek at the top item of the stack without removing it
    # def method peek that returns the last item from the list
    # Raise an exception if the stack is empty
    
        

        


# define main function and test the Stack class
def main():
    # Create a stack object
    my_stack = 

    # Perform operations on the stack based on user input in a loop
    # The loop will break when the user enters 'quit'
    while True:
        print("\tWhat Operation Would You Like to Perform on Stack?")
        print("\t\t1. Push an item onto the stack")
        print("\t\t2. Pop an item from the stack")
        print("\t\t3. Peek at the top item of the stack")
        print("\t\t4. Display the number of items in the stack")
        print("\t\t5. Check if the stack is empty")
        print("\t\t0. Quit")

        # Prompt the user to input a choice
        choice = int(input("Enter your choice: "))
        print()

        # Check if the user wants to quit
        

        # Perform the operation based on the user choice
        # Handle exceptions raised from stack class
        try:

            match choice:

                case 1:  # Push
                    # Prompt the user to input an item to push onto the stack
                    

                    # Push the item onto the stack
                    

                case 2:  # Pop
                    # Pop an item from the stack
                    

                    # Display the item that was popped
                    

                case 3:  # Peek
                    # Peek at the top item of the stack
                    

                    # Display the item that was peeked
                    

                case 4:  # Size
                    # Display the number of items in the stack
                    

                case 5:  # Is Empty
                    # Check if the stack is empty
                    

                case _:  # Invalid choice
                    # Raise an exception if the user enters an invalid choice
                    raise Exception("Invalid choice. Try again.")

        # Handle exceptions raised from stack class
        except Exception as ex:
            print(ex)

        # if no exception is raised, print success message
        else:
            print("Operation performed successfully.")

        # print a line after each operation,
        # regardless of success or failure
        finally:
            print("-" * 30)

    print("Goodbye!")


# call main function
main()
