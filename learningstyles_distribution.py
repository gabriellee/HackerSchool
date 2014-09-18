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


def main():
	'''initializes an instance of a learning styles probability distribution
	updates the probability distribution based on data
	checks the strength of the evidence that the distribution in hacker school is substantiallly different'''

	sensing_data = (2, 0)
	sensing_hypo = 50
	sensing_ratio = 65


	sensing_dist = StyleDist(range(0,101))
	sensing_likelihood = sensing_dist.Likelihood(sensing_data, sensing_hypo)
	print('p(D|50%)', sensing_likelihood)
	thinkplot.Hist(sensing_dist)

	#set p(D|~H)
	b_uniform = StyleDist(range(0,101))
	b_uniform.Remove(sensing_ratio)
	b_uniform.Normalize()

	# %matplotlib inline
	thinkplot.Pmf(sensing_dist)
	return sensing_dist


# def TestEvidence(, data):
# 	'''tests the strength of the evidence
# 	calculates p(D|H) / p(D|~H)

# 	pop_num: the number of people with the first learning style in data in a group of 100 non hacker schoolers  (ie sensing, active, visual, sequential)
# 	H: hypothesis that hypo/100 (ratio among hacker schoolers) = ratio among non hacker schoolers
# 	~H: hypothesis that hypo/100 is not the ratio among non-hacker schoolers, but might be any other value with equal probability'''
	
# 	same = StyleDist()
# 	same.Set(pop_num, 1)

# 	diff = StyleDist()
# 	for x in range(0,101):
# 		if x != popratio:
# 			diff.Set(x, 1)

# 	diff.Normalize()

# 	like_same = thinkbayes2.AverageLikelihood(like_same, data)
# 	like_diff = thinkbayes2.AverageLikelihood(like_diff, data)
# 	like_ratio = like_diff/like_same
# 	return like_ratio



print main()