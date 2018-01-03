'''
data visualization things
'''

import numpy as np
import matplotlib.pylab as plt
import pandas as pd



if __name__ == '__main__':

	#generate fake data
	x = np.random.normal(np.arange(100))
	y = np.random.multivariate_normal([0.5,1], [[1.2,0.4], [0.4,0.5]], size = 100)
	z = np.concatenate([x[:,np.newaxis],y], axis=1)

	#create our plot
	plt.plot(z[:,0], label = 'Dim 0', color='gray', ls='--')
	plt.plot(z[:,1], label = 'Dim 1')
	plt.plot(z[:,2], label = 'Dim 2', color='lavender')
	
	#default plot does not have a legend so we must make one
	plt.legend(loc = 'upper left')

	#gives plot a title
	plt.title('My data')

	#labels
	plt.xlabel('Index of data')
	plt.ylabel('Data value')

	#shows the plot
	#plt.show()
	#we must EITHER show or savefig, we can't do both
	#if we would rather save figure to file instead of showing it
	plt.savefig('mydata.pdf', bbox_inches='tight')

	#we need to close the plot or else subsequent plots will be drawn to the same canvas
	plt.close()

	#scatter plot of col 1 vs col 2
	plt.scatter(z[:,1], z[:,2])

	#plot a horizontal line
	plt.axhline(0.1)
	#plot a vertical line
	plt.axvline(0.5)

	plt.savefig('myscatter.pdf', bbox_inches='tight')
	plt.close()

	#we can also make a heat map
	w = np.histogram2d(z[:,1], z[:,2], bins=10)[0]
	plt.imshow(w)
	plt.savefig('myheatmap.pdf', bbox_inches='tight')
	plt.close()

	#histograms
	#alpha sets the color transparency
	plt.hist(z[:,0], alpha=0.5, bins=np.linspace(0,1,20))
	plt.hist(z[:,1], alpha=0.5, bins =20)
	plt.hist(z[:,2], alpha=0.5, bins=20)
	plt.savefig('myhistograms.pdf', bbox_inches='tight')
	plt.close()

	#pandas stuff

	#header = 0 says first line is the header line
	df = pd.read_csv('train.csv', header = 0)

	#we can print out a summary
	print df.describe()

	#access all of the names
	names = df['Name']
	

	for name in names.astype(str):
		if name.startswith('K'):
			print name


	print df['AgeuponOutcome']

	#get the color col
	colors = df['Color']
	#create a binary vector with True for all entries in Color that have the value 'brown'
	is_brown = df['Color'] == 'Brown'
	#select all rows that contain brown animals using the is_brown mask
	brown_only = df[is_brown]
	#same thing but more succinct
	brown_only = df[df['Color']=='Brown']

	#white animals mask
	is_white = df['Color'] == 'White'
	#logical OR operation (pipe = OR, ampersand = AND, ~ = NOT)
	is_brown_or_white = is_brown | is_white
	#all white or brown animals not named Rocket
	brown_or_white_no_rockets = df[((df['Color'] == 'Brown') | (df['Color'] == 'White')) &  ~(df['Name'] == 'Rocket')] 

	df_numpy = df.values #numpy matrix but NO COL HEADERS
	
























