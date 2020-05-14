'''
Find the first common ancestor of two nodes in a binary tree.
The tree is not necessarily a binary search tree.
But it IS a balanced binary tree.
'''
import numpy as np
import math

# BinaryTree class
class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.nnodes = 0 if root is None else 1

    def add_node(self, node):
        if self.root is None:
            self.root = node
            self.nnodes += 1
            return

        # Figure out where this node belongs
        height_of_incoming_node = math.floor(math.log2(self.nnodes+1))
        position_on_level = self.nnodes+1 - 2**height_of_incoming_node

        # Get the path to follow
        path_to_node = self.get_path(height_of_incoming_node, position_on_level)

        # Walk to the penultimate node in the path
        cur = self.root
        for b in path_to_node[:-1]:
            cur = cur.left if b == 0 else cur.right

        # Look at the last bit in the bit vector and set left child to node if it's zero
        if path_to_node[-1] == 0:
            cur.left = node
        else:
            cur.right = node

        # Set the parent of node
        node.parent = cur

        # Update the tree to reflect adding this node
        self.nnodes += 1

        print('Node: {} Parent: {} Is: {}'.format(node.value, node.parent.value, 'Left' if node.parent.left == node else 'Right'))

    def get_path(self, height, remainder):
        # Convert remainder to a bit vector
        bit_vector = [int(b) for b in bin(remainder)[2:]]

        # Pad zeros at start until bit_vector is height length
        return [0]*(height-len(bit_vector)) + bit_vector

    def common_ancestor(self, node1, node2):

        # compare the heights
        height_node1 = self.height_of(node1)
        height_node2 = self.height_of(node2)

        height_difference = abs(height_node1 - height_node2)

        # set pointers
        node_closest_to_root = node1 if height_node2 > height_node1 else node2
        node_less_close_to_root = node1 if node_closest_to_root == node2 else node2

        # move pointer for lower node up along tree until it is at the same height as the other node
        while height_difference > 0:
            node_less_close_to_root = node_less_close_to_root.parent

            height_difference -= 1

        # compare node ancestry by moving pointers up along tree until the pointers are the same node
        while node_closest_to_root != node_less_close_to_root:

            node_closest_to_root = node_closest_to_root.parent
            node_less_close_to_root = node_less_close_to_root.parent

        # we can return either pointer and it will be the first common ancestor
        return node_less_close_to_root


    def print_path_to_root(self, node):
        print('\nPath to root from', node.value)

        cur = node

        while cur.parent is not None:
            print(cur.parent.value)

            cur = cur.parent





    def height_of(self, node):
        '''
        traverses up parental lineage of node until it reached None
        '''

        height = 0
        cur = node
        while cur.parent != None:
            cur = cur.parent
            height += 1

        return height

# Node class
class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

def build_tree():
    root = Node(5)
    left = Node(6)
    right = Node(7)
    leftleft = Node(8)
    leftright = Node(9)
    rightleft = Node(10)

    tree = BinaryTree(root=root)

    tree.add_node(left)
    tree.print_path_to_root(left)

    tree.add_node(right)
    tree.print_path_to_root(right)

    tree.add_node(leftleft)
    tree.print_path_to_root(leftleft)

    tree.add_node(leftright)
    tree.print_path_to_root(leftright)

    tree.add_node(rightleft)
    tree.print_path_to_root(rightleft)



    print('Expected: {}\nResults: {}\n'.format(root.value, tree.common_ancestor(left, rightleft).value))
    print('Expected: {}\nResults: {}\n'.format(root.value, tree.common_ancestor(leftleft, rightleft).value))
    print('Expected: {}\nResults: {}\n'.format(left.value, tree.common_ancestor(leftleft, leftright).value))





if __name__ == '__main__':
    # Create a tree
    build_tree()

    # Populate it with some trial data

    # Try some test examples

    pass

















