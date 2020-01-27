'''

written & tested in Python 3.7 by Alyssa Jones

problem: find the smallest positive integer that is divisible by all integers between 1 & 20, inclusive

algo:

FOR each integer (int) between 2 & 20 (inclusive)
	IF (int) is prime
		power n = 1, ...
		raise it by one power and append (int) to list again while (int)^n <= 20

MULTIPLY primes in prime list together to get minimum integer divisible by all in [1, ..., 20]

'''
import math

def isPrime(my_int):

	if my_int == 2:
		return True
	# other even nums are not prime
	elif my_int % 2 == 0:
		return False

	# if my_int mod any other integer is 0 then it is not prime
	for i in range(3, my_int // 2):
		if my_int % i == 0:
			return False

	# if we get to this point, my_int must be prime
	return True

# UNNECESSARY FOR THIS PROBLEM
def primeFactorization(my_int):

	# if int is prime return just the int
	if isPrime(my_int) == True:
		return [my_int]

	# empty list to store prime factorization
	prime_factorization = []

	# begin checking if 2 & my_int // 2 are factors
	int1 = 2
	int2 = math.floor(my_int // 2)

	found_factors = False

	# check if int1 * int2 = my_int until success
	while (int1 <= int2) & (found_factors == False):

		if int1 * int2 == my_int:
			found_factors = True
			factors = [int1, int2]

			# recursively find prime factorization of the found factors
			for factor in factors:
				if isPrime(factor) == True:
					prime_factorization.append(factor)
				else:
					sub_factors = primeFactorization(factor)

					for factor in sub_factors:
						prime_factorization.append(factor)

		# increment up int1 (if it is not a factor of my_int) and increment down int2 (if it is not a factor of my_int)
		else:
			if my_int % int1 == 0:
				int2 -= 1
			elif my_int % int2 == 0:
				int1 += 1
			else:
				int1 += 1
				int2 -= 1

	# return list of prime
	return prime_factorization

def get_minimum_primes(max):
	primes = []

	for i in range(2, max + 1):
		if isPrime(i) == True:
			pow = 1
			while (i**pow) <= max:
				primes.append(i)
				pow += 1

	return primes

def compute_smallest_div_integer(max):
	primes = get_minimum_primes(max)

	product = 1

	for prime in primes:
		product *= prime

	return product

if __name__ == "__main__":

	min_int = compute_smallest_div_integer(20)
	print(min_int)





