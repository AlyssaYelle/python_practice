import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import colors as mcolors
import matplotlib.dates as mdates
from pandas import Series, DataFrame, Panel
from pandas.plotting import lag_plot, autocorrelation_plot, bootstrap_plot, parallel_coordinates

if __name__ == '__main__':
	#import data
	df = pd.read_csv('data/semester_data.csv', header = 0)
	#print df.describe()
	dates = pd.date_range('2018-01-19', periods=df.shape[0], freq='D')

	df.index = dates
	del df['date_index']

	plt.scatter(df['active_calories'], df['resting_calories'])
	plt.title('Active calories burned vs. resting calories burned')
	plt.savefig('act_rest_cals.pdf', bbox_inches='tight')
	plt.close()

	plt.scatter(df['exercise_minutes'], df['resting_calories'])
	plt.title('Total exercise minutes vs. resting calories burned')
	plt.savefig('ex_rest_cals.pdf', bbox_inches='tight')
	plt.close()



	steps = df['steps']
	steps.cumsum()
	plt.figure(); steps.plot(); plt.legend(loc='best')
	plt.savefig('steps.pdf', bbox_inches='tight')
	plt.close()

	cals1 = df['resting_calories']
	cals2 = df['active_calories']
	cals3 = df['total_calories']
	exercise_minutes = df['exercise_minutes']
	cals1.cumsum()
	cals2.cumsum()
	cals3.cumsum()
	exercise_minutes.cumsum()
	plt.figure(); cals1.plot(); cals2.plot(); cals3.plot(); exercise_minutes.plot(); plt.legend(loc='best')
	plt.savefig('exercise_calories.pdf', bbox_inches='tight')
	plt.close()

	resting_HR = df['resting_hr']
	sleep_hours = df['sleep']
	resting_HR.cumsum()
	sleep_hours.cumsum()
	plt.figure(); resting_HR.plot(); sleep_hours.plot(); plt.legend(loc='best')
	plt.savefig('sleep_hr.pdf', bbox_inches='tight')
	plt.close()

	stand_hours = df['stand_hours']
	distance_walked = df['walk_distance']
	stand_hours.cumsum()
	distance_walked.cumsum()
	plt.figure(); stand_hours.plot(); distance_walked.plot(); plt.legend(loc='best')
	plt.savefig('stand_walk.pdf', bbox_inches='tight')
	plt.close()

	bootstrap_plot(steps, size=30, samples=100, color='grey')
	plt.savefig('steps_bootstrap.pdf', bbox_inches='tight')
	plt.close()

	bootstrap_plot(cals3, size=30, samples=100, color='grey')
	plt.savefig('total_calories_bootstrap.pdf', bbox_inches='tight')
	plt.close()

	bootstrap_plot(exercise_minutes, size=30, samples=100, color='grey')
	plt.savefig('ex_mins_bootstrap.pdf', bbox_inches='tight')
	plt.close()

	bootstrap_plot(cals1, size=30, samples=100, color='grey')
	plt.savefig('rest_cals_bootstrap.pdf', bbox_inches='tight')
	plt.close()


	del df['steps']
	del df['total_calories']
	del df['stand_hours']
	del df['resting_calories']
	plt.figure(); parallel_coordinates(df, 'resting_hr')
	plt.title('Parallel coordinates plot, resting HR')
	plt.savefig('HR_clusters.pdf', bbox_inches='tight')
	plt.close()

	plt.figure(); parallel_coordinates(df, 'sleep')
	plt.title('Parallel coordinates plot, sleep hours')
	plt.savefig('sleep_clusters.pdf', bbox_inches='tight')
	plt.close()

	lag_plot(cals1)
	plt.show()
	plt.close()
	autocorrelation_plot(cals1)
	plt.savefig('autocor_rest_cals.pdf', bbox_inches='tight')
	plt.close()
'''
	lag_plot(resting_HR)
	plt.show()
	plt.close()
	autocorrelation_plot(resting_HR)
	plt.show()
	plt.close()

	lag_plot(sleep_hours)
	plt.show()
	plt.close()
	autocorrelation_plot(sleep_hours)
	plt.show()
	plt.close()

	lag_plot(steps)
	plt.show()
	plt.close()
	autocorrelation_plot(steps)
	plt.show()
	plt.close()

	plt.hist(df['steps'], bins=20)
	plt.xlabel('total number of daily steps')
	plt.ylabel('frequency')
	plt.show()
	plt.close()

	plt.scatter(df['exercise_minutes'], df['resting_calories'], color = 'pink')
	plt.scatter(df['exercise_minutes'], df['active_calories'], color = 'purple')
	plt.scatter(df['exercise_minutes'], df['total_calories'], color = 'green')
	plt.xlabel('minutes of exercise')
	plt.legend(loc = 'lower right')
	plt.show()
	plt.close()

	plt.scatter(df['exercise_minutes'], df['resting_calories'])
	plt.xlabel('minutes of exercise')
	plt.ylabel('calories burned at rest')
	plt.show()
	plt.close()

	plt.scatter(df['date_index'], df['resting_hr'])
	plt.xlabel('Day of semester')
	plt.ylabel('Resting HR')
	plt.show()
	plt.close()
'''
