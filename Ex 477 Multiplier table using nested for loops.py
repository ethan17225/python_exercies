# Multiplier Table using nested for loops
# Author: Amandeep Patti
'''
     |   1   2   3   4   5   6   7   8   9  10
--------------------------------------------------
   5 |   5  10  15  20  25  30  35  40  45  50
   6 |   6  12  18  24  30  36  42  48  54  60
   7 |   7  14  21  28  35  42  49  56  63  70
   8 |   8  16  24  32  40  48  56  64  72  80
   9 |   9  18  27  36  45  54  63  72  81  90
--------------------------------------------------
'''

# get input for start and end
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# print a blank line
print()

# print the top header row
# starting with 5 spaces and a pipe symbol
# then the column heading numbers 1 to 10 using a for loop
# move to new line
print("     |", end="")
for m in range(1, 10 + 1):
    print(f"{m:4d}", end="")
print()

# print a line of dashes using a for loop and move to new line
for i in range(1, 51):
    print("-", end="")
print()

# print the table using nested for loops
# starting with the row heading numbers
# then the pipe symbol
# then the product of the row and column numbers

# outer loop for the row numbers

# print the row heading number

# inner loop for the column numbers as multipliers

# move to new line


# print a line of dashes using a for loop and move to new line
for i in range(1, 51):
    print("-", end="")
print()
