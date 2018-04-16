'''
PYTHON 3
This program takes in as input a text file of the form
number_of_boxes
length width height # of box 1
.
.
.
length width height # of box n
and then computes the largest subset of nesting boxes
we assume that the boxes can be rotated
and must be strictly smaller than the outer box in order to fit inside
it prints out all nestings
'''


global potential_box_nests
potential_box_nests = []


# Combination function
def combine(a,b,lo,size):
	hi = len(a)
	if (lo == hi):
		if (len(b) == size):
			potential_box_nests.append(b)
		return
	if (len(b) == size):
		potential_box_nests.append(b)
	else:
		c = b[:]
		b.append(a[lo])
		combine(a,b,lo+1,size)
		combine(a,c,lo+1,size)


# this function does a binary-search style call for combinations of size n
# if it does not find a nesting, it recomputes the midpoint and tries again
# it it does find a valid nesting, it recomputes to a higher midpoint to see if larger nestings exist
# we quit re-calling the function when there are no higher order nestings
# initially hi should be num_boxes, lo = 0, mid = num_boxes//2
def search_for_nesting(box_list, hi, mid, lo):
	# initialize list in which we will add sucessful box nestings
	actual_box_nests = []
	b = []

	# generate all possible sets of size (mid)
	combine(box_list, b, 0, mid)

	# search for a nesting and append to list of valid nestings
	for box_set in potential_box_nests:
		if nesting_set(box_set):
			actual_box_nests.append(box_set)


	# reset parameters according to our findings
	if (len(actual_box_nests) >=1):
		lo = mid
		mid = mid + (hi-lo)//2
	elif (len(actual_box_nests) == 0):
		hi = mid
		mid = lo + (hi-lo)//2

	# once we have found the largest set(s) of nestings we print it out
	if (mid == lo) or (mid==hi):
		print('Largest Subset of Nesting Boxes')
		for box_set in actual_box_nests:
			if (len(box_set)==mid):
				for box in box_set:
					print(box)
				print('\n')
	else:
		# re-run function with new parameters
		return search_for_nesting(box_list,hi,mid,lo)
	

# Function to test if a box does indeed nest within another box
def does_nest(box1, box2):
	for i in range(0,3):
		if (box1[i] >= box2[i]):
			return False
	return True

# Function to test if all boxes in set nest
def nesting_set(boxes):
	boxes.sort()
	for i in range(len(boxes)-1):
		if not does_nest(boxes[i],boxes[i+1]):
			return False
	return True



def main():
	in_file = open('./text_files/boxes.txt', 'r')

	# first line gives us the total number of boxes
	line = in_file.readline()
	line = line.strip()
	num_boxes = int(line)

	# here we are reading in the list of boxes and sorting them by size
	box_list = []
	for i in range(num_boxes):
		line = in_file.readline()
		line = line.strip()
		box = line.split()
		for i in range(len(box)):
			box[i] = int(box[i])
		box.sort()
		box_list.append(box)

	in_file.close()
	box_list.sort()
	
	# now we will search for nestings
	search_for_nesting(box_list, num_boxes, num_boxes//2,0)
	
	


main()



