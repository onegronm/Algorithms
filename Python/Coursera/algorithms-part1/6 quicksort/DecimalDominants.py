# Decimal dominants. Given an array with n keys, design an algorithm to find all values 
# that occur more than n/10 times. The expected running time of your algorithm should be linear.
# Hint: determine the (n/10)th largest key using quickselect and check if it occurs more than n/10 times.
# https://massivealgorithms.blogspot.com/2019/03/decimal-dominants.html

# [20,19,18,17,16,15,14,14,14,11,10,9,8,7,6,5,4,3,2,1]
# 20/10 = 2 find elements that occur more than twice
# we can narrow our candidates to 9 elements, namely (n/10)-th, (2n/10)-th, … (9n/10)-th elements
# any elements left to (n/10)-th array cannot occur more than n/10 times because there won’t be enough room
# any elements left to (2n/10)-th array cannot occur more than 2n/10 times because there won’t be enough room ...
# repeat for sub array including and to the right side of (n/10)-th largest element
# if the n/10 th element is repeated in any sub array, update a counter
# reset counter if item doesn't repeat?

import unittest

class DecimalDominant:

	def __init__(self):
		"""
		"""

	def partition(self, arr, lo, hi):
		i = lo + 1
		j = hi

		while True:
			
			while arr[i] < arr[lo]:
				i += 1
				if i == hi: break

			while arr[lo] < arr[j]:
				if j == lo: break				
				j -= 1

			if i >= j: break # check if pointers cross
			arr[i], arr[j] = arr[j], arr[i] # swap

		arr[lo], arr[j] = arr[j], arr[lo] # swap with partitioning item
		return j # return index of item known to be in place

	def select(self, arr, k):
		lo = 0
		hi = len(arr) - 1

		while hi > lo:
			j = self.partition(arr, lo, hi)
			if j < k: lo = j + 1
			elif j > k: hi = j - 1
			else: return arr[k]

		return arr[k]


class Test(unittest.TestCase):

	def test1(self):
		"""
		"""
		d = DecimalDominant()
		i = d.select([20,19,18,17,16,15,14,14,14,11,10,9,8,7,6,5,4,3,2,1], 19 - 1)
		self.assertTrue(i == 19)



unittest.main(verbosity = 2)