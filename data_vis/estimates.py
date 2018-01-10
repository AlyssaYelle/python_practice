'''
load data.csv into numpy
plot histogram of data
what is eyeball estimate of the mean?
what is eyeball estimate of var, sd?
'''

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import colors as mcolors

if __name__ == '__main__':
	#import data
	df = pd.read_csv('data/data.csv', header = 0)

	
	plt.hist(df['data'], color = 'thistle', bins = 20)
	plt.xlabel('Frequency')
	plt.ylabel('Data value')
	plt.axvline(0.25, color = 'mediumvioletred')
	plt.axvline(2.25, color = 'palevioletred')
	plt.axvline(-1.75, color = 'palevioletred')
	plt.axvline(4.25, color = 'pink')
	plt.axvline(-3.75, color = 'pink')
	plt.axvline(6.25, color = 'linen')
	plt.axvline(-5.75, color = 'linen')
	plt.show()
	plt.close()





























