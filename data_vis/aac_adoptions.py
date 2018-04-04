'''
summarize imformation about the ages of pets adopted from the Austin Animal Center
-what is the distribution of ages in months for all the pets upon outcome
-what is the distribution of ages for dogs and cats separately
-how do adoption rates change as a function of month? how about for each pet type?
***make a heatmap showing adoption rates for age vs number of years
'''

import numpy as np
import matplotlib.pylab as plt
import pandas as pd
from matplotlib import colors as mcolors



if __name__ == '__main__':
	#import data
	df = pd.read_csv('data/train_hw.csv', header = 0)
	df.dropna(inplace = True)


	
	#get data for live dogs and live cats
	AgeuponOutcomeInMonths = df['AgeuponOutcomeInMonths']
	is_dog = df['AnimalType'] == 'Dog'
	is_cat = df['AnimalType'] == 'Cat'
	live_outcome = df['OutcomeType'] != 'Euthanasia'
	

	live_dogs = is_dog & live_outcome
	live_cats = is_cat & live_outcome

	#numpy version of the age upon outcome of live dogs/cats
	age_live_dogs = df[live_dogs]['AgeuponOutcomeInMonths']
	age_live_cats = df[live_cats]['AgeuponOutcomeInMonths']

	plt.hist(AgeuponOutcomeInMonths, label = 'all pets', color = 'indigo', alpha = 0.5, bins = 20)
	plt.hist(age_live_cats, label = 'cats only', color = 'thistle', alpha = 0.5, bins = 20)
	plt.hist(age_live_dogs, label = 'dogs only', color = 'tomato', alpha = 0.5, bins = 20)
	plt.xlabel('Age in Months')
	plt.ylabel('Adoptions')
	plt.legend(loc = 'upper right')
	plt.show()
	plt.close()

	outcome_months = df['OutcomeMonth']

	plt.hist(outcome_months, bins = 12)
	plt.xlabel('Month of Year')
	plt.ylabel('# Adoptions')
	plt.show()
	plt.close()





















