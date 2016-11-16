#!/usr/bin/env python
#KarolHorosin

import unittest
from Student import Student
import math

class test_Student(unittest.TestCase):
	def setUp(self):
		self.student = Student("Jan","Nowak")

	def test_init_raise_typeerror(self):
		self.assertRaises( TypeError, self.student.__init__, 21, 2)

	def test_add_grade_raise_typeerror(self):
		self.assertRaises( TypeError, self.student.add_grade, 2, 2)
		self.assertRaises( TypeError, self.student.add_grade, "sdas", "asd" )

	def test_get_total_average_return_correct_result(self):
		self.student.add_grade("Python",2)
		self.student.add_grade("Python",3)
		self.assertAlmostEqual(2.5, self.student.get_total_average(), places = 4)

	def test_get_class_average_resturn_correct_result(self):
		self.student.add_grade("Python",2)
		self.student.add_grade("Python",3)
		self.assertAlmostEqual(2.5, self.student.get_class_average("Python"), places = 4)

	def test_get_class_average_raises_typerror(self):
		self.student.add_grade("Python",2)
		self.assertRaises( TypeError, self.student.get_class_average, 2)




def main():
	unittest.main()
		
if __name__ == '__main__':
	main()
