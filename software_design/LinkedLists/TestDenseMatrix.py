class Matrix(object):
	def __init__(self, row = 0, col = 0):
		self.row = row
		self.col = col
		self.matrix = []

	# perform matrix addition
	def __add__(self, other):
		if self.row != other.row or self.col != other.col:
			return None

		mat = Matrix(self.row, self.col)
		for i in range (self.row):
			new_row = []
			for j in range (self.col):
				new_row.append(self.matrix[i][j] + other.matrix[i][j])
			mat.matrix.append(new_row)

		return mat

	def __mul__ (self, other):
		if self.col != other.row:
			return None

		mat = Matrix(self.row, other.col)
		for i in range (self.row):
			new_row = []
			for j in range (other.col):
				sum_mult = 0
				for k in range (other.row):
					sum_mult += (self.matrix[i][k]*other.matrix[k][j])
				new_row.append(sum_mult)
			mat.matrix.append(new_row)
		return mat

	def __str__(self):
		s = ''
		for i in range(self.row):
			for j in range(self.col):
				s = s + str(self.matrix[i][j]).rjust(4)
			s = s + '\n'
		return s

def read_matrix(in_file):
	line = in_file.readline().rstrip('\n').split()
	row = int(line[0])
	col = int(line[1])
	mat = Matrix(row, col)

	for i in range (row):
		line = in_file.readline().rstrip('\n').split()
		for j in range (col):
			line[j] = int(line[j])
		mat.matrix.append(line)
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
	in_file.close()

main()


