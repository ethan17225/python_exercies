# Stack with Exceptions Class
# Author: Amandeep Patti


# Objective(s):
# 1. Create a Queue class with the following properties:
#   - items
# 2. Create a constructor that initializes the items property to an empty list
# 3. Create a method called enqueue that takes in an item and adds it to the end of the list
# 4. Create a method called dequeue that removes and returns the first item from the list
# 5. Create a method called is_empty that returns True if the queue is empty, False otherwise
# 6. Create a method called size that returns the number of items in the queue
# 7. Create a method called peek that returns the first item from the list
# 8. Create a main function that does the following:
#   - Create a Queue object
#   - Prompt the user to input few items and enqueue those onto the queue
#   - Dequeue an item from the queue and display it
#   - Peek at the front item of the queue and display it
#   - Display the number of items in the queue
#   - Check if the queue is empty and display the result

# Sample Output:
#   What Operation Would You Like to Perform on Queue?
#       1. Enqueue an item onto the queue
#       2. Dequeue an item from the queue
#       3. Peek at the front item of the queue
#       4. Display the number of items in the queue
#       5. Check if the queue is empty
#       0. Quit
# Enter your choice: 1
# Enter an item to enqueue: Item1

# Enter your choice: 1
# Enter an item to enqueue: Item2

# Enter your choice: 1
# Enter an item to enqueue: Item3

# Enter your choice: 2
# The item dequeued from the queue is: Item1

# Enter your choice: 3
# The item peeked from the queue is: Item2

# Enter your choice: 4
# The number of items in the queue is: 2

# Enter your choice: 5
# Is the queue empty? False

# Enter your choice: 2
# The item dequeued from the queue is: Item2

# Enter your choice: 2
# The item dequeued from the queue is: Item3

# Enter your choice: 5
# Is the queue empty? True

# Enter your choice: 2
# Cannot dequeue from an empty queue.

# Enter your choice: 3
# Cannot peek in an empty queue.

# Enter your choice: 0
# Goodbye!

'''
+-------------------------------------+
|               Queue                 |
+-------------------------------------+
| - items: List                       |
+-------------------------------------+
| + __init__()                        |
| + enqueue(item: Any)                |
| + dequeue() -> Any                  |
| + is_empty() -> bool                |
| + size() -> int                     |
| + peek() -> Any                     |
+-------------------------------------+
'''

# Define a class called Queue to implement a queue data structure


    # Initialize the queue with an empty list to store items



    # Enqueue (add) an item to the back of the queue
    # The item is added to the end of the list
    # def method enqueue that takes in an item and adds it to the end of the list



    # Dequeue (remove and return) an item from the front of queue
    # The item is removed from the beginning of the list
    # def method dequeue that removes and returns the first item from the list
    # Raise an exception if the queue is empty



    # Check if the queue is empty
    # def method is_empty that returns True if the queue is empty, False otherwise



    # Get the number of items in the queue
    # def method size that returns the number of items in the queue



    # Peek at the front item of the queue without removing it
    # def method peek that returns the first item from the list
    # Raise an exception if the queue is empty





# define main function and test the Queue class
def main():
    # Create a queue object
    my_queue = 

    # Perform operations on the queue based on user input in a loop
    # The loop will break when the user enters 'quit'
    while True:
        print("\tWhat Operation Would You Like to Perform on Queue?")
        print("\t\t1. Enqueue an item onto the queue")
        print("\t\t2. Dequeue an item from the queue")
        print("\t\t3. Peek at the front item of the queue")
        print("\t\t4. Display the number of items in the queue")
        print("\t\t5. Check if the queue is empty")
        print("\t\t0. Quit")

        # Prompt the user to input a choice
        choice = int(input("Enter your choice: "))
        print()

        # Check if the user wants to quit
        if choice == 0:
            break

        # Perform the operation based on the user choice
        # Handle exceptions raised from queue class
        try:

            match choice:

                case 1:  # Enqueue
                    # Prompt the user to input an item to enqueue


                    # Enqueue the item onto the queue


                case 2:  # Dequeue
                    # Dequeue an item from the queue


                    # Display the item that was dequeued


                case 3:  # Peek
                    # Peek at the front item of the queue


                    # Display the item that was peeked


                case 4:  # Size
                    # Display the number of items in the queue


                case 5:  # Is Empty
                    # Check if the queue is empty


                case _:  # Invalid choice
                    # Raise an exception if the user enters an invalid choice


        # Handle exceptions raised from queue class


        # if no exception is raised, print success message


        # print a line after each operation,
        # regardless of success or failure



    print("Goodbye!")


# call main function
main()
