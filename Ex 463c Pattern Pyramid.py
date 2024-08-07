# Pattern  Pyramid
# using increasing numbers then decreasing numbers
# using nested for loops
# Author: Amandeep Patti
'''
    1
   121
  12321
 1234321
123454321 
'''
ROWS = 5

# Outer loop - rows
for row in range(1, ROWS + 1):

    # Inner loop - spaces - up to total rows-current row number

    # Print space and stay on same line

    # Inner loop - cols - increasing up current row number

    # Print col and stay on same line

    # Inner loop - cols - decreasing from current row-1 to 1

    # Print col and stay on same line

    # Print new line after each row
    print()
