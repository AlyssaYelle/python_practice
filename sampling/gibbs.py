'''
Given N observations X = {x_1,...,x_N} where x_i ~ N(mu, s^2) s.t. mu, s^2 unknown
mu ~ N(v,t)
1/s^2 ~ Gamma(a,b)
Calculate posteriors for mu and s^2
write a Gibbs sampler to sample the joint posterior distribution over m u and s^2
draw 300 samples with 100 burn-in and plot a scatter plot of mu vs s^2
'''


#currently something is wrong with the variance posterior


import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import colors as mcolors

if __name__ == '__main__':
	#import data
	df = pd.read_csv('data/data.csv', header = 0)

	posterior = []
	post_mus = []
	post_vars = []
	n = 300

	sample_mean = df['data'].mean()

	#prior hyperparameters
	nu = 0
	tau = 1
	a = 0.1
	b = 0.1

	#initialize mu and precision
	mu = 1
	precision = 0.25

	#parameters of mu's conditional posterior
	c_post_mean = (((n*sample_mean*precision)+(nu/tau))/((n*precision)+(1/tau)))
	c_post_var = 1/((n*precision)+(1/tau))
	c_post_std = np.sqrt(c_post_var)


	#parameters of precision's conditional posterior
	c_post_a =	n/2 + a
	

	for i in range (0,300):
		#sample from the conditional posterior of mu and update mu
		mu = np.random.normal(c_post_mean, c_post_std)
		c_post_b = b + 0.5*((df['data']-mu)**2).sum()
		
		#sample from the conditional posterior of precision and let that value be the new precision
		precision = np.random.gamma(c_post_a, c_post_b)

		#parameters of mu's conditional posterior
		c_post_mean = (((n*sample_mean*precision)+(nu/tau))/((n*precision)+(1/tau)))
		c_post_var = 1/((n*precision)+(1/tau))
		c_post_std = np.sqrt(c_post_var)

		variance = 1/precision
		post_mus.append(mu)
		post_vars.append(variance)
		posterior.append((mu, variance))
		


	#plot the mus and vars
	'''
	plt.hist(post_vars, bins = 20)
	plt.show()
	plt.close()
	'''

	plt.hist(post_mus, bins = 20)
	plt.show()
	plt.close()


































