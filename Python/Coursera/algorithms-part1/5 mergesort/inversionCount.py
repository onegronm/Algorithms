# Counting inversions. An inversion in an array a[] is a pair of entries a[i] and a[j] such that i < j but a[i] > a[j]. Given an array, design a linearithmic algorithm to count the number of inversions.
# hard
from typing import List
import unittest

class Solution:

	def inversionCount(self, arr:List[int]) -> int:
		"""
		"""

		# could not figure out intuition for linearithmic algorithm
		# brute force method involves comparing each number against all that are ahead of it
		# if it's less than current number, add 1 to inversion count

class Test(unittest.TestCase):
	def test_1(self):
		"""
		"""
		s = Solution()
		s.inversionCount([8,2,6,4,1,3,7,5,9])

		# 1,2,3,4,5,6,7,8,9
		# 


unittest.main(verbosity=2)