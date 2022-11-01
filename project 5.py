# Alejandro Porrata
# CMSC 210 C91
# Project 4

import sys
# take arguments
numRows = int(sys.argv[1])
# check for the input is not less than 1
if numRows < 1:
    print("Invalid input value. The number of rows cannot be less than 1.")
# input is greater than 20
elif numRows > 20:
    print("Invalid input value. The number of rows cannot be more than 20")    
# if input is between 1-20
else:
    starCount = 0
    k = numRows - 1
# loop for column
    for x in range(0, numRows):
# loop print the number of space
        for y in range(0, numRows-x-1):
            print(end=" ")
# decrementing k after each loop
            k = k - 1
# loop to print the star
        for y in range(0, x+1):
            print("* ", end="")
            starCount = starCount+1

        print()

# print the number of stars
    print(starCount)
    


