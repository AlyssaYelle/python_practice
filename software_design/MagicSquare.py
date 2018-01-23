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

# Populate a 2-D list with numbers from 1 to n2
def make_square (n):
  Matrix = [[0 for x in range(n)] for y in range(n)] 
  return Matrix


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
  print make_square(n)




  # Print the magic square

  # Verify that it is a magic square

main()



















