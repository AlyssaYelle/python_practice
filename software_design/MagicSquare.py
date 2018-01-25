'''
  File: MagicSquare.py

  Description: 
  Given an odd integer n, we create an nxn grid such that the grid contains all integers from 1 to n^2
  For all rows, columns, and the two main diagonals, the sum of the elements should be equal


  Student's Name: Alyssa Jones

  Student's UT EID: adj484

  Course Name: CS 313E 

  Unique Number: 

  Date Created: 23 January 2018

  Date Last Modified: 23 January 2018

'''
import numpy as np


# Populate a 2-D list with numbers from 1 to n2
def make_square (n):
  matrix = [[0 for x in range(n)] for y in range(n)] 
  # initialize starting location
  row = n-1
  col = n//2
  matrix[row][col] = 1

  #we move +1 col, -1 row
  #if out of col xor row range we go to [0]
  #if col AND row are out of range or the space is already occupied, we place number +1 row
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

  square = np.array(matrix)
  return square




# Print the magic square in a neat format where the numbers
# are right justified
def print_square ( magic_square ):
  for row in magic_square:
    print ' '.join('%04s' % i for i in row)

# Check that the 2-D list generated is indeed a magic square
def check_square ( magic_square, n ):
  #canonical_sum is the expected output for the sum of rows, etc
  canonical_sum = n*(n**2 + 1)/2

  #returns array of row sums, col sums
  sum_rows = magic_square.sum(axis=1)
  sum_cols = magic_square.sum(axis=0)

  #find the diagonal sums
  x = 1
  for elt in sum_rows:
    if elt != canonical_sum:
      x = 0
      break
    else:
      for elt in sum_cols:
        if elt != canonical_sum:
          x = 0
          break


  
  if x == 0:
    return 'Your magic square fails'
  else:
    return canonical_sum




def main():
  # Prompt the user to enter an odd number 3 or greater
  while True:
    n = int(raw_input("Please input an odd integer 3 or greater: "))

    #Check the user input
    if n%2 == 1 and n >= 3:
      break
  

  # Create the magic square 
  magic_square = make_square(n)

  #check square
  canonical_sum = check_square(magic_square, n)
  

  # Print the magic square
  print 'Here is a', n, 'by', n, 'magic square:'
  print_square(magic_square)
  # Retrieve vector of the sum of each row/col
  print 'Sum of row =', canonical_sum, '\nSum of column =', canonical_sum, '\nSum of diagonal (UL to LR) =', canonical_sum, '\nSum of diagonal (UR to LL) =', canonical_sum

main()



















