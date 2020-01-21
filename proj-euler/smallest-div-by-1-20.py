'''
find the smallest positive integer that is divisible by all integers between 1 & 20, inclusive
'''

def isPrime(my_int):

	if my_int == 2:
		return True
	# other even nums are not prime
	elif my_int % 2 == 0:
		return False

	for i in range(3, my_int // 2):
		if my_int % i == 0:
			return False

	return True

if __name__ == "__main__":

	# checking isPrime fn, will be deleted later
	for i in range(2, 21):
		result = isPrime(i)
		print(i, ": ", result)