'''
  File: MagicSquare.py

  Description: 
  Given an odd integer n, we create and nxn grid such that grid contains all integers from 1 to n^2
  For all rows, columns, and the two main diagonals, the sum of the elements should be equal


  Student's Name: Alyssa Jones

  Student's UT EID: adj484

  Course Name: CS 313E 

  Unique Number: 

  Date Created: 23 January 2018

  Date Last Modified: 23 January 2018

'''


import math


# Populate a 2-D list with numbers from 1 to n2
def make_square (n):
  matrix = [[0 for x in range(n)] for y in range(n)] 
  # initialize starting location
  row = n-1
  col = n//2
  matrix[row][col] = 1
  for i in range (2, n**2+1):
    if (row+1) >= n and (col+1) >=n:
      row -= 1
    elif (row+1) == n:
      row = 0
      col +=1
    elif (col +1) == n:
      col = 0
      row += 1
    else:
      row += 1
      col += 1

    if matrix[row][col] == 0:
      matrix[row][col] = i
    else:
      row -=2
      col -=1
      matrix[row][col] = i

  return matrix



'''
# Print the magic square in a neat format where the numbers
# are right justified
def print_square ( magic_square ):

# Check that the 2-D list generated is indeed a magic square
def check_square ( magic_square ):
'''

def main():
  # Prompt the user to enter an odd number 3 or greater
  while True:
    n = int(raw_input("Please input an odd integer 3 or greater: "))

    #Check the user input
    if n%2 == 1 and n >= 3:
      print n
      break
  

  # Create the magic square
  
  magic_square = make_square(n)




  # Print the magic square
  for row in magic_square:
    print row 
  # Verify that it is a magic square

main()



















