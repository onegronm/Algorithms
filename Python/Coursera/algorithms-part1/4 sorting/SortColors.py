# https://leetcode.com/problems/sort-colors/ 
# difficulty: medium
# must sort in-place
# insertion sort (use for small or partially-sorted arrays)
# best n
# average n^2/4 compares
# worst n^2/2 compares

import unittest
from typing import List

class Solution:
	def sortColors(self, nums: List[int]) -> None:
		"""
		"""
		n = len(nums)

		for i in range(0, len(nums)):
			for j in range(i, 0, -1):
				if nums[j] < nums[j-1]:
					self.swap(nums, j, j-1)

	def swap(self, arr, a, b):
		temp = arr[a]
		arr[a] = arr[b]
		arr[b] = temp

class Test(unittest.TestCase):
	def test_case_1(self):
		s = Solution()
		arr = [2,0,2,1,1,0]
		s.sortColors(arr)
		self.assertTrue(arr == [0,0,1,1,2,2])

	def test_case_2(self):
		s = Solution()
		arr = [2,0,1]
		s.sortColors(arr)
		self.assertTrue(arr == [0,1,2])

	def test_case_3(self):
		s = Solution()
		arr = [0]
		s.sortColors(arr)
		self.assertTrue(arr == [0])

	def test_case_4(self):
		s = Solution()
		arr = [1]
		s.sortColors(arr)
		self.assertTrue(arr == [1])

unittest.main(verbosity=2)

