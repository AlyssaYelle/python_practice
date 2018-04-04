'''
We take in as input a text file which represents a triangle
for example
3
1
2 3 
4 5 6
where the top integer is the number of rows the triangle contains
we want to compute the maximum path sum.
Here we use four different algorithms 
(exhaustive search, greedy, divide and conquer, and dynamic)
'''


import time
global max_sum_list
max_sum_list = []

# returns the greatest path sum using exhaustive search
def exhaustive_search(grid):
	exhaustive(grid,0,0,0)
	max_sum = max(max_sum_list)
	return max_sum

# helper function traverses through triangle to find all possible sums
def exhaustive(grid,idx1,idx2,temp):
	# base case
	if len(grid[idx1]) == len(grid):
		temp += grid[idx1][idx2]
		global variable
		max_sum_list.append(temp)
	else:
		exhaustive(grid, idx1 + 1, idx2, temp + grid[idx1][idx2])
		exhaustive(grid, idx1 + 1, idx2 + 1, temp + grid[idx1][idx2])




# returns the greatest path sum using greedy approach
# starting from top value it looks at the two possible choices
# and sums the best of those two choices
# then go to that position and repeat
def greedy(grid):
	sum = int(grid[0][0])
	line = 0
	index = 0
	for i in range(0, len(grid)-1):
		line += 1
		path1 = int(grid[line][index])
		path2 = int(grid[line][index+1])
		if path1 >= path2:
			sum += path1
		else:
			sum += path2
			index += 1
		
	return sum


# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search(grid):
	max_sum = conquer(grid, 0, 0)
	return max_sum



# returns the greatest path sum using dynamic programming
# for each value at bottom row of triangle moves upward in best manner
# at top of triangle returns max sum
def dynamic_prog(grid):
	row = len(grid)-2
	while row >= 0:
		index = 0
		for i in range(len(grid[row])):
			if int(grid[row+1][index]) >= int(grid[row+1][index+1]):
				grid[row][index] = int(grid[row][index]) + int(grid[row+1][index])
			else:
				grid[row][index] = int(grid[row][index]) + int(grid[row+1][index+1])
			index+=1
		row -=1
	max_sum = grid[0][0]
	return(grid, max_sum)
	#print('The greatest path sum through dynamic programming approach is', max_sum)



# here are some helper functions

# this does the dividing and conquering of the divide/conquer approach
def conquer(grid, row, col):
	if row == (len(grid)-1):
		return grid[row][col]
	else:
		return grid[row][col] + max(conquer(grid, row+1, col), conquer(grid,row+1, col+1))




# reads the file and returns a 2-D list that represents a triangle
def read_file():
	in_file = open('triangle.txt', 'r')

	# first line gives us the total number of boxes
	line = in_file.readline()
	line = line.strip()
	num_lines = int(line)

	# here we are reading in the list of boxes and sorting them by size
	grid = []
	for i in range(num_lines):
		line = in_file.readline()
		line = line.strip()
		nums = line.split()
		for i in range(len(nums)):
			nums[i] = int(nums[i])
		grid.append(nums)

	in_file.close()
	return grid


def main():
	# read triangular grid from file
	grid = read_file()

	ti = time.time()
	j = exhaustive_search(grid)
	print('The greatest path sum through exhaustive search approach is', j)
	tf = time.time()
	del_t = tf - ti
	print('The time taken for exhaustive search approach is', del_t, 'seconds.\n')

	ti = time.time()
	j = greedy(grid)
	print('The greatest path sum through greedy approach is', j)
	tf = time.time()
	del_t = tf - ti
	print('The time taken for greedy approach is', del_t, 'seconds.\n')

	ti = time.time()
	j = rec_search(grid)
	print('The greatest path sum through divide and conquer approach is', j)
	tf = time.time()
	del_t = tf -ti
	print('The time taken for divide and conquer approach is', del_t, 'seconds.\n')

	ti = time.time()
	j = dynamic_prog(grid)
	print('The greatest path sum through dynamic programming approach is', j[1])
	tf = time.time()
	del_t = tf - ti
	print('The time taken for dynamic programming approach is', del_t, 'seconds.\n')



if __name__ == '__main__':
	main()
























