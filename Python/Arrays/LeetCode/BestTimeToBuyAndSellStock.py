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

		lo = arr[0]
		hi = arr[0]
		maxProfit = 0

		for i in range(1, len(arr)):
			if arr[i] < lo:
				lo = hi = arr[i]
			elif arr[i] > hi:
				hi = arr[i]

		maxProfit = hi - lo

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

unittest.main(verbosity=2)