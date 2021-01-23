# Given two sorted arrays a[] and b[], of lengths n1 and n2 and an integer 0 <= k < n1 + n2,
# design an algorithm to find a key of rank k. The order of growth of the worst case running time of your algorithm 
# should be log n, where n = n1 + n2
# google (hard)
# https://stackoverflow.com/questions/4607945/how-to-find-the-kth-smallest-element-in-the-union-of-two-sorted-arrays

from typing import List
import unittest

class Selection:

	def findKthElement(self, arr1:List[int], arr2:List[int], k:int) -> int:

		# logarithmic solution

		if len(arr1) == 0 and len(arr2) == 0:
			return None

		# base case: if length of one of the arrays is 0, the answer is kth element of the second array.
		if len(arr1) == 0:
			return arr2[k]
		if len(arr2) == 0:
			return arr1[k]
		
		median1 = (len(arr1) // 2)
		median2 = (len(arr2) // 2)

		if median1 + median2 < k:
			# case not enough elements to cover k
			if arr1[median1] > arr2[median2]:
				# case k cannot be in arr2[:median2], so search in arr1 and arr2[median2+1:]
				return self.findKthElement(arr1, arr2[median2+1:], k - median2 - 1)
			else:
				# case k cannot be in arr1[:median1], so search in arr2 and arr1[median1+1:]
				return self.findKthElement(arr1[median1+1:], arr2, k - median1 - 1)
		else:
			# case there are enough elements to cover k element
			if arr1[median1] > arr2[median2]:
				# case k cannot be in arr1[median1:], so search in arr1[:median1] and arr2
				return self.findKthElement(arr1[:median1], arr2, k)
			else:
				# case k cannot be  in arr2[median2:], so search in arr2[:median1] and arr1
				return self.findKthElement(arr1, arr2[:median2], k)
		
		# quick sort solution below
		# merge both lists
		#arr = [0] * (len(a) + len(b))

		#for i in range(0,len(a)):
		#	arr[i] = a[i]

		#i = 0
		#for j in range(len(a),len(arr)):
		#	arr[j] = b[i]
		#	i += 1

		## join both lists and do quicksort
		#self.quicksort(arr, 0, len(arr)-1)

		#return arr[k-1]

		#logarithmic attempt below (works on some cases)
		#if k == 1 and not b: 
		#	return a[0]
		#elif k ==1 and not a:
		#	return b[0]
		#elif k == 1:
		#	return min(a[0],b[0])
		
		#n = len(a) + len(b)

		#if n == k:
		#	return max(a[len(a)-1],b[len(b)-1])
		#else:
		#	lenA = len(a)
		#	lenB = len(b)

		#	while lenA >= 1 and lenB >= 1:

		#		if lenA%2 == 0: # count elements from start up to median (inclusive) in a
		#			countA =  lenA//2
		#		else:
		#			countA = lenA//2 + 1

		#		if lenB%2 == 0: # count elements from start up to median (inclusive) in b
		#			countB = lenB//2
		#		else:
		#			countB = lenB//2 + 1

		#		if countA + countB == k:
		#			return max(a[countA - 1],b[countB - 1])
		#		elif countA + countB == k + 1:
		#			return min(a[countA - 1],b[countB - 1])
		#		else:
		#			lenA = countA
		#			lenB = countB

	def quicksort(self, arr, lo, hi):
		if hi <= lo: return

		j = self.partition(arr, lo, hi)
		self.quicksort(arr, lo, j-1)
		self.quicksort(arr, j+1, hi)


	def partition(self, a, lo, hi):
		i = lo + 1
		j = hi

		while True:
			while a[i] < a[lo]:
				if i == hi: break # find item on left to swap
				i += 1

			while a[j] > a[lo]:
				if j == lo: break # find item on right to swap
				j -= 1

			if i >= j: break # check if pointers cross
			a[i], a[j] = a[j], a[i] # swap

		a[lo], a[j] = a[j], a[lo] # swap with partitioning item
		return j # return index of item known to be in place

class Test(unittest.TestCase):
	def test0(self):
		s = Selection()
		r = s.findKthElement([2], [1], 2 - 1) # third argument is k - 1
		self.assertEqual(r, 2)

	def test1(self):
		s = Selection()
		r = s.findKthElement([2,3,6,7,9], [1,4,8,10], 5 - 1)
		self.assertEqual(r, 6)

	def test2(self):
		s = Selection()
		r = s.findKthElement([100,112,256,349,770], [72,86,113,119,265,445,892], 7 - 1)
		self.assertEqual(r, 256)

	def test3(self):
		s = Selection()
		r = s.findKthElement([100,112,256,349,770], [72,86,113,119,265,445,892], 2 - 1)
		self.assertEqual(r, 86)

	def test4(self):
		s = Selection()
		r = s.findKthElement([100,112,256,349,770], [72,86,113,119,265,445,892], 1 - 1)
		self.assertEqual(r, 72)

	def test5(self):
		s = Selection()
		r = s.findKthElement([1], [], 1 - 1)
		self.assertEqual(r, 1)

	def test6(self):
		s = Selection()
		r = s.findKthElement([],[], 1 - 1)
		self.assertEqual(r, None)

	def test7(self):
		s = Selection()
		r = s.findKthElement([1,2,3,4,5],[6,7,8,9,10], 5 - 1)
		self.assertEqual(r, 5)

unittest.main(verbosity=2)