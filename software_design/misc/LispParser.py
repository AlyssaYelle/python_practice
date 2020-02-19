'''

Write code that takes some Lisp code and returns an abstract syntax tree. 
The AST should represent the structure of the code and the meaning of each token. 
For example, if your code is given "(first (list 1 (+ 2 3) 9))", 
it could return a nested array like ["first", ["list", 1, ["+", 2, 3], 9]].

'''

class Parser:

    def __init__(self):
        pass



class AbstractSyntaxTree:
    '''
    creates an empty tree
    each node on the tree can have multiple childen
    '''

    def __init__(self):
        self.root = None





class Node:
    '''
    returns a node that may optionally have a single parent node and many child nodes
    '''

    def __init__(self, data = None):
        self.data = data
        self.parent = None
        self.children = []

    # return a string representation of a link
    def __str__(self):
        s = str(self.data)
        return s


if __name__ == "__main__":
    my_node = Node("(+ 2 3)")
    print(my_node)






if __name__ == '__main__':
    parser = Parser()