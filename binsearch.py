import sys

my_list = [5,8,1,12,14,700,6,1,32,55]

n = int(sys.argv[1])

def binsearch(my_list, n):
	my_list.sort()
	mid = len(my_list)//2
	if n < my_list[0]:
		x = (my_list, 0)
	elif n > my_list[len(my_list)-1]:
		x = (my_list, len(my_list))
	elif n == my_list[mid]:
		x = (my_list,mid)
	else:
		start = 0
		end = len(my_list)-1
		while n != my_list[mid]:
			if end == start + 1:
				mid = end
				break
			if n < my_list[mid]:
				end = mid
				mid = (start + end)//2
			else:
				start = mid
				mid = (start + end)//2
		x = (my_list,mid)
	return x


def bin_rec(my_list,n):
	my_list.sort()
	mid = len(my_list)//2
	if n < my_list[0]:
		x = (my_list, 0)
	elif n > my_list[len(my_list)-1]:
		x = (my_list, len(my_list))
	elif n == my_list[mid]:
		x = (my_list,mid)
	else:
		start = 0
		end = len(my_list)-1
		x = bin_helper(my_list, n, start, end,mid)
	return x

def bin_helper(my_list,n,start,end,mid):
	if n == my_list[mid]:
		x = (my_list, mid)
		return x
	if end == start + 1:
		mid = end
		x = (my_list, mid)
		return x
	elif n < my_list[mid]:
		end = mid
		mid = (start + end)//2
		return bin_helper(my_list,n,start,end,mid)
	elif n > my_list[mid]:
		start = mid
		mid = (start + end)//2
		return bin_helper(my_list,n,start,end,mid)






print bin_rec(my_list,n)
print binsearch(my_list,n)