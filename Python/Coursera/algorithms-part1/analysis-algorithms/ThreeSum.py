# https://leetcode.com/problems/3sum/

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.
# Notice that the solution set must not contain duplicate triplets.
# Must solve in quadratic time.
from typing import List

# time is O(n log n + n^2)
# TwoSum is O(n) and we call it O(n) times
# sorting takes O(n log n)
def twoSum(i: int, nums: List[int], res: List[List[int]]):

	lo = i+1
	hi = len(nums)-1

	while lo < hi:

		sum = nums[i] + nums[lo] + nums[hi]

		if sum < 0:
			# if sum < 0, increment lo. This way we are always moving towards zero
			lo+=1

		elif sum > 0:
			# if sum > 0, decrement hi. This way we are always moving towards zero
			hi-=1

		else:
			# sum is zero so we found a triplet
			arr = []
			arr.append(nums[i])
			arr.append(nums[lo])
			arr.append(nums[hi])
			
			# add it to the result res
			res.append(arr)

			# decrement hi and increment lo
			lo+=1
			hi-=1

			# increment lo while the next value is the same as before to avoid duplicates
			while lo < hi and nums[lo] == nums[lo-1]:
				lo+=1


def threeSum(nums: List[int]) -> List[List[int]]:

	res = []
	nums.sort()

	for i in range(0, len(nums)):

		# if the current value is greater than zero, break from the loop
		# Remaining values cannot sum to zero
		if nums[i] > 0:
			break

		# if the current value is the same as the previous one, skip it
		if i > 0 and nums[i] == nums[i-1]:
			continue

		# call twoSum() for the current value
		twoSum(i, nums, res)

	return res


print(threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]

