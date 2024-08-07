# File Content as Collection
# Author : Amandeep Patti

# Objective(s):
# 1. Read the content of a file
# 2. Write the content of a file
# 3. Use with statement to open a file
# 4. Processing the content of a file as collection
# 5. Splitting the content of a file
# 6. Splitting the content of a file line by line
# 7. Splitting the content of a file word by word

# Todo:
# 1. Create a file named "numbers.txt"
# 2. Generate few random numbers and save those to the file
# 3. Display the content of the file
# 4. Display the content of the file as collection
# 5. Display the content of the file line by line
# 6. Display the content of the file word by word
# Note: Use with statement to open a file

# Sample Output:
# Entire content of the file:
# 12 34 56 78 90
# 12 34 56 78 90
# 12 34 56 78 90
# 12 34 56 78 90
# 12 34 56 78 90
# Content as collection:
# ['12 34 56 78 90', '12 34 56 78 90', '12 34 56 78 90', '12 34 56 78 90', '12 34 56 78 90']
# Content of the file line by line:
# 12 34 56 78 90
# 12 34 56 78 90
# 12 34 56 78 90
# 12 34 56 78 90
# 12 34 56 78 90
# Content of the file word by word
# 12
# 34
# 56
# ....
# 78
# 90


# Importing random module


# Open the file in write mode using with statement
with 

    # Generating random numbers and saving them to the file
    # Use nested for loops to generate 5 lines of 5 random numbers
    # and save those to the file
    # The random numbers should be in the range of 11 to 99
    # Numbers must be separated by a space
    # After each line, a new line character must be added
    for r in 

        for c 
            # Write the random number to the file and add a space
            

        # Add a new line character after each line
        

# Open the file in read mode using with statement
with 

    # Read the content of the file
    content = 

    print("Entire content of the file: ")
    # Display the content of the file
    print(content)

    print("Content as collection: ")
    # Split the content of the file and display it
    print(

    print("Content of the file line by line: ")
    # Split the content as lines and display line by line
    for line 
        print(

    print("Content of the file word by word")
    # Split the content as lines and process line by line
    for line 

        # Split the line as words and process word by word
        for word 
            print(
