from typing import List
import unittest

class Solution:

	# follow-up: The overall run time complexity should be O(log (m+n)).
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		"""
		"""

		i = 0
		j = 0
		k = 0
		temp = []
		left = 0
		right = 0

		while (i < len(nums1) or j < len(nums2)) and k < len(nums1) + len(nums2):
			if nums1 and i < len(nums1):
				left = nums1[i]
			if nums2 and j < len(nums2):
				right = nums2[j]

			# j >- len(nums2) -> nums2 is exhausted
			if nums1 and (i < len(nums1) and left <= right) or j >= len(nums2):
				temp.append(left)
				i += 1
			# i >= len(nums1) -> nums1 is exhausted
			elif nums2 and (j < len(nums2) and right < left) or i >= len(nums1):
				temp.append(right)
				j += 1

			k += 1

		median = 0
		if (len(nums1) + len(nums2)) % 2 == 0:
			median = (temp[((len(nums1) + len(nums2))//2)-1] + temp[((len(nums1) + len(nums2))//2)]) / 2
		else:
			median = temp[(len(nums1) + len(nums2))//2]

		return median
				

class Test(unittest.TestCase):
	"""
	"""
	
	def test_0(self):
		s = Solution()
		self.assertTrue(s.findMedianSortedArrays([1,3],[2]) == 2)

	def test_1(self):
		s = Solution()
		self.assertTrue(s.findMedianSortedArrays([1,2],[3,4]) == 2.5)

	def test_2(self):
		s = Solution()
		self.assertTrue(s.findMedianSortedArrays([0,0],[0,0]) == 0.0)

	def test_3(self):
		s = Solution()
		self.assertTrue(s.findMedianSortedArrays([],[1]) == 1)

	def test_4(self):
		s = Solution()
		self.assertTrue(s.findMedianSortedArrays([2],[]) == 2)

	def test_5(self):
		s = Solution()
		self.assertTrue(s.findMedianSortedArrays([1,3,5,7,9],[2,4,6,8,10]) == 5.5)		


unittest.main(verbosity=2)
