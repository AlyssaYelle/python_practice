# Given n of 1 or more, return the factorial of n, 
# which is n * (n-1) * (n-2) ... 1.
# Compute the result recursively (without loops). 
def factorial(n):
	if (n==0):
		return 1
	else:
		return n*factorial(n-1)


# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies 
# recursively (without loops or multiplication).
def bunnyEars(bunnies):
	if (bunnies == 1):
		return 2
	else:
		return 2 + bunnyEars(bunnies-1)

# The fibonacci sequence is a famous bit of mathematics, and it happens 
# to have a recursive definition. The first two values in the sequence 
# are 0 and 1 (essentially 2 base cases). Each subsequent value is the 
# sum of the previous two values, so the whole sequence is: 
# 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on.
# Define a recursive fibonacci(n) method that returns the nth fibonacci 
# number, with n=0 representing the start of the sequence.
def fibonacci(n):
	if (n == 0):
		return 0
	elif (n == 1):
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

# We have bunnies standing in a line, numbered 1, 2, ...
# The odd bunnies (1, 3, ..) have the normal 2 ears.
# The even bunnies (2, 4, ..) we'll say have 3 ears, because they each 
# have a raised foot. Recursively return the number of "ears" in the 
# bunny line 1, 2, ... n (without loops or multiplication).
def bunnyEars2(bunnies):
	if (bunnies == 1):
		return 2
	elif (bunnies%2 ==0):
		return 3 + bunnyEars2(bunnies-1)
	else:
		return 2 + bunnyEars2(bunnies-1)

# We have triangle made of blocks. The topmost row has 1 block, the 
# next row down has 2 blocks, the next row has 3 blocks, and so on.
# Compute recursively (no loops or multiplication) the total number of 
# blocks in such a triangle with the given number of rows. 
def triangle(rows):
	if (rows == 1):
		return 1
	else:
		return rows + triangle(rows-1)

# Given a non-negative int n, return the sum of its digits recursively 
# (no loops). Note that mod (%) by 10 yields the rightmost digit 
# (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit 
# (126 / 10 is 12).
def sumDigits(n):
	if (n//10 == 0):
		return n
	else:
		return n%10 + sumDigits(n//10)

# Given a non-negative int n, return the count of the occurrences of 7 
# as a digit, so for example 717 yields 2. (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), 
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
def count7(n):
	if (n//10 == 0):
		if (n%10 == 7):
			return 1
		else:
			return 0
	else:
		if (n%10 == 7):
			return 1 + count7(n//10)
		else:
			return 0 + count7(n//10)

# Given a non-negative int n, compute recursively (no loops) the count 
# of the occurrences of 8 as a digit, except that an 8 with
# another 8 immediately to its left counts double, so 8818 yields 4. 
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
def count8(n):
	pass

# Given base and n that are both 1 or more, compute recursively (no loops) 
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
def powerN(base, n):
	if (n==0):
		return 1
	elif (n==1):
		return base
	else:
		return base*powerN(base,n-1)

# Given a string, compute recursively (no loops) the number of lowercase 
# 'x' chars in the string.
def countX(string):
	if (len(string) == 1):
		if (string[0] == 'x'):
			return 1
		else:
			return 0
	else:
		if (string[0] == 'x'):
			return 1 + countX(string[1:])
		else:
			return 0 + countX(string[1:])

# Given a string, compute recursively (no loops) the number of times 
# lowercase "hi" appears in the string.
def countHi(string):
	if (len(string)<2):
		return 0
	else:
		if (string[0] == 'h' and string[1] == 'i'):
			return 1 + countHi(string[2:])
		else:
			return 0 + countHi(string[1:])

# Given a string, compute recursively (no loops) a new string where all 
# appearances of "pi" have been replaced by "3.14".
def changePi(string):
	if (len(string) == 2):
		if (string[:] == 'pi'):
			return '3.14'
		else:
			return string
	else:
		if (string[:2] == 'pi'):
			return '3.14' + changePi(string[2:])
		else:
			return string[:2] + changePi(string[2:])

# Given a string, compute recursively a new string where all the 'x' 
# chars have been removed.
def noX(string):
	if (len(string)==1):
		if (string[0]=='x'):
			pass
		else:
			return string
	else:
		if (string[0] == 'x'):
			return noX(string[1:])
		else:
			return string[0] + noX(string[1:])

# Given an array of ints, compute recursively if the array contains a 6.
# We'll use the convention of considering only the part of the array that 
# begins at the given index. In this way, a recursive call can pass index+1 
# to move down the array. The initial call will pass in index as 0.
def array6(nums, index):
	if (index == len(nums)-1):
		if (nums[index]==6):
			return 'This array contains a 6'
		else:
			return 'This array does not contain a 6'
	else:
		if (nums[index] == 6):
			return 'This array contains a 6'
		else: return array6(nums, index+1)

# Given an array of ints, compute recursively the number of times that the 
# value 11 appears in the array. We'll use the convention of considering 
# only the part of the array that begins at the given index. In this way, 
# a recursive call can pass index+1 to move down the array. The initial 
# call will pass in index as 0. 
def array11(nums, index):
	if (index == len(nums)-1):
		if (nums[index] == 11):
			return 1
		else:
			return 0
	else:
		if (nums[index] == 11):
			return 1+ array11(nums, index+1)
		else:
			return 0 + array11(nums, index+1)

# Given an array of ints, compute recursively if the array contains 
# somewhere a value followed in the array by that value times 10. We'll 
# use the convention of considering only the part of the array that begins 
# at the given index. In this way, a recursive call can pass index+1 to 
# move down the array. The initial call will pass in index as 0.
def array220(nums, index):
	if (index == len(nums)-2):
		if (nums[index] == nums[index+1]//10):
			return 'This array contains a value immediately followed by value*10'
		else:
			return 'This array does not contain a value immediately followed by value*10'
	else:
		if (nums[index] == nums[index+1]//10):
			return 'This array contains a value immediately followed by value*10'
		else:
			return array220(nums, index+1)

# Given a string, compute recursively a new string where all the adjacent 
# chars are now separated by a "*".
def allStar(string):
	if (len(string)==1):
		return string
	else:
		return string[0] + '*' + allStar(string[1:])

# Given a string, compute recursively a new string where identical chars 
# that are adjacent in the original string are separated from each other 
# by a "*".
def pairStar(string):
	if (len(string)==1):
		return string
	elif (len(string)==2):
		if (string[0]==string[1]):
			return string[0] + '*' + string[1]
		else:
			return string
	else:
		if (string[0]==string[1]):
			return string[0] + '*' + pairStar(string[1:])
		else:
			return string[0] + pairStar(string[1:])

# Given a string, compute recursively a new string where all the lowercase 
# 'x' chars have been moved to the end of the string.
def endX(string):
	if (len(string)==1):
		return string
	else:
		if (string[0] == 'x'):
			return endX(string[1:]) + 'x'
		else:
			return string[0] + endX(string[1:])

# We'll say that a "pair" in a string is two instances of a char separated 
# by a char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" 
# contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number 
# of pairs in the given string.
def countPairs(string):
	if (len(string)==3):
		if (string[0]==string[2]):
			return 1
		else:
			return 0
	else:
		if (string[0]==string[2]):
			return 1 + countPairs(string[1:])
		else:
			return 0 + countPairs(string[1:])

# Count recursively the total number of "abc" and "aba" substrings that 
# appear in the given string.
def countAbc(string):
	if (len(string) == 3):
		if (string[0:] == 'abc') or (string[0:]=='aba'):
			return 1
		else:
			return 0
	else:
		if (string[0:3]=='abc') or (string[0:3]== 'aba'):
			return 1 + countAbc(string[1:])
		else:
			return 0 + countAbc(string[1:])

# Given a string, compute recursively (no loops) the number of "11" 
# substrings in the string. The "11" substrings should not overlap.
def count11(string):
	if (len(string)==2):
		if (string[:]=='11'):
			return 1
		else:
			return 0
	else:
		if (string[0:2] == '11'):
			return 1 + count11(string[2:])
		else:
			return 0 + count11(string[1:])

# Given a string, return recursively a "cleaned" string where adjacent 
# chars that are the same have been reduced to a single char. So "yyzzza" 
# yields "yza".
def stringClean(string):
	if (len(string)==2):
		if (string[0]==string[1]):
			return string[0]
		else:
			return string
	else:
		if (string[0]==string[1]):
			return stringClean(string[1:])
		else:
			return string[0] + stringClean(string[1:])


# Given a string, compute recursively the number of times lowercase "hi" 
# appears in the string, however do not count "hi" that have an 'x' 
# immedately before them.
def countHi2(string):
	if (len(string) < 2):
		return 0
	else:
		if (string[0:3]=='xhi'):
			return 0 + countHi2(string[3:])
		elif (string[0:2]=='hi'):
			return 1 + countHi2(string[2:])
		else:
			return 0 + countHi2(string[1:])

# Given a string that contains a single pair of parenthesis, compute 
# recursively a new string made of only of the parenthesis and their 
# contents, so "xyz(abc)123" yields "(abc)".
def parenBit(string):
	if (string[0] == '('):
		if (string[len(string)-1]==')'):
			return string
		else:
			return parenBit(string[0:len(string)-1])
	else:
		return parenBit(string[1:])

# Given a string, return True if it is a nesting of zero or more pairs 
# of parenthesis, like "(())" or "((()))". Suggestion: check the first 
# and last chars, and then recur on what's inside them.
def nestParen(string):
	if (string[0]=='(') and (string[len(string)-1]==')'):
		return True
	elif (string[0]=='('):
		return nestParen(string[:len(string)-1])
	elif (string[len(string)-1]==')'):
		return nestParen(string[1:])
	else:
		return nestParen(string[1:len(string)-1])

# Given a string and a non-empty substring sub, compute recursively the 
# number of times that sub appears in the string, without the sub strings 
# overlapping.
def strCount(string, sub):
	x = len(sub)
	if (len(string)<x):
		return 0
	else:
		if (string[0:x] == sub):
			return 1 + strCount(string[x:], sub)
		else:
			return 0 + strCount(string[1:], sub)

# Given a string and a non-empty substring sub, compute recursively if 
# at least n copies of sub appear in the string somewere, possibly with 
# overlapping. n will be non-negative.
def strCopies(string, sub, n):
	pass



# Given a string and a non-empty substring sub, compute recursively the 
# largest substring which starts and ends with sub and return its length.
def strDist(str, sub):
	pass









def main():
	n = 5
	print n, '! =', factorial(n)
	bun = 4
	print bun, 'bunnies have ', bunnyEars(bun), ' ears'
	fib = 5
	print 'fibonacci number #', fib, ' is ', fibonacci(fib)
	alien_buns = 4
	print 'the alien bunny group  of size', alien_buns, 'has', bunnyEars2(alien_buns), 'ears'
	rows = 4
	print 'a triangle with', rows, 'rows has', triangle(rows), 'blocks'
	n = 123
	print 'the digits of', n, 'sum to', sumDigits(n)
	n = 77171
	print n, 'contains', count7(n), '7s'
	base = 2
	power = 4
	print base, 'raised to',power, '=', powerN(base, power)
	string = 'axbxxcdx'
	print string, 'contains x',countX(string), 'times'
	string = 'hihihifsdgdfbadhadfhi'
	print string, 'says hi', countHi(string), 'times'
	string = 'piffffgidhdspipipi'
	print changePi(string)
	string = 'bvxcnfhgxxxxgh'
	print noX(string)
	nums = [5,3,6,8,6]
	print array6(nums,0)
	nums = [5,5,4,3,5]
	print array6(nums,0)
	nums = [11,12,5,6,7,8,11,11]
	print 'This array contains', array11(nums,0), '11s'
	nums = [10,1,13,4,3,15,150]
	print array220(nums,0)
	string = 'xxxxxx'
	print allStar(string)
	string = 'aabcbbnhmmgg'
	print pairStar(string)
	string = 'xxddgxxfgds'
	print endX(string)
	string = 'AxAxccvbbbAxA'
	print string, 'has', countPairs(string), 'pairs'
	string = 'acabcabagfhdabc'
	print string, 'contains', countAbc(string), 'pairs of abc or aba'
	string = '11fdsbdfsg111fdhg1111'
	print string, 'has', count11(string), '11s'
	string = 'yyzzzaa'
	print 'The clean string is', stringClean(string)
	string = 'hihixhivbfxhihi'
	print string, 'has', countHi2(string), 'his without xs in front'
	string = 'abc(123)abc'
	print parenBit(string)
	string = 'aa(())'
	print nestParen(string)
	string = 'bobobobmondaybobobobooobob'
	sub = 'bob'
	print strCount(string, sub)
	string = 'bobobobmondaybobobobooobob'
	sub = 'bob'
	print strCopies(string,sub,3)


main()