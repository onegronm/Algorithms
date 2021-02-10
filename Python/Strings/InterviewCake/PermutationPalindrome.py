import unittest

class Solution():
	"""
	"""
	def isPalindrome(self, input) -> bool:
		"""
		"""
		isPalindrome = True

		if not input:
			return False

		if len(input) < 2:
			return True

		# supposition: if the number of characters is even, then each character must exist in equal amount
		# if the number of characters is uneven, each character must exist in equal amount, except maybe one
		# we only need to know if a character appears an even or odd number of times
		# if odd, no more than one of the caracters appears an odd number of times
		characterCount = {}

		for i in range(0, len(input)):
			key = input[i]
			if key in characterCount:
				characterCount[key] += 1
			else:
				characterCount[key] = 1

		oddCounts = 0
		for k in characterCount.keys():
			if characterCount[k] % 2 != 0:
				oddCounts += 1
		
		if len(input) % 2 == 0 and oddCounts > 0:
			isPalindrome = False

		if len(input) % 2 != 0 and oddCounts > 1:
			isPalindrome = False

		return isPalindrome

class Test(unittest.TestCase):
	def test1(self):
		s = Solution()
		self.assertTrue(s.isPalindrome("civic"))

	def test2(self):
		s = Solution()
		self.assertTrue(s.isPalindrome("ivicc"))

	def test3(self):
		s = Solution()
		self.assertFalse(s.isPalindrome("civil"))

	def test4(self):
		s = Solution()
		self.assertFalse(s.isPalindrome("livci"))

	def test5(self):
		s = Solution()
		self.assertTrue(s.isPalindrome("aaaaa"))

	def test6(self):
		s = Solution()
		self.assertTrue(s.isPalindrome("otto"))

	def test7(self):
		s = Solution()
		self.assertTrue(s.isPalindrome("eve"))

	def test8(self):
		s = Solution()
		self.assertTrue(s.isPalindrome("radar"))

	def test9(self):
		s = Solution()
		self.assertTrue(s.isPalindrome("rotator"))

unittest.main(verbosity=2)