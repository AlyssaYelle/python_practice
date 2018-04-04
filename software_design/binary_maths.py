'''
(PYTHON 3)
This program acts as a calculator that can only use the {+ - * /} operators
so we have to use binary search to find the nth root of a number.
Saving so I can add functionality to it as I get more free time
'''

class ImproperMathTimeError(Exception):
	def __init__(self,value):
		self.value = value

class ImproperMathTypeError(Exception):
	def __init__(self, value):
		self.value = value

class ImproperValues(Exception):
	def __init__(self, value):
		self.value = value


def which_math():
	math_type = str(raw_input('Please select the type of math problem you want to solve:\nnth root\nlogn\n'))
	if math_type != 'nth root' and math_type != logn:
		raise ImproperMathTypeError('Not an accepted math type')
	else:
		do_math(math_type)

def do_math(math_type):
	if math_type == 'nth root':
		num = float(raw_input('Select a positive number to compute the nth root of: '))
		n = int(raw_input('Now choose an n: '))
		hi = num
		lo = 1
		nth_root(num, n, hi, lo)
	if math_type == 'logn'
		n = float(raw_input('Please select a positive number to compute the log of: '))
		base = int(raw_input('Select an integer for the base: '))
		logn(n, base)


def nth_root(num,n,hi,lo):
	epsilon = .00000001
	mid = float((hi+lo)/2)
	value = mid
	root = n
	while root > 1:
		value = value*mid
		root -= 1

	if (abs(value - num) < epsilon):
		print 'The answer is', mid
	else:
		if value < num:
			lo = mid
			return nth_root(num, n, hi, lo)
		if value > num:
			hi = mid
			return nth_root(num, n, hi, lo)


def logn(n, base):
	pass



def main():

	math_time = raw_input('Would you like to solve a math problem? (y/n)\n')
	if math_time == 'n' or math_time == 'N':
		print 'Okay, bye!'
	elif math_time == 'y' or math_time== 'Y':
		which_math()
	else:
		raise ImproperMathTimeError('Accepted values are: y or n')


if __name__ == '__main__':
	main()





























