#!/usr/bin/env python

'''
generates fake data based on a given ratio of learning styles

input:  
		each dist is a tuple of the probability of the first learning style and the probability of the second style
		ex: if actref_dist = (.3, .7), there is a 30 percent chance of an active learner and a 70 percent chance of a reflective learner


		'''

import random
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pickle
import csv
import string

# Open file for writing
w = csv.writer(open("pseudodata.csv", "w"))

def MakeData(actref_dist,senint_dist,visver_dist,seqglo_dist):

	# Range of possible values.
	# -1 = active/sensing/visual/global
	# +1 = reflective/intuitive/verbal/sequential
	xk = (-1,1)
	
	# Create random number generators that spit out numbers
	# according to their pre-set distributions.
	actref_custm = stats.rv_discrete(name = 'actref_custm', values=(xk,actref_dist))
	senint_custm = stats.rv_discrete(name = 'senint_custm', values=(xk,senint_dist))
	visver_custm = stats.rv_discrete(name = 'visver_custm', values=(xk,visver_dist))
	seqglo_custm = stats.rv_discrete(name = 'seqglo_custm', values=(xk,seqglo_dist))


	for i in range(students_to_generate):
		#generate a fake name
		name = ''.join(random.choice(string.letters) for h in range(14))
		#generate a learning styles profile
		act_ref = actref_custm.rvs()
		sen_int = senint_custm.rvs()
		vis_ver = visver_custm.rvs()
		seq_glo = seqglo_custm.rvs()

		# Uncomment for debug code
		print name, act_ref, sen_int, vis_ver, seq_glo

		# Write to file
		w.writerow([name, act_ref, sen_int, vis_ver, seq_glo])

if __name__ == "__main__":
	# Desired frequency distributions of the data.
	# All numbers in a set must sum to 1.
	actref_dist = (.5, .5)
	senint_dist = (.7, .3)
	visver_dist = (.8, .2)
	seqglo_dist = (.45, .65)

	# Desired number of students to generate
	students_to_generate = 100

	MakeData(actref_dist, senint_dist, visver_dist, seqglo_dist)