# Given two sorted arrays a[] and b[], of lengths n1 and n2 and an integer 0 <= k < n1 + n2,
# design an algorithm to find a key of rank k. The order of growth of the worst case running time of your algorithm 
# should be log n, where n = n1 + n2
# google (hard)
from typing import List
import unittest

class Selection:

	def findKthElement(self, a:List[int], b:List[int], k:int) -> int:
		if not a and not b: 
			return

		if k == 1 and not b: 
			return a[0]
		elif k ==1 and not a:
			return b[0]
		elif k == 1:
			return min(a[0],b[0])
		
		n = len(a) + len(b)

		if n == k:
			return max(a[len(a)-1],b[len(b)-1])
		else:
			lenA = len(a)
			lenB = len(b)

			while lenA >= 1 and lenB >= 1:
				if lenA%2 == 0: # count elements from start up to median (inclusive) in a
					countA =  lenA//2
				else:
					countA = lenA//2 + 1

				if lenB%2 == 0: # count elements from start up to median (inclusive) in b
					countB = lenB//2
				else:
					countB = lenB//2 + 1

				if countA + countB == k:
					return max(a[countA - 1],b[countB - 1])
				elif countA + countB == k + 1:
					return min(a[countA - 1],b[countB - 1])
				else:
					lenA = countA
					lenB = countB

		return 0

class Test(unittest.TestCase):
	def test1(self):
		s = Selection()
		r = s.findKthElement([2,3,6,7,9], [1,4,8,10], 5)
		self.assertEqual(r, 6)

	def test2(self):
		s = Selection()
		r = s.findKthElement([100,112,256,349,770], [72,86,113,119,265,445,892], 7)
		self.assertEqual(r, 256)

	def test3(self):
		s = Selection()
		r = s.findKthElement([100,112,256,349,770], [72,86,113,119,265,445,892], 2)
		self.assertEqual(r, 86)

	def test4(self):
		s = Selection()
		r = s.findKthElement([100,112,256,349,770], [72,86,113,119,265,445,892], 1)
		self.assertEqual(r, 72)

	def test5(self):
		s = Selection()
		r = s.findKthElement([1], [], 1)
		self.assertEqual(r, 1)

	def test6(self):
		s = Selection()
		r = s.findKthElement([],[], 1)
		self.assertEqual(r, None)

	def test7(self):
		s = Selection()
		r = s.findKthElement([1,2,3,4,5],[6,7,8,9,10], 5)
		self.assertEqual(r, 5)

unittest.main(verbosity=2)