'''
This program considers the Josephus problem, in which n soldiers
are surrounded by an enemy force with no way out.
They arrange themselves in a circle and decide to commit suicide
by counting off x soldiers, starting from soldier a, 
then soldier #x will die, etc etc.
The output of this program is the order in which they commit suicide.
The soldiers are represented by a circular linked list.
To get n, a, x we read in a text file of the form
n
a
x
'''

# class for a single link
# here we will use a double link
class Link(object):
	# a single link will have a next pointer, pointing to itself
	# and a prev pointer, pointing back to itself
	def __init__(self, data = None, next_link = None, prev_link = None):
		self.data = data
		self.next = next_link
		self.prev = prev_link

	def __str__(self):
		return str(self.data)

# class for a doubly linked circular list
class CircularList(object):
	# initialize with a single link as self.first
	# and also self.last
	# inititalize count as 1
	def __init__(self):
		self.first = Link()
		self.count = 1

	# insert an element in the list
	def insert(self, item):
		current = self.first
		new_link = Link(item)

		if self.first.data == None:
			self.first = new_link
			self.first.next = self.first
			self.first.prev = self.first
			self.last = self.first
		else:
			self.first.prev = new_link
			self.last.next = new_link
			new_link.prev = self.last
			self.last = new_link
			new_link.next = self.first
			self.count += 1


	# find the link with the given key
	def find(self, key):
		current = self.first

		if current.data == key:
			return current

		while current.data != key:
			if current.next == self.first:
				return None
			else:
				current = current.next

		return current

	# delete a link with the given key
	def delete(self, key):
		found = self.find(key)
		if found == self.first:
			self.first = found.next

		if self.find(key) == False:
			return None
		else:
			back = found.prev
			forward = found.next
			back.next = forward
			forward.prev = back
			self.count -= 1

		

		



	# delete the nth link starting from the Link start
	# Return the next link from the deleted Link
	def delete_after(self, start, n):
		current = self.find(start)
		
		for i in range(n-1):
			current = current.next

		self.delete(current.data)
		print(current)
		return current.next

		

	# return a string representation of a Circular List
	def __str__(self):
		current = self.first
		s = ''
		i = 0
		while True:
			s = s + str(current) + '\n'
			i += 1
			current = current.next
			
			if i == self.count:
				return s

def main():
	in_file = open('josephus.txt', 'r')
	num_soldiers = int(in_file.readline().rstrip('\n'))
	first_soldier = int(in_file.readline().rstrip('\n'))

	count = int(in_file.readline().rstrip('\n'))

	my_list = CircularList()
	i = 0
	for i in range(num_soldiers):
		my_list.insert(i+1)
		i += 1

	
	deleted = my_list.delete_after(first_soldier, count)
	while my_list.count > 0:
		deleted = my_list.delete_after(deleted.data, count)

main()