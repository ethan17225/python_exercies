# Testing 3-digit Arm strong Number using while loop
# Author: Amandeep Patti

# A 3-digit armstrong number is a number
# that is equal to the sum of cubes of it's digits.
# For example, 153 is an armstrong number
# because 153 = 1^3 + 5^3 + 3^3

# get input from user and store it in num
num = int(input("Enter a 3-digit integer number : "))

# initialize sum to 0 to store sum of digit cubes
sum = 0

# make a copy of num and store it in temp
temp = num

# loop until temp is greater than 0
while (temp > 0):

    # add cube of last digit to sum
    

    # update temp by removing last digit
    

# print whether num is an arm strong or not
if (sum == num):
    print(f"{num} is an arm strong")
else:
    print(f"{num} is not an arm strong")
