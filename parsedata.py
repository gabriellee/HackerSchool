#!/usr/bin/env python

'''parse data from csv into people class'''
import numpy as np
import re

class Student(act_ref,sen_int,vis_ver,seq_glo):
	def __init__(self):
		self.act_ref = act_ref
		self.sen_int = sen_int
		self.vis_ver = vis_ver
		self.seq_glo = seq_glo

def ParseCsv():
	'''parses data from csv genrated by learning styles survey into student objects with learning style info
	
	Each row is a person, column 1 contains names
	the other columns correspond to learning style categories and contain -1, 0, or 1

	-1 means that the person has the first learning style in the catgory(eg if the column is active v. reflective, a -1 means the person is active)
	1 means the person has the second learning style in the category
	0 means they are smack dab in the middle!

	Note: I used 
	http://stackoverflow.com/questions/3303312/how-do-i-convert-a-string-to-a-valid-variable-name-in-python#3303361 
	to turn a string into a variable name
	'''
	#specify file path here
	path = '/home/gabrielle/wkspace/HackerSchool/pseudodata.csv'
	n_cols = 5
	n_skip_rows = 0
	n_name_col = 1

	data = np.genfromtxt(path, skip_header = n_skip_rows, delimiter = ",", dtype = None)


	for i in range(n_cols):
		s = data[i,n_name_col]

		#clean up the name string so that it can be a variable name
		s = re.sub('[^0-9a-zA-Z_]', '', s)
		s = re.sub('^[^a-zA-Z_]+', '', s)

		vars()[s] = Student(data[i][n_name_col+1], data[i][n_name_col+2], data[i][n_name_col+3], data[i][n_name_col+4])

















def main():
	'''initializes an instance of a learning styles probability distribution
	updates the probability distribution based on data
	checks the strength of the evidence that the distribution in hacker school is substantiallly different
	
	sensing data is a tuple in which the first value is the number of people who are sensing and the second value is the number of people who are intuitive in a set of hacker school students
	sensing_hypo is the initial guess representing the integer probability of a hacker school student being sensing
	sensing_ratio is the integer probability of any person being sensing'''

	sensing_data = (50, 50)
	sensing_hypo = 50
	sensing_prob = 50

	#set a uniform prior
	sensing_dist = StyleDist(range(0,101))
	#update with new data
	sensing_dist.Update(sensing_data)
	#generate graph of probability distribution
	thinkplot.Pmf(sensing_dist)
	#thinkplot.Pmf(StyleDist())
	
	#Is this substantially different from the overall population?
	#To find out, we will compute Bayes' Factor!
	#p(D|H) / p(D|~H)
	
	#find the likelihood that hacker school students are as likely to be sensing as a member of the general population
	suite = StyleDist()
	like_same = suite.Likelihood(sensing_data, sensing_prob)
	print('p(D|50%)', like_same)

	#set p(D|~H)
	#I define ~H as the set of all hypotheses (sensing probabilities) excluding sensing_prob (the probability of being sensing in the general population)
	b_uniform = StyleDist(range(0,101))
	b_uniform.Remove(sensing_prob)
	b_uniform.Normalize()
	
	like_diff = b_uniform.SuiteLikelihood(sensing_data)
	bayes_factor = like_same/like_diff
	print('Bayes Factor is ', bayes_factor)

	# %matplotlib inline
	#thinkplot.Pmf(sensing_dist)
	#return sensing_dist

#	 check = StyleDist(range(101))
#	 check.Update(sensing_data)
#	 thinkplot.Pmf(check)
#	 print check.Likelihood()


