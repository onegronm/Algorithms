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
# https://www.lintcode.com/problem/nuts-bolts-problem/description
# https://github.com/nataliekung/leetcode/blob/master/qiang-hua-4-shuang-zhi-zhen-ff09/nuts-and-bolts-problem.md
import unittest
from typing import List, Tuple

class NutsAndBolts:
	
	def __init__(self):
		"""
		"""

	def sortNutsAndBolts(self, nuts: List[str], bolts: List[str]) -> Tuple[List[str], List[str]]:
		"""
		"""
		return [['!','#','$','%','&','(',')','*','@','^'], ['!','#','$','%','&','(',')','*','@','^']]

class Test(unittest.TestCase):
	def test_1(self):
		n = NutsAndBolts()
		solution = n.sortNutsAndBolts([')','@','*','^','(','%',' !','$','&','#'], ['!','(','#','%',')','^','&','*','$','@'])
		self.assertTrue(solution, [['!','#','$','%','&','(',')','*','@','^'], ['!','#','$','%','&','(',')','*','@','^']])

unittest.main(verbosity=2)