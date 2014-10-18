#!/usr/bin/env python

'''parse data from csv into people class'''
import numpy as np
import re

class Student():
	def __init__(self,act_ref,sen_int,vis_ver,seq_glo):
		self.act_ref = act_ref
		self.sen_int = sen_int
		self.vis_ver = vis_ver
		self.seq_glo = seq_glo

def ParseCsv(path):
	'''parses data from csv genrated by learning styles survey into student objects with learning style info
	
	Each row is a person, column 1 contains names
	the other columns correspond to learning style categories and contain -1, 0, or 1

	-1 means that the person has the first learning style in the catgory(eg if the column is active v. reflective, a -1 means the person is active)
	1 means the person has the second learning style in the category
	0 means they are smack dab in the middle!

	student_dict is a dictionary with student names mapped to a list containing the student's learning style information
	element 1 of the list contains whether the student is active or reflective
	2 contains whether the student is sensing versus intuitive
	3 contains whether the student is visual or verbal
	4 contains sequential or global

	'''
	#specify file path here
	#path = '/home/gabrielle/wkspace/HackerSchool/pseudodata.csv'
	n_cols = 5
	n_skip_rows = 0
	n_name_col = 0

	data = np.genfromtxt(path, skip_header = n_skip_rows, delimiter = ",", dtype = None)

	# Temporary storage - Gabrielle, pls rename/cleanup
	student_dict = {}
	for student in data:
		student_dict[student[0]] = (student[1], student[2], student[3], student[4])
		print(student_dict)
	return student_dict


