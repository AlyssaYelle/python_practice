class Link(object):
	def __init__(self, col = 0, data = 0, next = None):
		self.col = col
		self.data = data
		self.next = next

	# return a string representation of a link
	def __str__(self):
		s = '(' + str(self.col) + ', ' + str(self.data) + ')'
		return s

class LinkedList(object):
	def __init__(self):
		self.first = None
		self.count = 0

	def insert_last(self, col, data):
		new_link = Link(col, data)
		current = self.first

		if current == None:
			self.first = new_link
			self.count += 1
			return

		while current.next != None:
			current = current.next

		current.next = new_link
		self.count += 1

	def insert_link(self, col, data):
		current = self.first

		for i in range(self.count):

			if col == current.col:

				current.data = data
			if current.next != None:

				if current.next.col > col:
					new_link = Link(col, data)
					next_link = current.next
					current.next = new_link
					self.count += 1
					new_link.next = next_link
					return
				current = current.next
			else:
				self.insert_last(col, data)

	def delete_link(self, col, data):
		prev = self.first
		current = self.first

		for i in range(self.count):

			if current.col > col:
				return
			if current.col == col and self.count == 1:
				self.first = None
				count -= 1
				return
			if current.col == col:

				current = current.next
				prev.next = current
				self.count -= 1
				return
			else:
				prev = current
				current = current.next



	def __str__(self):
		s = ''
		current = self.first
		for i in range(self.count):
			s = s + str(current).rjust(4)
			current = current.next
		return s

class Matrix(object):
	def __init__(self, row = 0, col = 0):
		self.row = row
		self.col = col
		self.matrix = []

	# perform assignment operation: matrix[row][col] = data
	def set_element(self, row, col, data):
		i = 0

		for m_row in self.matrix:

			if row == i:
				if data == 0:
					m_row.delete_link(col, data)
				else:
					m_row.insert_link(col, data)
			i += 1


	# add two sparse matrices
	def __add__(self, other):
		if self.row != other.row or self.col != other.col:
			return None

		mat = Matrix(self.row, self.col)
		for i in range (self.row):
			new_row = LinkedList()
			row_self = self.get_row(i)
			row_other = other.get_row(i)
			for j in range (self.col):
				data = row_self[j] + row_other[j]
				new_row.insert_last(j, data)
			mat.matrix.append(new_row)

		return mat

	# multiply two sparse matrices
	def __mul__(self, other):
		if self.col != other.row:
			return None

		mat = Matrix(self.row, other.col)
		for i in range (self.row):
			new_row = LinkedList()
			row_self = self.get_row(i)
			for j in range (other.col):
				col_other = other.get_col(j)
				sum_mult = 0
				for k in range (other.row):
					sum_mult += (row_self[k]*col_other[k])
				new_row.insert_last(j,sum_mult)
			mat.matrix.append(new_row)
		return mat

	# return a list representing a row with the zero elements inserted
	def get_row(self, n):
		the_row = []
		i = 0
		for row in self.matrix:

			if n == i:
				current = row.first
				for j in range(self.col):
					if current.col == j:
						the_row.append(current.data)
						if current.next != None:
							current = current.next
					else:
						the_row.append(0)

			i += 1
		return the_row



	# return a list representing a colum with the zero elements included
	def get_col(self, n):
		the_col = []

		for row in self.matrix:
			the_row = []

			current = row.first
			for i in range(self.col):
				if i == current.col:
					the_row.append(current.data)
					if current.next != None:
						current = current.next
				else:
					the_row.append(0)
			the_col.append(the_row[n])



		
		return the_col

	# return a string representation of a matrix
	def __str__(self):
		s = ''

		for row in self.matrix:
			current = row.first
			
			for i in range(self.col):
				if current.col == i:
					s = s + str(current.data).rjust(4)
					if current.next != None:
						current = current.next

				else:
					s = s + '0'.rjust(4)

			s = s + '\n'

		return s

def read_matrix(in_file):
	line = in_file.readline().rstrip('\n').split()
	row = int(line[0])
	col = int(line[1])
	mat = Matrix(row, col)

	for i in range (row):
		line = in_file.readline().rstrip('\n').split()
		new_row = LinkedList()
		for j in range (col):
			elt = int(line[j])
			if elt != 0:
				new_row.insert_last(j, elt)
		mat.matrix.append(new_row)
		
	line = in_file.readline()

	return mat

def main():
	in_file = open('./text_files/matrix.txt', 'r')

	print('Test Matrix Addition')
	matA = read_matrix(in_file)
	print(matA)
	matB = read_matrix(in_file)
	print(matB)

	matC = matA + matB
	print(matC)

	print('\nTest Matrix Multiplication')
	matP = read_matrix(in_file)
	print(matP)
	matQ = read_matrix(in_file)
	print(matQ)

	matR = matP * matQ
	print(matR)

	print('\nTest Setting a Zero Element to a Non-Zero Value')
	matA.set_element(1,1,5)
	print(matA)

	print('\nTest Setting a Non-Zero Element to a Zero Value')
	matB.set_element(1,1,0)
	print(matB)

	print('\nTest Getting a Row')
	row = matP.get_row(1)
	print(row)

	print('\nTest Getting a Column')
	col = matQ.get_col(0)
	print(col)

	in_file.close()

if __name__ == "__main__":
	main()