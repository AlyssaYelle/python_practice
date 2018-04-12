


class Stack(object):
	def __init__(self):
		self.stack = []

	# add an item to the top of the stack
	def push (self, item):
		self.stack.append(item)

	# remove an item from the top of the stack
	def pop (self):
		return self.stack.pop()

	# check the item on top of the stack
	def peek (self):
		return self.stack[-1]

	# check if the stack is empty
	def is_empty (self):
		return (len(self.stack)==0)

	# return the number of elements in the stack
	def size (self):
		return (len(self.stack))



class Node(object):
	def __init__(self, data = None):
		self.data = data
		self.lchild = None
		self.rchild = None

	# return a string representation of a link
	def __str__(self):
		s = str(self.data)
		return s

class Tree(object):
	def __init__(self):
		self.root = None

	def createTree(self, expr):
		pass

	def evaluate(self, aNode):
		pass

	def preOrder(self, aNode):
		pass

	def postOrder(self, aNode):
		pass

def main():
	in_file = open('~/Projects/python_practice/software_design/text_files/expression.txt', 'r')
	exp = infile.readline.rstrip('\n')
	print(exp)


main()











