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
		scale = "year old" if self.age >= 1 else "month old"
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

	# dog survey collects information about user's dog preferences
	def dog_survey(self):

		# initialize range of weights and ages
		age_range = [0,0]
		weight_range = [5, 50]

		# prompt user to enter a minimum age
		min_age = int(input("Please enter the minimum age (in years) dog you're willing to foster (minumum value 0, maximum value 17):  "))

		# prompt again if user enters value out of range
		while (min_age not in range(0, 18)):
			print("Invalid input. Please enter a number between 0 and 17.")
			min_age = int(input("Please enter the minimum age (in years) dog you're willing to foster (minumum value 0, maximum value 17):  "))

		# build max age prompt based on user's input for min age
		max_age_input_message = "Please enter the maximum age (in years) dog you're willing to foster (minumum value " + str(min_age) + ", maximum value 17):  "

		# prompts user to enter a maximum age
		max_age = int(input(max_age_input_message))

		# prompt again if user enters value out of range
		while (max_age not in range(0, 18)) | (max_age < min_age):
			print("Invalid input. Please enter a number between " + str(min_age) + " and 17.")
			max_age = int(input(max_age_input_message))

		# update user's age preference range
		age_range[0] = min_age
		age_range[1] = max_age

		# prompt user to enter whether they are okay with a large dog
		large_dogs_survey_input = input("Can you foster a large adult (> 50lbs) dog? (y/n):  ")

		# prompt again if user input is invalid
		while large_dogs_survey_input not in ["y", "Y", "n", "N"]:
			print("Invalid input. Please enter y or n")
			large_dogs_survey_input = input("Can you foster a large adult (> 50lbs) dog? (y/n):  ")

		# update weight range based on user's reponse
		weight_range[1] = 120 if large_dogs_survey_input in ["y", "Y"] else 50

		# prompt user to enter whether they can walk dog 3 or more times per day
		can_walk_dog = input("Can you commit to walking your foster dog at least 3 times a day? (y/n):  ")

		# prompt again if user input is invalid
		while can_walk_dog not in ["Y", "y", "n", "N"]:
			print("Invalid input. Please enter y or n")
			can_walk_dog = input("Can you commit to walking your foster dog at least 3 times a day? (y/n):  ")

		# append dog preferences to foster_specs only if user can commit to 3 dog walks per day
		if can_walk_dog in ["y", "Y"]:
			self.foster_specs.append(["dog", age_range, weight_range])


	# cat survey collects information about user's cat preferences
	def cat_survey(self):

		# initialize range of weights and ages
		age_range = [0,0]
		weight_range = [0.5, 10]

		# prompt user to enter a minimum age
		min_age = int(input("Please enter the minimum age (in years) cat you're willing to foster (minumum value 0, maximum value 20):  "))

		# prompt again if user enters value out of range
		while (min_age not in range(0, 21)):
			print("Invalid input. Please enter a number between 0 and 20.")
			min_age = int(input("Please enter the minimum age (in years) cat you're willing to foster (minumum value 0, maximum value 20):  "))

		# build max age prompt based on user's input for min age
		max_age_input_message = "Please enter the maximum age (in years) cat you're willing to foster (minumum value " + str(min_age) + ", maximum value 20):  "

		# prompts user to enter a maximum age
		max_age = int(input(max_age_input_message))

		# prompt again if user enters value out of range
		while (max_age not in range(0, 18)) | (max_age < min_age):
			print("Invalid input. Please enter a number between " + str(min_age) + " and 20.")
			max_age = int(input(max_age_input_message))

		# update user's age preference range
		age_range[0] = min_age
		age_range[1] = max_age

		# update maximum weight range if user is open to fostering cats 1 yr or older
		if max_age >= 1:
			weight_range[1] = 19


		# prompt user to enter whether they will keep cat indoors
		cat_indoors = input("Can you commit to keeping your cat or kitten indoors at all times? (y/n):  ")

		# prompt again if user input is invalid
		while cat_indoors not in ["Y", "y", "n", "N"]:
			print("Invalid input. Please enter y or n")
			cat_indoors = input("Can you commit to keeping your cat or kitten indoors at all times? (y/n):  ")

		# append cat preferences to foster_specs only if user can commit to keeping cat indoors
		if cat_indoors in ["y", "Y"]:
			self.foster_specs.append(["cat", age_range, weight_range])


	# process survey to determine eligility
	def survey_results(self):

		# if foster_specs length = 0 then user did not meet foster requirements
		if len(self.foster_specs) == 0:
			print("We cannot approve your application at this time. Please review our foster requirements and check back later! :)\nCat requirements: Foster must keep cat indoors at all times.\nDog requirements: Foster must commit to walking dog at least 3 times per day.")
			return
		else:
			print("\nCongratulations! Meet your new foster pet. :)\n")

		# generate an animal if user is accepted as foster
		self.generate_foster_animal()

	# randomly generate a foster animal
	def generate_foster_animal(self):

		# randomly select cat or dog (if they qualify for both, otherwise this will return the sole animal type they qualified for)
		animal_type = self.foster_specs[random.randint(0, len(self.foster_specs)-1)]
		
		# generate random age within user's age preferences
		random_age = random.randint(animal_type[1][0], animal_type[1][1])

		# generate random age in months if random age < 1
		animal_age = random_age if random_age >= 1 else random.random()

		# generate random animal weight based on user's size preferences
		animal_weight = random.uniform(animal_type[2][0], animal_type[2][1]) if animal_age >= 1 else (random.uniform(animal_type[2][0], animal_type[2][1])) / 2

		# create the pet
		foster_pet = Dog(animal_age, animal_weight) if animal_type[0] == 'dog' else Cat(animal_age, animal_weight)

		# the pet greets the user
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






