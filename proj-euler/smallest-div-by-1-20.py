'''

written & tested in Python 3.7 by Alyssa Jones

problem: find the smallest positive integer that is divisible by all integers between 1 & 20, inclusive

'''

import math

def get_primes(stopping_point):

	primes = []

	for i in range(2, stopping_point + 1):

		maybePrime = True

		for prime in primes:
			if i % prime == 0:
				maybePrime = False
				break 

		if maybePrime:
			power = 1

			while i**power <= stopping_point:
				primes.append(i)
				power += 1

	return primes




def compute_smallest_div_integer(max):
	if max < 1:
		raise ValueError

	primes = get_primes(max)

	product = 1

	for prime in primes:
		product *= prime

	return product

if __name__ == "__main__":


	product = compute_smallest_div_integer(20)
	print(product)





