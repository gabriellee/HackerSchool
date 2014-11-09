#!/usr/bin/env python
import parsedata
import learningstyle
import thinkbayes2
import thinkplot
from numpy import mean 
from numpy import std
from numpy import linspace
from math import sqrt


def getHypos(data, num_stderrs = 3.0, num_points = 40):
	m = mean(data)
	s = std(data)

	m_err = m / sqrt(len(data))
	s_err = s / sqrt(2 * (len(data) - 1))

	m_spread = m_err * num_stderrs
	s_spread = s_err * num_stderrs

	mus = linspace(m - m_spread, m + m_spread, num_points)
	sigmas = linspace(s - s_spread, s + s_spread, num_points)

	return mus, sigmas

def main(path, active_hypo):
	'''initializes an instance of a learning styles probability distribution
	updates the probability distribution based on data
	checks the strength of the evidence that the distribution in hacker school is substantiallly different
	
	path is the path of the csv containing the data
	sensing data is a tuple in which the first value is the number of people who are sensing and the second value is the number of people who are intuitive in a set of hacker school students
	sensing_hypo is the initial guess representing the integer probability of a hacker school student being sensing
	sensing_ratio is the integer probability of any person being sensing

	Ohypotheses are mu, sigma pairs
	prior distribution is uniform
	liklihood is computed by evaluating the gaussian distribution of the hypo at the learning number

	'''

	studentdict = parsedata.ParseCsv(path)

	actref_data = [studentdict[student][1] for student in studentdict]
	senint_data = [studentdict[student][2] for student in studentdict]
	visver_data = [studentdict[student][3] for student in studentdict]
	seqglo_data = [studentdict[student][3] for student in studentdict]

	mus,sigmas = getHypos(actref_data)

	actref_style = learningstyle.Style(mus,sigmas)
	actref_style.UpdateSet(actref_data)
	#thinkplot.Pmf(actref_style)




if __name__ == "__main__":

	main('/home/gabrielle/wkspace/HackerSchool/pseudoscores.csv',100)
	#main(sys.argv[1],sys.argv[2])