'''

python3

takes in a mathematical expression in string form and takes the derivative

to begin, we will assume mathematical expression
1. is valid
2. contains only integers, +, *, ^, and the letter x

'''

class Differentiator:

    def __init__(self):
        pass



class Node:
    def __init__(self, data = None):
        self.data = data
        self.parent = None
        self.lchild = None
        self.rchild = None

    # return a string representation of a link
    def __str__(self):
        s = str(self.data)
        return s



class ExpressionTree:
    def __init__(self):
        self.root = None



class Stack:
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



if __name__ == "__main__":
    return