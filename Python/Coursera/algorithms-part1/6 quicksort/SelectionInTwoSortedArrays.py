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
		r = s.findKthElement([2,3,6,7,9], [1,4,8,10], 5)
		self.assertEqual(r, 6)

	def test2(self):
		s = Selection()
		r = s.findKthElement([100,112,256,349,770], [72,86,113,119,265,445,892], 7)
		self.assertEqual(r, 256)

	def test3(self):
		s = Selection()
		r = s.findKthElement([100,112,256,349,770], [72,86,113,119,265,445,892], 2)
		self.assertEqual(r, 86)

	def test4(self):
		s = Selection()
		r = s.findKthElement([100,112,256,349,770], [72,86,113,119,265,445,892], 1)
		self.assertEqual(r, 72)

unittest.main(verbosity=2)