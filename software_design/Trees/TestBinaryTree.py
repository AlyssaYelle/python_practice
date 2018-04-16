# create a binary search tree object
# not necessarily balanced
# test methods



class Node (object):
	def __init__(self, data = None):
		self. data = data
		self.lchild = None
		self.rchild = None

	# check if node is a leaf
	# this might come in handy at some point
	def is_leaf(self):
		if self.lchild != None or self.rchild != None:
			return False
		return True

	def __str__(self):
		s = str(self.data)
		return s

class Tree (object):
	def __init__(self):
		self.root = None
		self.count = 0

	# search for a node with a key
	# not useful for this homework but it's there to use if ever necessary
	def search (self, key):
		current = self.root
		while current != None and current.data != key:
			if key < current.data:
				current = current.lchild
			else:
				current = current.rchild
		return current

	# insert a node in a tree
	def insert( self, val):
		new_node = Node(val)

		if self.root == None:
			self.root = new_node
		else:
			current = self.root
			parent = self.root
			while current != None:
				parent = current
				if val < current.data:
					current = current.lchild
				else:
					current = current.rchild
			if val < parent.data:
				parent.lchild = new_node
			else:
				parent.rchild = new_node
		self.count += 1

	# delete a node with a given key
	# not useful for this homework but it's there to use if ever necessary
	def delete (self, key):
		delete_node = self.root
		parent = self.root
		is_left = False

		# if empty tree
		if delete_node == None:
			return None

		# find the delete node
		while delete_node != None and delete_node.data != key:
			parent = delete_node
			if key < delete_node.data:
				delete_node = delete_node.lchild
				is_left = True
			else:
				delete_node = delete_node.rchild
				is_left = False

		# if node not found
		if delete_node == None:
			return None

		# check if delete node is a leaf node
		if delete_node.lchild == None and delete_node.rchild == None:
			if delete_node == self.root:
				self.root = None
			elif is_left:
				parent.lchild = None
			else:
				parent.rchild = None

		# delete node is a node with only a left child
		elif delete_node.rchild == None:
			if delete_node == self.root:
				self.root = delete_node.lchild
			elif is_left:
				parent.lchild = delete_node.lchild
			else:
				parent.rchild = delete_node.lchild

		# delete node is a node with only a right child
		elif delete_node.lchild == None:
			if delete_node == self.root:
				self.root = delete_node.rchild
			elif is_left:
				parent.lchild = delete_node.rchild
			else:
				parent.rchild = delete_node.rchild

		# delete node has both left and right children
		else:
			# find delete node's successor and the successor's parent node
			successor = delete_node.rchild
			successor_parent = delete_node

			while successor.lchild != None:
				successor_parent = successor
				successor = successor.lchild

			# successor node is right child of delete node
			if delete_node == self.root:
				self.root = successor
			elif is_left:
				parent.lchild = successor
			else:
				parent.rchild = successor

			# connect delete node's left child to be the successor's left child
			successor.lchild = delete_node.lchild

			# successor node left descendent of delete node
			if successor != delete_node.rchild:
				successor_parent.lchild = successor.rchild
				successor.rchild = delete_node.rchild

		self.count -= 1
		return delete_node



	# returns true if two binary trees are similar
	# pNode is another tree
	def is_similar(self, pNode):
		# the helper function will traverse the trees simultaneously
		# beginning at the root
		if self.is_similar_helper(self.root, pNode.root):
			return True
		else:
			return False



	# helper function for is_similar
	def is_similar_helper(self, aNode, bNode):

		# two empty trees are similar
		if aNode == None and bNode == None:
			return True

		# check cases in case trees are not empty
		else:
			# not similar if one tree has node where another does not
			if (aNode == None and bNone != None) or (aNode != None and bNode == None):
				return False
			# not similar if one tree has a leaf where another does not
			elif (aNode.is_leaf() and bNode.is_leaf() == False) or (bNode.is_leaf() and aNode.is_leaf() == False):
				return False
			# not similar if data does not match
			elif aNode.data != bNode.data:
				return False
			else:
				# passed test cases so continue traversing tree
				return self.is_similar_helper(aNode.lchild, bNode.lchild)
				return self.is_similar_helper(aNode.rchild, bNode.rchild)

	# prints out all nodes at the given level
	def print_level(self, level):
		# this will be easier to do with a private method allowing for more parameters

		the_level = []

		# if the level is greater than the height of the tree
		# then obviously no nodes exist at the given level
		if level > self.get_height():
			return None

		# call private helper function which will update the_level list
		self.print_level_helper(level, 1, self.root, the_level)
		return the_level
		

	def print_level_helper(self, level, current_level, aNode, the_level):
		if aNode is None:
			return

		# only want to append to the_level if we are at the correct level
		if current_level == level:
			the_level.append(aNode.data)
			return the_level

		return self.print_level_helper(level, current_level + 1, aNode.lchild, the_level), self.print_level_helper(level, current_level + 1, aNode.rchild, the_level)




	# returns the height of the tree
	def get_height(self):
		# let a private helper function that takes the root as a param do the work
		return(self.get_height_helper(self.root))

	def get_height_helper(self, aNode):
		# if node is none then we're done with this path
		if aNode is None:
			return 0
		# otherwise we want the max path height
		return (1 + max(self.get_height_helper(aNode.lchild), self.get_height_helper(aNode.rchild)))

	# returns number of nodes in the tree
	def num_nodes(self):
		# if there's no root the tree is empty and has 0 nodes
		if self.root == None:
			return 0
		# otherwise we count the nodes in each subtree and add 1
		# (the root counts as one node)
		else:
			return(1 + self.num_nodes_helper(self.root.lchild) + self.num_nodes_helper(self.root.rchild))

	def num_nodes_helper(self, aNode):
		# if we traverse the tree over to where a node doesn't exist then there's nothing to add
		if aNode == None:
			return 0
		# keep traversing smaller and smaller subtrees
		return (1 + self.num_nodes_helper(aNode.lchild) + self.num_nodes_helper(aNode.rchild))


def main():
	# create three trees - two are the same, one is different
	# create three lists of values to insert into the trees
	tree1_data = [6, 5, 7, 2, 4, 8, 9]
	tree2_data = [6, 5, 7, 2, 4, 8, 9]
	tree3_data = [6, 7, 3, 4, 5, 2, 10, 8, 9]

	# create three tree objects
	tree1 = Tree()
	tree2 = Tree()
	tree3 = Tree()

	# loop through value lists to populate the trees
	for i in range(len(tree1_data)):
		tree1.insert(tree1_data[i])

	for i in range(len(tree2_data)):
		tree2.insert(tree2_data[i])

	for i in range(len(tree3_data)):
		tree3.insert(tree3_data[i])


	# test method is_similar()
	print('Tree 1 is similar to Tree 2: ', tree1.is_similar(tree2))
	print('Tree 1 is similar to Tree 3: ', tree1.is_similar(tree3), '\n')

	# print levels of two trees that are different
	# here i am testing level 3
	# other levels have been tested as well
	print('Tree 1 Level 3: ', tree1.print_level(3))
	print('Tree 3 Level 3: ', tree3.print_level(3),'\n')

	# get the height of the two trees that are different
	print('Height of Tree 1: ', tree1.get_height())
	print('Height of Tree 3: ', tree3.get_height(),'\n')

	# get the total number of nodes for a binary search tree
	print('Number nodes in Tree 1: ', tree1.num_nodes())
	print('Number nodes in Tree 2: ', tree2.num_nodes())
	print('Number nodes in Tree 3: ', tree3.num_nodes())

if __name__ == '__main__':
	main()






