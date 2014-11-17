#!/usr/bin/env python

'''parse data from csv into people class'''
import numpy as np
import re

def ParseCsv(path):
	'''parses data from csv genrated by learning styles survey into student objects with learning style info
	
	Each row is a person, column 1 contains names
	the other columns correspond to learning style categories and contain scores

	- means the person has the first learning style in the catgory(eg if the column is active v. reflective, a -1 means the person is active)
	+ means the person has the second learning style in the category
	0 means they are smack dab in the middle!

	student_dict is a dictionary with student names mapped to a list containing the student's learning style information
	element 1 of the list contains whether the student is active or reflective
	2 contains the student's sensing-intuitive number
	3 contains the student's visual-verbal number
	4 contains sequential or global

	'''
	#specify file path here
	#path = '/home/gabrielle/wkspace/HackerSchool/pseudodata.csv'
	n_cols = 5
	n_skip_rows = 1
	n_name_col = 1

	data = np.genfromtxt(path, skip_header = n_skip_rows, delimiter = ",", dtype = None)

	student_dict = {}
	student_dict = [student[3]*-1 if student[2]=='active' else student[3] for student in data]
	student_dict = [student[5]*-1 if student[4]=='sensing' else student[5] for student in data]
	student_dict = [student[7]*-1 if student[6]=='visual' else student[7] for student in data]
	student_dict = [student[9]*-1 if student[8]=='global' else student[9] for student in data]

	return student_dict



