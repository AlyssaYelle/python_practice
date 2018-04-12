import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import colors as mcolors

if __name__ == '__main__':
	#import data
	df = pd.read_csv('data/jan_activity.csv', header = 0)
	df = df[:13]
	print df.describe()

	
	print df.mean(axis=0)	


	plt.scatter(df['active_calories'],df['resting_calories'])
	plt.xlabel('calories burned during physical activity')
	plt.ylabel('calories burned at rest')
	plt.savefig('./plots/act_vs_rest.pdf', bbox_inches='tight')
	plt.close()

	plt.scatter(df['exercise_minutes'], df['resting_calories'], color = 'pink')
	plt.xlabel('minutes of exercise')
	plt.ylabel('calories burned at rest')
	plt.savefig('./plots/xmins_v_bmr.pdf', bbox_inches='tight')
	plt.close()

	plt.scatter(df['exercise_minutes'], df['resting_calories'], color = 'pink')
	plt.scatter(df['exercise_minutes'], df['active_calories'], color = 'purple')
	plt.xlabel('minutes of exercise')
	plt.legend(loc = 'lower right')
	plt.savefig('./plots/xmins_v_allcals.pdf', bbox_inches='tight')
	plt.close()

	plt.scatter(df['stand_hours'], df['steps'])
	plt.xlabel('stand hours')
	plt.ylabel('total number of daily steps')
	plt.savefig('./plots/stand_v_steps.pdf', bbox_inches='tight')
	plt.close()

	plt.hist(df['steps'], bins=6)
	plt.xlabel('total number of daily steps')
	plt.ylabel('frequency')
	plt.savefig('./plots/steps_freq.pdf', bbox_inches='tight')
	plt.close()

	df.cumsum()
	plt.figure(); df.plot(); plt.legend(loc='best')
	plt.show()
	plt.close()
	#plt.savefig('time_series.pdf', bbox_inches='tight')





