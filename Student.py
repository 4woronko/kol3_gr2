#!/usr/bin/env python
#KarolHorosin

import re

class Student(object):

	def __init__(self, name, surname):
		
		if isinstance(name, str) :
			self.name = name
		else:
			raise TypeError("Wrong student's name")

		if isinstance(surname, str) :
			self.surname = surname
		else:
			raise TypeError("Wrong student's surname")			
		
		self.scores = {}


	def get_total_average(self):
		suma = 0
		no = 0
		for i in self.scores.values():
			suma = suma + sum(i)
			no = no + len(i)
		return float(suma)/float(no)

	def get_class_average(self, class_name):
		no = float (len(self.scores[class_name]))
		suma = float( sum(self.scores[class_name]))
		return suma/no

	def add_grade(self, class_name, score):
		p = re.compile('\d+(\.\d+)?')
		if not isinstance( class_name, str ) :
			raise TypeError( "Wrong class name type" )
		else:
			if not (class_name in self.scores.keys()) :
				self.scores[ class_name ] = []
			self.scores[ class_name ].append(score)	


