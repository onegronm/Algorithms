# Given two sorted arrays a[] and b[], of lengths n1 and n2 and an integer 0 <= k < n1 + n2,
# design an algorithm to find a key of rank k. The order of growth of the worst case running time of your algorithm 
# should be log n, where n = n1 + n2

from typing import List
import unittest

class Selection:

	def findKthElement(self, a:List[int], b:List[int], k:int) -> int:
		"""
		"""
		return 0

class Test(unittest.TestCase):
	def test1(self):
		s = Selection()
		k = 5
		r = s.findKthElement([],[],k)
		self.assertEqual(r, 0)

unittest.main(verbosity=2)