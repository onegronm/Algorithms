from typing import List
import unittest

class Solution:

	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		"""
		"""

class Test(unittest.TestCase):
	"""
	"""
	
	def test_0(self):
		s = Solution()
		self.assertTrue(s.findMedianSortedArrays([1,3],[2]), 2)

	def test_1(self):
		s = Solution()
		self.assertTrue(s.findMedianSortedArrays([1,2],[3,4]), 2.5)

	def test_2(self):
		s = Solution()
		self.assertTrue(s.findMedianSortedArrays([0,0],[0,0]), 0)

	def test_3(self):
		s = Solution()
		self.assertTrue(s.findMedianSortedArrays([],[1]), 1)

	def test_4(self):
		s = Solution()
		self.assertTrue(s.findMedianSortedArrays([2],[]), 2)

unittest.main(verbosity==2)
