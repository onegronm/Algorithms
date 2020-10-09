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
			self.peak = nums[mid]
		# CASE mid is greater than peak, search right
		elif nums[mid] > self.peak:
			self.peak = nums[mid]
			self.findPeak(nums, mid, len(nums)-1)
		# CASE value is less than peak, search left
		else:
			self.findPeak(nums, start, mid)

	# [-3,-2,-1,100,90, 60, 20]
	# [-1,0,-2]
	# [-4,-3,-1,0,-2]
	def bitonicArray(self, arr:List[int], key: int) -> int:

		self.peak = arr[0] # assume left-most number is the smallest
		
		start = 0
		end = len(arr) - 1

		self.findPeak(arr, start, end)

		return self.peak

sol = Solution()
print(sol.bitonicArray([-3,-2,-1,100,90, 60, 20],0)) # peak 100
print(sol.bitonicArray([-3, 8, 9, 20, 17, 5, 1],0)) # peak 20
print(sol.bitonicArray([5, 6, 7, 8, 9, 10, 3, 2, 1],0)) # peak 10
