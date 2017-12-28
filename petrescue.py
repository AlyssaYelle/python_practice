'''
pet rescue
you can adopt a snake, dog, or kitten
you can name your pet and give them a treat
after pet is fed, print out names of pets by reading their collar
'''

class Shelter:
	def __init__(self, pet_inventory):
		pass


class PetAdopter:
	def __init__(self):
		pass

	#adopter selects the type of pet they want to adopt
	def adopt(self, shelter):
		pass		

	#adopter names their pet
	def name(self, pet_name):
		pass

	#adopter feeds the pet
	def give_treat(self, treat):
		pass


class Pet:
	def __init__(self, collar):
		self.collar = collar 

	def speak(self):
		pass

	def eat(self, treat):
		self.speak()
		print 'I love', treat


class Snake(Pet):
	def __init__(self, collar):
		Pet.__init__(self, collar)

	def speak(self):
		print 'Hissss'

class Doggo(Pet):
	def __init__(self, collar):
		Pet.__init__(self, collar)

	def speak(self):
		print 'Woof!'


class Kitten(Pet):
	def __init__(self, collar):
		Pet.__init__(self, collar)

	def speak(self):
		print 'Purrrr'


class Collar:
	def __init__(self, pet_name):
		self.name = pet_name


if __name__ == '__main__':
	treat = 'food'
	pet_name = 'Sssssssylvessster'
	collar = Collar(pet_name)
	pet = Snake(collar)
	pet.eat(treat)
	print 'my name is', collar.name