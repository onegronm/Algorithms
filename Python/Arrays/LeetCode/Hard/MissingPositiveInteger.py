# stripe question
# https://leetcode.com/problems/first-missing-positive/
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# difficulty: hard

from typing import List
import unittest

class Solution:

	# first attempt
	# intuition: by popping existing pos integers and negatives, reduce the number of items to compare (still quadratic)
	#def firstMissingPositive(self, arr:List[int]) -> int:
	#	"""
	#	"""
	#	loPosInt = 1

	#	i = 0
	#	while arr and i < len(arr):
	#		if arr[i] == loPosInt:
	#			self.swap(arr, i, len(arr)-1)
	#			arr.pop()
	#			i = 0
	#			loPosInt += 1
	#			continue
	#		elif arr[i] <= 0:
	#			self.swap(arr, i, len(arr)-1)
	#			arr.pop()
	#		else:
	#			i += 1

	#	return loPosInt

	#def swap(self, arr, a, b):
	#	temp = arr[a]
	#	arr[a] = arr[b]
	#	arr[b] = temp

	# second attempt
	# Hint: think about how you would solve the problem in non-constant space. Can you apply that logic to the existing space?
	def firstMissingPositive(self, arr:List[int]) -> int:
		"""
		"""
		dict = {}

		for i in range(0,len(arr)):
			val = arr[i]
			if val not in dict.keys():
				dict[val] = 1

		loPosInt = 1

		for i in range(0,len(arr)):
			if loPosInt in dict.keys():
				loPosInt += 1
			else:
				return loPosInt

		return loPosInt

class Test(unittest.TestCase):

	def test_case_1(self):
		s = Solution()
		arr = [3, 4, -1, 1]
		self.assertTrue(s.firstMissingPositive(arr) == 2)

	def test_case_2(self):
		s = Solution()
		arr = [1, 2, 0]
		self.assertTrue(s.firstMissingPositive(arr) == 3)

	def test_case_3(self):
		s = Solution()
		arr = [0]
		self.assertTrue(s.firstMissingPositive(arr) == 1)

	def test_case_4(self):
		s = Solution()
		arr = [0,1,2,3,4,5,6,7,8,9,10]
		self.assertTrue(s.firstMissingPositive(arr) == 11)

	def test_case_5(self):
		s = Solution()
		arr = [7,8,9,11,12]
		self.assertTrue(s.firstMissingPositive(arr) == 1)

	def test_case_6(self):
		s = Solution()
		arr = [-7,-8,-9,-11,-12]
		self.assertTrue(s.firstMissingPositive(arr) == 1)

	def test_case_7(self):
		s = Solution()
		arr = [-7,-8,0,1,3]
		self.assertTrue(s.firstMissingPositive(arr) == 2)

unittest.main(verbosity=2)