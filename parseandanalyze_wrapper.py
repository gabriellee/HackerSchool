#!/usr/bin/env python
import parsedata
import learningstyles_distribution2
import thinkbayes2
import thinkplot
import sys.argv

def main(path, active_hypo):
	'''initializes an instance of a learning styles probability distribution
	updates the probability distribution based on data
	checks the strength of the evidence that the distribution in hacker school is substantiallly different
	
	path is the path of the csv containing the data
	sensing data is a tuple in which the first value is the number of people who are sensing and the second value is the number of people who are intuitive in a set of hacker school students
	sensing_hypo is the initial guess representing the integer probability of a hacker school student being sensing
	sensing_ratio is the integer probability of any person being sensing'''

	studentdict = parsedata.ParseCsv(path)
	sensing_data = [0,0]
	for student in studentdict
:		if studentdict[student][0] == 1:
			active_data[0] +=1
		elif studentdict[student][1] == -1:
			sensing_data[1] += 1


	
	active_prob = 50

	#set a uniform prior
	active_dist = learningstyles_distribution2.StyleDist(range(0,101))
	#update with new data
	active_dist.Update(active_data)
	#generate graph of probability distribution
	thinkplot.Pmf(active_dist)
	#thinkplot.Pmf(learningstyles_distribution2.StyleDist())
	
	#Is this substantially different from the overall population?
	#To find out, we will compute Bayes' Factor!
	#p(D|H) / p(D|~H)
	
	#find the likelihood that hacker school students are as likely to be sensing as a member of the general population
	suite = learningstyles_distribution2.StyleDist()
	like_same = suite.Likelihood(active_data, active_prob)
	print('p(D|50%)', like_same)

	#set p(D|~H)
	#I define ~H as the set of all hypotheses (sensing probabilities) excluding sensing_prob (the probability of being sensing in the general population)
	b_uniform = learningstyles_distribution2.StyleDist(range(0,101))
	b_uniform.Remove(sensing_prob)
	b_uniform.Normalize()
	
	like_diff = b_uniform.SuiteLikelihood(sensing_data)
	bayes_factor = like_same/like_diff
	print('Bayes Factor is ', bayes_factor)

	# %matplotlib inline
	#thinkplot.Pmf(sensing_dist)
	#return sensing_dist

#	 check = learningstyles_distribution2.StyleDist(range(101))
#	 check.Update(sensing_data)
#	 thinkplot.Pmf(check)
#	 print check.Likelihood()

if __name__ == "__main__":

	main('/home/gabrielle/wkspace/HackerSchool/pseudodata.csv',50)
	#main(sys.argv[1],sys.argv[2])