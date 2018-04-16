# expression tree program takes in as input a mathematical expression
# formatted with parentheses
# and computes answer
# we assume that the expression is valid
# also outputs the expression in prefix and postfix notation


global preOrder_str
preOrder_str = 'Prefix expression: '
global postOrder_str
postOrder_str = 'Postfix expression: '


# will use stack objects to keep track of mathematical expression
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
		self.parent = None
		self.lchild = None
		self.rchild = None

	# return a string representation of a link
	def __str__(self):
		s = str(self.data)
		return s

class Tree(object):
	def __init__(self):
		self.root = None


	# first create two stack objects
	# one for operands
	# one for operators
	# ')' tells us when to pop from stack
	# pop two from operands, one from operators, make a tree (or append if popping existing trees)
	# return fully populated expression tree
	def createTree(self, expr):
		operand_stack = Stack()
		operator_stack = Stack()
		operators = ['+', '-', '*', '/']
		s = ''
		for ch in expr:
			if ch == '(':
				s = s + ch + ' '
				pass
			elif ch == ')':
				s = s + ch + ' '
				op = operator_stack.pop()
				if operator_stack.size() == 0:
					self.root = op
				r = operand_stack.pop()
				l = operand_stack.pop()
				r.parent = op
				l.parent = op
				op.lchild = l
				op.rchild = r
				operand_stack.push(op)


			elif ch in operators:
				s = s + ch + ' '
				new_node = Node(ch)

				operator_stack.push(new_node)

			else:
				s = s + ch + ' '
				new_node = Node(float(ch))
				operand_stack.push(new_node)
		s = s + ' = '
		return s


	# evaluates the expression tree
	# starting from leaf nodes
	def evaluate(self, aNode):
		exp = ['+','-','*','/']
		root = self.root
		parent = aNode
		lchild = parent.lchild
		rchild = parent.rchild
		if self.root.lchild == None and self.root.rchild == None:
			solution = root.data
			return (solution)
		if lchild.data in exp:
			aNode = lchild
			self.evaluate(aNode)
		if rchild.data in exp:
			aNode = rchild
			self.evaluate(aNode)
		if lchild not in exp and rchild not in exp:
			op = aNode
			if op.data == '+':
				op.data = lchild.data + rchild.data
			elif op.data == '-':
				op.data = lchild.data - rchild.data
			elif op.data == '*':
				op.data = lchild.data * rchild.data
			elif op.data == '/':
				op.data = lchild.data / rchild.data

			op.lchild = None
			op.rchild = None
			self.evaluate(root)		



	def preOrder(self, aNode):
		if aNode != None:
			s = str(aNode) + ' '
			global preOrder_str
			preOrder_str = preOrder_str + s
			self.preOrder(aNode.lchild)
			self.preOrder(aNode.rchild)

	def postOrder(self, aNode):
		if aNode != None:
			self.postOrder(aNode.lchild)
			self.postOrder(aNode.rchild)
			s = str(aNode) + ' '
			global postOrder_str
			postOrder_str = postOrder_str + s




def main():
	in_file = open('expression.txt', 'r')
	exp = in_file.readline().rstrip('\n').split()
	my_tree = Tree()
	tree = my_tree.createTree(exp)
	root = my_tree.root
	my_tree.preOrder(root)
	my_tree.postOrder(root)
	solution = my_tree.evaluate(root)
	print(tree,my_tree.evaluate(root),'\n')
	print(preOrder_str, '\n')
	print(postOrder_str)



if __name__ == "__main__":
	main()











