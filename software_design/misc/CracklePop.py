'''

Written & tested in Python 3.7 by Alyssa Jones

Write a program that prints out the numbers 1 to 100 (inclusive).
If the number is divisible by 3, print Crackle instead of the number.
If it's divisible by 5, print Pop.
If it's divisible by both 3 and 5, print CracklePop.

'''


def crackle_pop(min, max):

	# loop over values from min to max
	for i in range(min, max + 1):

		# set value to CracklePop if divisible by 3 & 5
		if (i % 3 == 0) & (i % 5 == 0):
			out = "CracklePop"
		# if value is exclusively divisible by 3 or 5
		# set value to Crackle (if div. by 3) or Pop (if div. by 5)
		elif (i % 3 == 0) ^ (i % 5 == 0):
			out = "Crackle" if (i % 3 == 0) else "Pop"
		# otherwise value stays same
		else:
			out = i

		# print out updated value
		print(out)

if __name__ == "__main__":

	# call crackle_pop function for range (1, 100)
	crackle_pop(1, 100)