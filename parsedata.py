#!/usr/bin/env python

'''parse data from csv into people class'''
import numpy as np
import re

def ParseCsv(path):
	'''parses data from csv genrated by learning styles survey into student objects with learning style info
	
	Each row is a person, column 1 contains names
	the other columns correspond to learning style categories and contain -1, 0, or 1

	- means the person has the first learning style in the catgory(eg if the column is active v. reflective, a -1 means the person is active)
	+ means the person has the second learning style in the category
	0 means they are smack dab in the middle!

	student_dict is a dictionary with student names mapped to a list containing the student's learning style information
	element 1 the student's is active-reflective number
	2 contains the student's sensing-intuitive number
	3 contains the student's visual-verbal number
	4 contains sequential-global

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


