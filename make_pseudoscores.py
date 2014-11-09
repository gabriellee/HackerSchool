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
w = csv.writer(open("pseudoscores.csv", "w"))
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
w = csv.writer(open("pseudoscores.csv", "w"))

def MakeData(number_of_students, actref_dist,senint_dist,visver_dist,seqglo_dist):

	# Range of possible values.
	#-11 through 11, distributed according to a gaussian
	# -1 = active/sensing/visual/global
	# +1 = reflective/intuitive/verbal/sequential
	xk = (-1,1)
	
	# Create random number generators that spit out numbers
	# according to their pre-set distributions.
	# actref_custm = stats.rv_discrete(name = 'actref_custm', values=(xk,actref_dist))
	# senint_custm = stats.rv_discrete(name = 'senint_custm', values=(xk,senint_dist))
	# visver_custm = stats.rv_discrete(name = 'visver_custm', values=(xk,visver_dist))
	# seqglo_custm = stats.rv_discrete(name = 'seqglo_custm', values=(xk,seqglo_dist))


	for i in range(number_of_students):
		#generate a fake name
		name = ''.join(random.choice(string.letters) for h in range(14))
		#generate a learning styles profile
		act_ref = int(np.random.normal(actref_dist))
		if act_ref > 11:
			act_ref = 11
		elif act_ref < -11:
			act_ref = -11

		sen_int = int(np.random.normal(senint_dist))
		if sen_int > 11:
			sen_int = 11
		elif sen_int < -11:
			sen_int = -11

		vis_ver = int(np.random.normal(visver_dist))
		if vis_ver > 11:
			vis_ver = 11
		elif vis_ver < -11:
			vis_ver = -11

		seq_glo = int(np.random.normal(seqglo_dist))
		if seq_glo > 11:
			seq_glo = 11
		elif seq_glo < -11:
			seq_glo = -11

		# Uncomment for debug code
		print name, act_ref, sen_int, vis_ver, seq_glo

		# Write to file
		w.writerow([name, act_ref, sen_int, vis_ver, seq_glo])

if __name__ == "__main__":
	# Desired frequency distributions of the data.
	# All numbers in a set must sum to 1.
	#the first value in each dist is the mean of the standard dev
	#the second value is the standard deviation
	actref_dist = (0, .3)
	senint_dist = (5, .3)
	visver_dist = (.8, .3)
	seqglo_dist = (-5, .3)

	# Desired number of students to generate
	number_of_students = 100

	MakeData(number_of_students, actref_dist, senint_dist, visver_dist, seqglo_dist)
def MakeData(number_of_students, actref_dist,senint_dist,visver_dist,seqglo_dist):

	# Range of possible values.
	# -1 = active/sensing/visual/global
	# +1 = reflective/intuitive/verbal/sequential
	xk = (-1,1)
	
	# Create random number generators that spit out numbers
	# according to their pre-set distributions.
	actref_custm = stats.rv_discrete(a=-11, b=11, name = 'actref_custm', inc = 2, )


	actref_custm = stats.rv_discrete(name = 'actref_custm', values=(xk,actref_dist))
	senint_custm = stats.rv_discrete(name = 'senint_custm', values=(xk,senint_dist))
	visver_custm = stats.rv_discrete(name = 'visver_custm', values=(xk,visver_dist))
	seqglo_custm = stats.rv_discrete(name = 'seqglo_custm', values=(xk,seqglo_dist))


	for i in range(number_of_students):
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
	number_of_students = 100

	MakeData(number_of_students, actref_dist, senint_dist, visver_dist, seqglo_dist)