# https://afteracademy.com/blog/find-an-element-in-a-bitonic-array
# Find an element in a bitonic array
# Must be O(~3 log n) in the worst case

# An array is bitonic if it is comprised of an increasing sequence of integers followed immediately by a decreasing sequence of integers. 
# Write a program that, given a bitonic array of n distinct integer values, determines whether a given integer is in the array.

# use binary search (log n)
# first find the maximum
# then binary search increasing sequence
# then binary search decreasing sequence

from typing import List

class Solution:

	def __init__(self):
		self.peak = 0

	def findPeak(self, nums, start, end):			
		mid = start + ((end - start) // 2)

		# CASE if mid is greater than left and right, then we found the peak					
		if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
			self.peak = mid
		# CASE mid is greater than peak, search right
		elif nums[mid] > self.peak:
			self.peak = mid
			self.findPeak(nums, mid, len(nums) - 1)
		# CASE value is less than peak, search left
		else:
			self.findPeak(nums, start, mid)

	def leftBinarySearch(self, nums, start, end, key):

		while start <= end:

			mid = start +(end - start) // 2

			if nums[mid] == key:
				return mid

			if key < nums[mid]:
				end = mid - 1
			else:
				start = mid + 1

		return -1

	def rightBinarySearch(self, nums, start, end, key):

		while start <= end:

			mid = start +(end - start) // 2

			if nums[mid] == key:
				return mid

			if key < nums[mid]:
				start = mid + 1
			else:				
				end = mid - 1

		return -1

	# [-3,-2,-1,100,90, 60, 20]
	# [-1,0,-2]
	# [-4,-3,-1,0,-2]
	def bitonicArray(self, arr:List[int], key: int) -> int:

		self.peak = 0 # assume left-most number is the smallest
		
		start = 0
		end = len(arr) - 1

		# Find the peak point of the bitonic array
		self.findPeak(arr, start, end)

		# If the element to be searched is equal to the peak element then return its index.
		if arr[self.peak] == key:
			return self.peak

		# If the element to be searched is greater than the element at peak point then the element does not exist in the array.
		if key > arr[self.peak]:
			return -1
		else:
			# do binary search on both halves
			result = self.leftBinarySearch(arr, 0, self.peak - 1, key)

			if result != -1:
				return result
			
			return self.rightBinarySearch(arr, self.peak, len(arr)-1, key)
			
		return -1

sol = Solution()
print(sol.bitonicArray([-3,-2,-1,100, 90, 60, 20], 100)) # 3
print(sol.bitonicArray([-3,-2,-1,100, 90, 60, 20], 20)) # 6
print(sol.bitonicArray([-3,-2,-1,100, 90, 60, 20], -3)) # 0
print(sol.bitonicArray([-3, 8, 9, 20, 17, 5, 1], 17)) # 4
print(sol.bitonicArray([5, 6, 7, 8, 9, 10, 3, 2, 1], 0)) # -1
