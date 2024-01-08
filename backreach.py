import pandas as pd
import numpy as np

def conditions_product(df1,df2):
	'''
	Truth table for functions 1 AND 2 given the input truth tables 
	for function 1 and function 2. The inputs need to be dataframes with column names 
	corresponding to the the labes of the nodes.
	'''

	# Firts check if the two function share input nodes

	shared_columns = list(set(df1.columns) & set(df2.columns))

	if len(shared_columns) == 0:
		#if they don't, take all possible products of conditions
		merged_df = pd.merge(df1, df2, how = 'cross')
	else:
		#if they do, just keep the non conflicting ones
		merged_df = pd.merge(df1, df2, on = shared_columns)

	merged_df = merged_df.sort_index(axis=1)

	return merged_df

'''
the following functions are just utils for the generation of random 
truth tables
'''

def generate_random_dataframe(k, n, m):
	'''
	Given a number k, and n greater than k I need a dataframe with k columns. 
	The column names are random numbers between 1 and n. There are m rows. 
	All entries are either 0 or 1, each with probability 50%.
	'''
	# Generate random column names
	column_names = np.random.choice(range(1, n+1), k, replace=False)
	
	# Create a DataFrame with k columns and m rows
	df = pd.DataFrame(columns=column_names, index=range(m))
	
	# Populate the DataFrame with 0s and 1s with a 50% probability
	df = df.applymap(lambda x: np.random.choice([0, 1], p=[0.5, 0.5]))
	
	# As it stands, the code could generate duplicate rows. let's remove them.
	df = df.drop_duplicates()
	
	#sort the columns
	df = df.sort_index(axis=1)
	
	return df

def generate_and_find_closest(avg, n):
	'''
	given integers avg and n > avg, 
	generate random integers (internal parameter num_sampling), 
	then select the one closest to avg.
	This function is used twice:
	1) To determine the number of inputs for the boolean functions 
	in the updating rule.
	2) To determine the number of correct inputs in the truth table
	'''

	# Generate random integers
	
	num_sampling = int(n/3)+1 # just an example

	random_integers = np.random.randint(1, n+1, size = num_sampling)

	# Find the integer closest to mean_kin
	closest_integer = min(random_integers, key=lambda k: abs(k - avg))

	return closest_integer



