import thinkbayes2
import thinkplot
import matplotlib
#%matplotlib inline

class StyleDist(thinkbayes2.Suite):
	'''maps from the distribution of learning styles within Hacker School to its expected probability'''
	#hypo is the probability of type1 v type2, 
	#data is a string, either 'type1' or 'type2'

	def Likelihood(self, data, hypo):
		'''Computes the likliehood of the data under the hypothesis

		data: tuple of (number of type1, number of type2)
		hypo:  integer value of the probability of type1 (0-100)'''

		type1, type2 = data
		like = (hypo/100.0)**type1 * (1 - hypo/100.0)**type2
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