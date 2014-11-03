import thinkbayes2
import thinkplot
import matplotlib
#%matplotlib inline

class Style(thinkbayes2.Suite, thinkbayes2.Joint):
	'''Each style is a joint distribution of mu and sigma values
	'''
	def __init__(self, mus, sigmas):
		thinkbayes2.Suite.__init__(self)
		pairs = [(mu,sigma) for mu in mus for sigma in sigmas]
		thinkbayes2.Suite.__init__(self,pairs)



	def Likelihood(self, data, hypo):
		'''Computes the likelihood of the data under the hypothesis

		data: tuple of (number of sensing, number of intuitive)
		hypo:  mu and sigma pair describing the distribution of learning styles'''

		mu, sigma = hypo
		x = data
		like = thinkbayes2.EvalNormalPdf(x,mu,sigma)
		return like

