# Counting inversions. An inversion in an array a[] is a pair of entries a[i] and a[j] such that i < j but a[i] > a[j]. Given an array, design a linearithmic algorithm to count the number of inversions.
# hard
# hint: count while mergesorting
from typing import List
import unittest

class Solution:

	def mergeSortInversions(self, arr:List[int]):
		"""
		"""

		# could not figure out intuition for linearithmic algorithm
		# brute force method involves comparing each number against all that are ahead of it
		# if it's less than current number, add 1 to inversion count

		# solution: a linearithmic algorithm exists for inversion count by divide and conquer
		# see UC Davis lecture: https://www.youtube.com/watch?v=Vj5IOD7A6f8&ab_channel=UCDavis
		# https://medium.com/@ssbothwell/counting-inversions-with-merge-sort-4d9910dc95f0

		# applications:
		# ranking songs
		# music site consults database to find people with similar tastes. Person with least inversions has most similar taste
		# voting theory
		# sensitivity analysis of google's ranking function
		# rank aggregation for meta-searching on the web
		# measuring the "sortedness" of an array

		if len(arr) == 1:
			return arr, 0
		else:
			a = arr[:len(arr)//2]
			b = arr[len(arr)//2:]

			a, ai = self.mergeSortInversions(a)
			b, bi = self.mergeSortInversions(b)
			c = []

			i = 0
			j = 0
			inversions = 0 + ai + bi


		while i < len(a) and j < len(b): # if any of the lists is exhausted, exit the loop

			if a[i] <= b[j]:
				c.append(a[i])
				i+=1
			else:
				c.append(b[j])
				j+=1
				inversions += (len(a) - i)

		# append to c what remains of both lists
		c += a[i:]
		c += b[j:]

		return c, inversions

class Test(unittest.TestCase):
	def test_1(self):
		"""
		"""
		s = Solution()
		print(s.mergeSortInversions([8,2,6,4,1,3,7,5,9]))

	def test_2(self):
		s = Solution()
		self.assertTrue(s.mergeSortInversions([3,2,1]) == ([1,2,3], 3))

unittest.main(verbosity=2)