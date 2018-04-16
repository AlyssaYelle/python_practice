
def permute_secretary(a,lo):
	hi = len(a)
	if (lo == hi):
		if (a[0] == 'A') or (a[1]=='B') or (a[2]=='C') or (a[3]=='D'):
			pass
		else:
			print a
	else:
		for i in range (lo,hi):
			a[lo], a[i] = a[i], a[lo]
			permute_secretary(a, lo+1)
			a[lo], a[i] = a[i], a[lo]

def permute_friends(a,lo):
	hi = len(a)
	if (lo == hi):
		if (help_friends_sit(a)):
			print a

	else:
		for i in range(lo,hi):
			a[lo], a[i] = a[i], a[lo]
			permute_friends(a, lo+1)
			a[lo], a[i] = a[i], a[lo]

def help_friends_sit(a):
	if (a[0]== 'A' and a[4] == 'B') or (a[0] == 'B' and a[4] == 'A'):
		return False
	for i in range(1, 4):
		if (a[i] == 'A' and a[i+1] != 'B') and (a[i] == 'A' and a[i-1] != 'B'):
			return False
		elif (a[i] == 'B' and a[i+1] != 'A') and (a[i] == 'B' and a[i-1] != 'A'):
			return False
		elif (a[i] == 'C' and a[i-1] == 'D') or (a[i] == 'C' and a[i+1] == 'D'):
			return False 
		elif (a[i] == 'D' and a[i-1] == 'C') or (a[i] == 'D' and a[i+1] == 'C'):
			return False
	return True



def main():
	a1 = ['A', 'B', 'C', 'D']
	a2 = ['A', 'B', 'C', 'D', 'E']
	permute_secretary(a1,0)
	permute_friends(a2,0)
	

main()