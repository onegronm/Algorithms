# https://www.geeksforgeeks.org/check-if-two-arrays-are-permutations-of-each-other/
# Given two integer arrays of size nn, design a subquadratic algorithm to determine whether one is a permutation of the other. That is, do they contain exactly the same entries but, possibly, in a different order.

import unittest

# simple solution in O(nlogn)
class Permutations:
	"""
	"""
	
	def arePermutations(self, arr1, arr2):
		if len(arr1) != len(arr2):
			return False

		arr1.sort()
		arr2.sort()

		for i in range(0,len(arr1)):
			if arr1[i] != arr2[i]:
				return False

		return True

	# solution in O(n) time, O(n) space
	def arePermutations2(self, arr1, arr2):

		if len(arr1) != len(arr2):
			return False

		dict = {}

		for i in range(0, len(arr1)):
			x = arr1[i]
			if x not in dict.keys():
				dict[x] = 1
			else:
				dict[x] += 1

		for i in range(0, len(arr2)):
			x = arr2[i]
			if x not in dict.keys() or dict[x] == 0:
				return False
			dict[x] -= 1

		return True

class Test(unittest.TestCase):
	def test_case_1(self):
		p = Permutations()
		self.assertTrue(p.arePermutations2([2, 1, 3, 5, 4, 3, 2],[3, 2, 2, 4, 5, 3, 1]))

	def test_case_2(self):
		p = Permutations()
		self.assertFalse(p.arePermutations2([2, 1, 3, 5],[3, 2, 2, 4]))

unittest.main(verbosity=2)