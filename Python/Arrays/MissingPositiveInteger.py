# stripe question
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

from typing import List
import unittest

class Solution:

	# my attempt
	# intuition: by popping existing pos integers and negatives, reduce the number of items to compare
	# (still quadratic)
	def findMissingInteger(self, arr:List[int]) -> int:
		"""
		"""
		loPosInt = 1

		i = 0
		while arr and i < len(arr):
			if arr[i] == loPosInt:
				self.swap(arr, i, len(arr)-1)
				arr.pop()
				i = 0
				loPosInt += 1
				continue
			elif arr[i] <= 0:
				self.swap(arr, i, len(arr)-1)
				arr.pop()
			else:
				i += 1

		return loPosInt

	def swap(self, arr, a, b):
		temp = arr[a]
		arr[a] = arr[b]
		arr[b] = temp


class Test(unittest.TestCase):

	def test_case_1(self):
		s = Solution()
		arr = [3, 4, -1, 1]
		self.assertTrue(s.findMissingInteger(arr) == 2)

	def test_case_2(self):
		s = Solution()
		arr = [1, 2, 0]
		self.assertTrue(s.findMissingInteger(arr) == 3)

	def test_case_3(self):
		s = Solution()
		arr = [0]
		self.assertTrue(s.findMissingInteger(arr) == 1)

	def test_case_4(self):
		s = Solution()
		arr = [0,1,2,3,4,5,6,7,8,9,10]
		self.assertTrue(s.findMissingInteger(arr) == 11)

unittest.main(verbosity=2)