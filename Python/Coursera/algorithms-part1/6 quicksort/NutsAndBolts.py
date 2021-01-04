# A disorganized carpenter has a mixed pile of n nuts and n bolts. The goal is to find the corresponding pairs of nuts and bolts. Each nut fits exactly one bolt and each bolt fits exactly one nut. By fitting a nut and a bolt together, the carpenter can see which one is bigger (but the carpenter cannot compare two nuts or two bolts directly). Design an algorithm for the problem that uses at most proportional to n \log nnlogn compares (probabilistically).
# Input:
# The lists of locks and keys.
# nuts = { ),@,*,^,(,%, !,$,&,# }
# bolts = { !, (, #, %, ), ^, &, *, $, @ }
# Output:
# After matching nuts and bolts:
# Nuts:  ! # $ % & ( ) * @ ^
# Bolts: ! # $ % & ( ) * @ ^
# Hint: modify the quicksort partitioning part of quicksort.
# https://github.com/nataliekung/leetcode/blob/master/qiang-hua-4-shuang-zhi-zhen-ff09/nuts-and-bolts-problem.md
import unittest
from typing import List, Tuple

class NutsAndBolts:
	
	# 1. shuffle nuts and bolts for performance guarantee
	# 2. partition the nuts returning the index of item in place.
	# 3. partition the bolts using the index from step 1 as the pivot
	# 4. repeat quick sort for lo to index
	# 5. repeat quick sort for index + 1 to hi

	def sortNutsAndBolts(self, nuts: List[str], bolts: List[str]) -> Tuple[List[str], List[str]]:
		"""
		"""
		if not nuts or not bolts:
			return

		if len(nuts) != len(bolts):
			return

		# shuffle nuts
		# shuffle bolts

		return self.quickSort(nuts, bolts, 0, len(nuts)-1)

	def quickSort(self, nuts:List[str], bolts:List[str], lo, hi) -> Tuple[List[str], List[str]]:
		if hi <= lo: return
		j = self.partition(nuts, bolts[lo], lo, hi)
		self.partition(bolts, nuts[j], lo, hi) # use the index of the in-place element in nuts as pivot for partitioning bolts
		self.quickSort(nuts, bolts, lo, j-1) # repeat for left side of pivot
		self.quickSort(nuts, bolts, j, hi) # repeat for right side of pivot


class Test(unittest.TestCase):
	def test_1(self):
		n = NutsAndBolts()
		solution = n.sortNutsAndBolts([')','@','*','^','(','%',' !','$','&','#'], ['!','(','#','%',')','^','&','*','$','@'])
		self.assertTrue(solution, [['!','#','$','%','&','(',')','*','@','^'], ['!','#','$','%','&','(',')','*','@','^']])

unittest.main(verbosity=2)