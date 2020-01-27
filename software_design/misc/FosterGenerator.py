'''
Written and tested in Python 3.7 by Alyssa Jones

Program to generate a foster animal after user inputs information about their household
'''

import math
import random


# abstract Pet class
class Pet:

	# constructor
	def __init__(self, age, weight):
		self.age = age
		self.weight = weight


	# display age in years if older than 1, convert to months otherwise
	def describe_age(self):
		age = str(self.age) if self.age >= 1 else str(math.floor(self.age * 12))
		scale = "year old" if self.age > 1 else "month old"
		return age + " " + scale


	# require speak method to be defined in child classes
	def speak(self):
		raise NotImplementedError

	# require describe_self method to be defined in child classes
	def describe_self(self):
		raise NotImplementedError

	# method to make pet speak and describe themself to user
	def greet(self):
		self.speak()
		self.describe_self()



# Dog class is child of Pet class
class Dog(Pet):

	# method to make dog 'speak' (make a noise)
	def speak(self):

		# Adult dogs (>= 1 yr old) say 'woof'
		# Puppies (< 1 yr old) say 'arf'
		speak = "Woof!" if self.age >= 1 else "Arf!"

		print(speak)

	# method to describe dog based on age and weight
	def describe_self(self):

		# large dog defined by weight >= 50
		size_descriptive = "large" if self.weight >= 50 else "small"

		# adult dog defined by age >= 1
		age_descriptive = "dog" if self.age >= 1 else "puppy"

		print("I am a " + size_descriptive + " " + self.describe_age() + " " + age_descriptive + ".")


# Cat class is child of Pet class
class Cat(Pet):

	# method to make cat 'speak' (make a noise)
	def speak(self):

		# Adult cats (age >= 1) say 'meoww'
		# Kittens (age < 1) say 'mew'
		speak = "Meowww!" if self.age >= 1 else "Mew!"

		print(speak)

	# method to describe cat based on age and weight
	def describe_self(self):

		# chonky cat defined by weight > 14
		size_descriptive = "chonky" if self.weight > 14 else "healthy"

		# adult cat defined by age >= 1
		age_descriptive = "cat" if self.age >= 1 else "kitten"

		print("I am a " + size_descriptive + " " + self.describe_age() + " " + age_descriptive + ".")


# Application class
class Application:
	def __init__(self):
		self.dogs_OK = False
		self.cats_OK = False
		self.foster_specs = []

	# method for basic survey to determine interest in dogs and/or cats
	def take_survey(self):

		# check if dogs are OK
		open_to_dogs = input("Are you open to fostering a dog? (y/n): ")

		# handle invalid input
		while open_to_dogs not in ["y", "Y", "n", "N"]:
			print("Invalid input. Please enter y or n")
			open_to_dogs = input("Are you open to fostering a dog? (y/n): ")

		# update self.dogs_OK if user enters y or Y
		self.dogs_OK = True if open_to_dogs in ["y", "Y"] else self.dogs_OK

		# only display dog survey if dogs are OK
		if self.dogs_OK == True:
			self.dog_survey()

		# check if cats are OK
		open_to_cats = input("Are you open to fostering a cat? (y/n): ")

		# handle invalid input
		while open_to_cats not in ["y", "Y", "n", "N"]:
			print("Invalid input. Please enter y or n")
			open_to_cats = input("Are you open to fostering a cat? (y/n): ")

		# update self.cats_OK if user enters y or Y
		self.cats_OK = True if open_to_cats in ["y", "Y"] else self.cats_OK

		# only display cat survey if cats are OK
		if self.cats_OK == True:
			self.cat_survey()

		# exit if neither dogs nor cats are OK
		if not self.dogs_OK and not self.cats_OK:
			print("\nUnfortunately we only have cats and dogs at this time! Please check back later. :)")
			return

		# review survey
		self.survey_results()

	def dog_survey(self):

		# initialize range of weights and ages
		age_range = [0,0]
		weight_range = [5, 50]

		# collect user input and update ranges
		age_range[0] = int(input("Please enter the minimum age (in years) dog you're willing to foster (minumum value 0, maximum value 17):  "))
		age_range[1] = int(input("Please enter the maximum age (in years) dog you're willing to foster (minumum value 0, maximum value 17):  "))
		weight_range[1] = 120 if input("Can you foster a large adult (> 50lbs) dog? (y/n):  ") == "y" else (50 if age_range[1] >= 1 else 35)

		#passes_dog_criteria = True if input("Can you commit to walking your foster dog at least 3 times a day? (y/n):  ") == "y" else False

		if input("Can you commit to walking your foster dog at least 3 times a day? (y/n):  ") == "y":
			self.foster_specs.append(["dog", age_range, weight_range])



	def cat_survey(self):
		# initialize range of weights and ages
		age_range = [0,0]
		weight_range = [0.5, 5]

		# collect user input and update ranges
		age_range[0] = int(input("Please enter the minimum age (in years) cat you're willing to foster (minumum value 0, maximum value 20):  "))
		age_range[1] = int(input("Please enter the maximum age cat (in years) you're willing to foster (minumum value 0, maximum value 20):  "))

		if age_range[1] >= 1:
			weight_range[1] = 18

		#passes_cat_criteria = True if input("Can you commit to keeping your cat or kitten indoors at all times? (y/n):  ") == 'y' else False

		if input("Can you commit to keeping your cat or kitten indoors at all times? (y/n):  ") == 'y':
			self.foster_specs.append(["cat", age_range, weight_range])



	def survey_results(self):


		if len(self.foster_specs) == 0:
			print("We cannot approve your application at this time. Please review our foster requirements and check back later! :)\nCat requirements: Foster must keep cat indoors at all times.\nDog requirements: Foster must commit to walking dog at least 3 times per day.")
			return
		else:
			print("\nCongratulations! Meet your new foster pet :)\n")

		self.generate_foster_animal()


	def generate_foster_animal(self):
		animal_type = self.foster_specs[random.randint(0, len(self.foster_specs)-1)]
		
		random_age = random.randint(animal_type[1][0], animal_type[1][1])
		animal_age = random_age if random_age >= 1 else random.random()

		animal_weight = random.uniform(animal_type[2][0], animal_type[2][1])

		foster_pet = Dog(animal_age, animal_weight) if animal_type[0] == 'dog' else Cat(animal_age, animal_weight)

		foster_pet.greet()








if __name__ == "__main__":
	print("Welcome to Alyssa's Furry Friend Rescue! \n")
	# my_dog = Dog(5, 80)
	# my_dog.greet()
	# my_cat = Cat(0.2, 4)
	# my_cat.greet()
	app = Application()
	app.take_survey()
	# pet = Pet(4, 20)
	# pet.greet()






