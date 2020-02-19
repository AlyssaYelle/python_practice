#  File: BST_Cipher.py

#  Description: encrypt and decrypt using happly little binary treeeees

#  Student Name: Alyssa Jones

#  Student UT EID: adj484

#  Partner Name: Juan Zambrano

#  Partner UT EID: jez346

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 16 April

#  Date Last Modified: 19 April


class Node (object):
    def __init__(self, data):
        self.data = data
        self.rchild = None
        self.lchild = None

    def __str__(self):
        return str(self.data)


class Tree (object):
	# the init() function create the binary search tree with the
	# encryption string. If the encryption string contains any
	# character other than the characters 'a' through 'z' or the
	# space character drop that character
	def __init__ (self, encrypt_str):
		self.root = None
		# convert to lower & adds only char or space
		char_ls = []
		for i in encrypt_str.lower():
			if i.isalpha() or i.isspace():
				char_ls.append(i)
		l = []
		for ch in char_ls:
			if ch not in l: 
				l.append(ch)
		for i in l:
			self.insert(i)


	# the insert() function adds a node containing a character to
	# the binary search tree. If the character already exists, it
	# does not add that character. There are no duplicate characters
	# in the binary search tree
	def insert (self, ch):
		new_node = Node(ch)
		if(self.root == None):
			self.root = new_node
			return
		elif(ord(ch) >= ord('a') and ord(ch) <= ord('z')):
			current = self.root
			parent = self.root
			while(current != None):
				parent = current
				if(ord(ch) < ord(current.data)):
					current = current.lchild
				else:
					current = current.rchild
			if (ord(ch) < ord(parent.data)):
				parent.lchild = new_node
			else:
				parent.rchild = new_node

	# the search() function will search for a character in the binary
	# search tree and return a string containing a series of lefts (<)
	# and rights (>) needed to reach that character. It will return a 
	# blank string if the character does not exists in the search tree.
	# It will return * if the character is the root of the tree.
	def search (self, ch):
		current = self.root
		if( ch == current.data):
			return '*'
		st = ''
		while((current != None) and (current.data != ch)):
			if(ch < current.data):
				st += '<'
				current = current.lchild
			elif(ch > current.data):
				st += '>'
				current = current.rchild
		if(current == None):
			return ''
		else:
			return st

	# the traverse() function will take a string composed of a series of
	# lefts (<) and rights (>) and return the corresponding character
	# in the binary search tree. It will return an empty string
	# if the input parameter does not lead to a valid character.
	def traverse (self, st):
		prev = self.root
		current = self.root
		s = ''
		for i in range(len(st)):

			if st[i] == '!':

				if st[i-1] == '!':
					s += ' '
				else:
					s += current.data
				prev = self.root
				current = self.root

			else:
				if st[i] == '<':
					prev = current
					current = current.lchild

				if st[i] == '>':
					prev = current
					current = current.rchild

		return s

				

	# the encrypt() function will take a string as input parameter, 
	# convert it to lower case, and return the encrypted string. 
	# It will ignore all digits, punctuation marks, and special characters.
	def encrypt (self, st):
		string = st.lower()
		encrypt_st = ''
		for i in string:
			encrypt_st +=self.search(i) + '!'  # add '!' in between i values
		return encrypt_st[:-1]  # gets rid of last "!

	# the decrypt() function will take a string as input parameter and
	# return the decrypted string.
	def decrypt (self, st):
		st += '!'
		return self.traverse(st)

def main():
        # Test key --> output when encrypted == "*!<!<!>!<<!*!<"
        key = input('Enter encryption key: ')
        key = Tree(key)
        
        # prompt user to input string
        encrypt_string = input('\nEnter string to be encrypted: ')
        print("Encrypted string: ", key.encrypt(encrypt_string))
        print()
        decrypt_string = input('Enter string to be decrypted: ')
        print("Decrypted string: ",key.decrypt(decrypt_string))


if __name__ == '__main__':
    main()


















