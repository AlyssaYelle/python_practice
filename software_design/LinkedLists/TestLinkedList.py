'''
The purpose of this program is to create a linked list class
and define helpful methods
We then test the methods in main
'''

class Link(object):
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)

class LinkedList(object):
	def __init__(self):
		self.first = None
		self.count = 0

	# get number of links
	def get_num_links(self):
		return self.count

	# add an item at the beginning of the list
	def insert_first(self, item):
		new_link = Link(item)
		new_link.next = self.first
		self.first = new_link
		self.count += 1

	# add an item at the end of a list
	def insert_last(self, item):
		new_link = Link(item)

		current = self.first
		if (current == None):
			self.first = new_link
			self.count += 1
			return

		while current.next != None:
			current = current.next

		current.next = new_link
		self.count += 1

	# add an item in an ordered list in ascending order
	def insert_in_order(self, item):
		new_link = Link(item)
		current = self.first

		if current == None:
			self.first = new_link
			self.count += 1
			return

		if current.data >= item:
			new_link.next = current
			self.first = new_link
			self.count += 1
			return

		while current.next != None and current.next.data < item:
			current = current.next

		new_link.next = current.next
		current.next = new_link
		self.count += 1


	# search in an unordered list, return None if not found
	def find_unordered(self, item):
		current = self.first

		if current == None:
			return None

		while current.data != item:
			if current.next == None:
				return None
			else:
				current = current.next

		return current

	# search in an ordered list, return None if not found
	def find_ordered(self, item):
		current = self.first

		if current == None:
			return None

		while current.data != item:
			if current.next == None:
				return None
			elif current.data > item:
				return None
			else:
				current = current.next

		return current


	# delete and return Link from an unordered list or None if not found
	def delete_link(self, item):
		previous = self.first
		current = self.first
		if current == None:
			return None
		while current.data != item:
			if current.next == None:
				return None
			else:
				previous = current
				current = current.next
		if previous == self.first:
			self.first = current
		else:
			previous.next = current.next
		self.count -= 1
		return Link(item)


	# string representation of data 10 items to a line, 2 spaces between data
	def __str__(self):
		current = self.first
		s = ''
		i = 0
		while True:
			s = s + str(current) + '  '
			i += 1
			current = current.next
			if i%10 == 0:
				s = s + '\n'
			if i == self.count:
				return s


	# copy contents of a list and return new list
	def copy_list(self):
		new_list = LinkedList()

		current = self.first
		for i in range(self.count):
			new_list.insert_last(current.data)
			current = current.next
			i+=1
		return new_list


	# reverse the contents of a list and return new list
	def reverse_list(self):
		new_list = LinkedList()

		current = self.first
		for i in range(self.count):
			new_list.insert_first(current.data)
			current = current.next
			i+=1
		return new_list

	# sort the contents of a list in ascending order
	def sort_list(self):
		sorted_list = LinkedList()
		current = self.first

		for i in range(self.count):
			sorted_list.insert_in_order(current.data)
			current = current.next

		return sorted_list

	# return True if a list is sorted in ascending order
	def is_sorted(self):
		current = self.first

		while current.next != None:
			if current.next.data < current.data:
				return False
			current = current.next

		return True

	# return True if list is empty
	def is_empty(self):
		if self.count == 0:
			return True
		return False

	# merge two sorted lists and return new list
	def merge_list(self, other):
		merged_list = LinkedList()

		current1 = self.first
		current2 = other.first

		while merged_list.count < (self.count + other.count):
			merged_list.insert_in_order(current1.data)
			merged_list.insert_in_order(current2.data)
			current2 = current2.next
			current1 = current1.next

		return merged_list



	# test if two lists are equal and return True
	def is_equal(self, other):
		if self.count != other.count:
			return False

		current1 = self.first
		current2 = other.first

		for i in range(self.count):
			if current1.data != current2.data:
				return False
			i += 1
			current1 = current1.next
			current2 = current2.next
		return True

	# remove duplicate values without changing order

	def remove_duplicates(self):
		no_dups_list = LinkedList()
		current = self.first
		vals = []

		while current != None:
			if current.data not in vals:
				vals.append(current.data)
				no_dups_list.insert_last(current.data)
			current = current.next

		return no_dups_list






def main():
	# test methods insert_first() and __str__() by adding more than 10 items to list and printing it
	my_list = LinkedList()
	print('My new list is empty: (T/F)')
	print(my_list.is_empty())
	my_list.insert_first(1)
	my_list.insert_first(7)
	my_list.insert_first(13)
	my_list.insert_first(8)
	my_list.insert_first(3)
	my_list.insert_first(13)
	my_list.insert_first(9)
	my_list.insert_first(2)
	my_list.insert_first(4)
	my_list.insert_first(5)
	my_list.insert_first(6)
	my_list.insert_first(10)
	my_list.insert_first(7)
	print('I have added data to my list.')
	print('this list has', my_list.get_num_links(), 'links')
	print('here is my list')
	print(my_list)

	# test method insert_last()
	print('I am adding an 8 to the end of my list')
	my_list.insert_last(8)
	print(my_list)

	# test method insert_in_order()
	print('I am adding an 11 and a 32 to my list')
	my_list.insert_in_order(11)
	my_list.insert_in_order(32)
	print(my_list)

	# test method get_num_links()
	print('now my list has', my_list.get_num_links(), 'links')

	# test method find_unordered()
	# consider two cases - item is there, item isn't there
	print('I will check to see if my list contains a 7')
	print(my_list.find_unordered(7))
	print('I will check to see if my list contains a 22')
	print(my_list.find_unordered(22))

	# test method find_ordered()
	# consider two cases - item is there, item isn't there
	print('I will check to see if my list contains a 10')
	print(my_list.find_ordered(10))
	print('I will check to see if my list contains a 22')
	print(my_list.find_ordered(22))

	# test method delete_link()
	# consider two cases - item is there, item isn't there
	print('my list currently has', my_list.get_num_links(), 'links')
	print('I will delete 77 from my list')
	print(my_list.delete_link(77))
	print('I will delete 1 from my list')
	print(my_list.delete_link(1))

	print('my list currently has', my_list.get_num_links(), 'links')
	print(my_list)

	# test method copy_list()
	print('I will copy my list')
	print('new list:')
	c_list = my_list.copy_list()
	print(c_list)

	# test method reverse_list()
	print('I will reverse my list')
	r_list = my_list.reverse_list()
	print('reversed list:\n',r_list)

	# test method sort_list()
	print('I will sort my original list')
	s_list = my_list.sort_list()
	print('sorted list:\n', s_list)

	# test method is_sorted()
	# consider two cases - list is sorted, list is unsorted
	print('confirming that sorted list is sorted:', s_list.is_sorted())
	print('is the original list sorted?', my_list.is_sorted())

	# test method is_empty()
	print('My list is empty: (T/F)')
	print(my_list.is_empty())

	# test method merge_list()
	print('now i will merge my original list and the reversed list')

	m_list = my_list.merge_list(r_list)
	print(m_list)

	# test method is_equal()
	# consider two cases - lists are equal, lists are not
	print('is my list equal to the copied list? ', my_list.is_equal(c_list))
	print('is my list equal to the reversed list? ', my_list.is_equal(r_list))

	# test remove_duplicates()
	print('I will remove the duplicate values from my merged list')
	print(m_list.remove_duplicates())



if __name__ == '__main__':
	main()









