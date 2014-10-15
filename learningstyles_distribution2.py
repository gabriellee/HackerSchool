#!/usr/bin/env python

import thinkbayes2
import thinkplot
import matplotlib
#%matplotlib inline

class StyleDist(thinkbayes2.Suite):
	'''maps from the distribution of learning styles within Hacker School to its expected probability'''
	#hypo is the probability of sensing v intuitive, 
	#data is a string, either 'sensing' or 'intuitive'

	def Likelihood(self, data, hypo):
		'''Computes the likliehood of the data under the hypothesis

		data: tuple of (number of sensing, number of intuitive)
		hypo:  integer value of the probability of sensing (0-100)'''

		sensing, intuitive = data
		like = (hypo/100.0)**sensing * (1 - hypo/100.0)**intuitive
		return like


	def SuiteLikelihood(suite, data):
	    """Computes the weighted average of likelihoods for sub-hypotheses.

	    suite: Suite that maps sub-hypotheses to probability
	    data: some representation of the data
	   
	    returns: float likelihood
	    """
	    total = 0
	    for hypo, prob in suite.Items():
	        like = suite.Likelihood(data, hypo)
	        total += prob * like
	    return total