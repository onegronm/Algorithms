import unittest
from typing import List

class ReverseStack:
	"""
	"""

	def reverse(self, arr, lo: int, hi: int) -> List[int]:

		if lo >= hi or not arr:
			return

		arr[lo], arr[hi] = arr[hi], arr[lo] # swap

		lo += 1
		hi -= 1

		self.reverse(arr, lo, hi)


class Test(unittest.TestCase):
	"""
	-1,-1,10,5,0,7
	7	-1 10 5 0	-1
	7 0		10 5	-1-1
	7 0 5			10 -1 -1
	7 0 5 10 -1 -1
	"""

	def test_1(self):
		s = [1,2,3,4,5]
		r = ReverseStack()
		r.reverse(s, 0, len(s)-1)
		self.assertListEqual(s,[5,4,3,2,1])

	def test_2(self):
		s = []
		r = ReverseStack()
		r.reverse(s, 0, len(s)-1)
		self.assertListEqual(s,[])

	def test_3(self):
		s = [1]
		r = ReverseStack()
		r.reverse(s, 0, len(s)-1)
		self.assertListEqual(s,[1])

	def test_4(self):
		s = [-1,-1,10,5,0,7]
		r = ReverseStack()
		r.reverse(s, 0, len(s)-1)
		self.assertListEqual(s,[7,0,5,10,-1,-1])

unittest.main(verbosity=2)

