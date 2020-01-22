'''
Program to generate a foster animal after user inputs information about their household
'''

import math


# Pet super class
class Pet:

	# constructor
	def __init__(self, age, weight, behavioral_issue = None):
		self.age = age
		self.weight = weight
		self.behavioral_issue = behavioral_issue

	# display age in years if older than 1, convert to months otherwise
	def describe_age(self):
		age = str(self.age) if self.age >= 1 else str(math.floor(self.age * 12))
		scale = "year old" if self.age > 1 else "month old"
		return age + " " + scale

	# describe behavioral issues, if they exist
	def describe_behavior(self):
		if self.behavioral_issue is None:
			return "I don't have any behavioral issues, please help me keep up the good work!"
		else:
			return "I am a little bit " + str(self.behavioral_issue) + ". Please help me work on my manners!"

	# placeholder speak method -- should be updated in child class
	def speak(self):
		print("Hi there!")

	def greet(self):
		self.speak()
		print("I am a " + self.size_descriptive + " " + self.describe_age() + " " + self.age_descriptive + ". " + self.describe_behavior())


# Dog class is child of Pet class
class Dog(Pet):

	# constructor
	def __init__(self, age, weight, behavioral_issue = None):
		# adding on to pet constructor
		Pet.__init__(self, age, weight, behavioral_issue = None)
		self.size_descriptive = "large" if weight >= 50 else "small"
		self.age_descriptive = "dog" if age >= 1 else "puppy"


	def speak(self):
		speak = "Woof!" if self.age >= 1 else "Arf!"
		print(speak)


# Application class
class Application:
	def __init__(self):
		self.dog_acceptance = {adult: True, baby: True, behavioral_issues: True}
		self.cat_acceptance = {adult: True, baby: True, behavioral_issues: True}
		self.passes_dog_criteria = True
		self.passes_cat_criteria = True

	def survey1(self):
		pass

	def dog_survey(self):
		pass

	def cat_survey(self):
		pass








if __name__ == "__main__":
	print("Welcome to Alyssa's Furry Friend Rescue! \n")
	my_dog = Dog(.5, 20, "mouthy")
	my_dog.greet()





