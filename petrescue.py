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
	'''
	pet can make a noise dependent upon subclass
	pet can eat food
	pet learns to say its name
	'''
	def __init__(self, collar):
		self.collar = collar 

	def speak(self):
		pass

	def eat(self, treat):
		self.speak()
		print 'I love', treat

	def read_name(self):
		print 'My name is', self.collar.name


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
	#assigns a name to the pet via their collar
	def __init__(self, pet_name):
		self.name = pet_name


if __name__ == '__main__':

	#initial pet inventory
	#ideally should retrieve from a csv file
	pet_inventory = {"Snakes:" : 1, "Doggos:" : 1, "Kittens:" : 1}

	#ask user if they would like to adopt a pet
	text = raw_input("Welcome to Dr. Tasney's spooky pet rescue! Would you like to adopt a pet today? y/n \n")
	
	#exit if user doesn't want to adopt today
	if text == 'n':
		print 'Okay! Have a spooky day!'
		exit()
	
	else:

		#initialize list of newly adopted pets
		all_pets = []

		while True:
			print 'Here is our current inventory:', pet_inventory
			'''
			allow user to choose and name a pet
			add pet to the list of newly adopted pets
			update inventory as a type of pet is removed
			repeat until user is done adopting or inventory is depleted
			'''
			pet_choice = raw_input("Would you like a snake (s), doggo (d) or kitten (k)? \n")
			pet_name = raw_input("What would you like to name your new pet? \n")
			pet_treat = raw_input("What kind of treat would you like to feed your new pet? \n")
			more_pets = raw_input("Would you like to adopt another pet? (y/n) \n")
			
			all_pets.append((pet_choice, pet_name, pet_treat))

			if more_pets == 'n':
				break


		'''
		each new pet will:
		-make a noise depended upon their subclass
		-state their name
		-say they love food
		'''
		for pet in all_pets:
			collar = Collar(pet[1])
			if pet[0] == 's':
				new_pet = Snake(collar)
			elif pet[0] == 'd':
				new_pet = Doggo(collar)
			elif pet[0] == 'k':
				new_pet = Kitten(collar)
			treat = pet[2]
			new_pet.read_name()	
			new_pet.eat(treat)
				






	