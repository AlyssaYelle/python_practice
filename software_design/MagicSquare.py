'''
PYTHON 2.7

  Given an odd integer n, we create an nxn grid such that 
  the grid contains all integers from 1 to n^2
  For all rows, columns, and the two main diagonals, 
  the sum of the elements should be equal

'''
import numpy as np


# Populate a 2-D array with numbers from 1 to n^2
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
#%03s also works for the purpose of this assignment but 4 is more versatile
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
  col_index = 0
  row_index = 0
  ULLR_sum = 0
  #sum UL to LR
  for i in range (0,n):
    ULLR_sum += magic_square[row_index][col_index]
    row_index +=1
    col_index +=1
  #sum UR to LL
  col_index = n-1
  row_index = 0
  URLL_sum = 0
  for i in range (0,n):
    URLL_sum += magic_square[row_index][col_index]
    row_index += 1
    col_index -= 1


  #check conditions

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

  if ULLR_sum != canonical_sum or URLL_sum != canonical_sum:
    x = 0
  else:
    pass


  #report back if the square fails
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



















