'''
Given N observations X = {x_1,...,x_N} where x_i ~ N(mu, s^2) s.t. mu, s^2 unknown
mu ~ N(v,t)
1/s^2 ~ Gamma(a,b)
Calculate posteriors for mu and s^2
write a Gibbs sampler to sample the joint posterior distribution over m u and s^2
draw 300 samples with 100 burn-in and plot a scatter plot of mu vs s^2
'''


import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import colors as mcolors



























