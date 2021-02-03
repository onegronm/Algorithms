# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# easy
import unittest

class Solution:
	"""
	"""

	def maxProfit(self, arr) -> int:
		"""
		"""
		if len(arr) == 1 or not arr:
			return 0

		lo = 0
		hi = 0
		maxProfit = 0

		for i in range(1, len(arr)):
			if arr[i] < arr[lo]:
				lo = hi = i
			elif arr[i] > arr[hi]:
				hi = i
				profit = arr[hi] - arr[lo]
				if profit > maxProfit: maxProfit = profit

		if maxProfit < 0 : maxProfit = 0

		return maxProfit

class Test(unittest.TestCase):

	def test_1(self):
		s = Solution()
		arr = [1,2,3,4,5,100]		
		self.assertTrue(s.maxProfit(arr) == 99)

	def test_2(self):
		s = Solution()
		arr = [1,2,100,3,4]
		self.assertTrue(s.maxProfit(arr) == 99)

	def test_3(self):
		s = Solution()
		arr = [3,4,1,2,100]
		self.assertTrue(s.maxProfit(arr) == 99)

	def test_4(self):
		s = Solution()
		arr = [7,1,5,3,6,4]
		self.assertTrue(s.maxProfit(arr) == 5)

	def test_5(self):
		s = Solution()
		arr = [7,6,4,3,1]
		self.assertTrue(s.maxProfit(arr) == 0)

	def test_6(self):
		s = Solution()
		arr = [1]
		self.assertTrue(s.maxProfit(arr) == 0)

	def test_7(self):
		s = Solution()
		arr = []
		self.assertTrue(s.maxProfit(arr) == 0)

	def test_8(self):
		s = Solution()
		arr = [2,4,1]
		self.assertTrue(s.maxProfit(arr) == 2)

	def test_9(self):
		s = Solution()
		arr = [3,2,6,5,0,3]
		self.assertTrue(s.maxProfit(arr) == 4)
		
unittest.main(verbosity=2)