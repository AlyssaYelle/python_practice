


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

		operand_stack = Stack()
		operator_stack = Stack()
		operators = ['+', '-', '*', '/']
		for ch in expr:
			if ch == '(':
				pass
			elif ch == ')':
				op = operator_stack.pop()
				r = operand_stack.pop()
				l = operand_stack.pop()
				op.lchild = l
				op.rchild = r
				self.root = op
				operand_stack.push(self)
				print(l,op,r)

			elif ch in operators:
				new_node = Node(ch)
				operator_stack.push(new_node)
				#print(new_node)
			else:
				new_node = Node(float(ch))
				operand_stack.push(new_node)
				#print(new_node)

	def evaluate(self, aNode):
		if aNode.lchild == None and aNode.rchild == None:
			return aNode.data
		else:
			pass

	def preOrder(self, aNode):
		pass

	def postOrder(self, aNode):
		pass




def main():
	in_file = open('expression.txt', 'r')
	exp = in_file.readline().rstrip('\n').split()
	my_tree = Tree()
	my_tree.createTree(exp)


if __name__ == "__main__":
	main()











