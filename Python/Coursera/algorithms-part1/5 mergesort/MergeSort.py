from typing import List
import unittest

class Mergesort:
	def merge(self,arr: List[str], aux: List[str], lo: int, mid: int, hi: int) -> None:
		"""
		"""
		for i in range(lo, hi+1):
			aux[i] = arr[i]

		i = lo
		j = mid+1

		for k in range(lo, hi+1):
			if i > mid:
				arr[k] = aux[j] # exhausted first half
				j+=1
			elif j > hi:
				arr[k] = aux[i] # exhausted second half
				i+=1
			elif aux[j] < aux[i]:
				arr[k] = aux[j]
				j+=1
			else:
				arr[k] = aux[i]
				i+=1
	
	def sortaux(self,arr: List[str], aux: List[str], lo: int, hi: int) -> None:
		"""
		"""
		if hi <= lo: return
		mid = lo + (hi - lo) // 2
		self.sortaux(arr, aux, lo, mid)
		self.sortaux(arr, aux, mid+1, hi)
		self.merge(arr, aux, lo, mid, hi)

	def sort(self, arr: List[str]) -> None:
		"""
		"""
		aux = list(arr)
		self.sortaux(arr, aux, 0, len(arr)-1)
		
class Test(unittest.TestCase):

	def test_case_1(self):
		s = Mergesort()
		arr = ["m","e","r","g","e","s","o","r","t","e","x","a","m","p","l","e"]
		s.sort(arr)
		print(arr)
		self.assertTrue(arr[0] == "a")

unittest.main(verbosity=2)

