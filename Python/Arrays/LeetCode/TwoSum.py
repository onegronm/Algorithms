# https://leetcode.com/problems/two-sum/
from typing import List

# Given an array of integers nums and an integer target, return indices of the two numbers 
# such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
def twoSum(self, nums: List[int], target: int) -> List[int]:

	# same element cannot be used twice so can only check once
	# Q: check only with number on right or with all numbers on right?
	# A: check with all numbers on right. For example, input [3,2,3] must yield [0,2]
	# Q: compare left-most with right-most number or two consecutive numbers?
	# A: comparing two consecutive numbers takes N^2

	# time O(n^2)
	# brute force

	 # same element cannot be used twice so can only check once
	# Q: check only with number on right or with all numbers on right?
	# Q: compare left-most with right-most number or two consecutive numbers?

    if not nums or len(nums) == 1:
        return []

    i = 0
    j = 1

    # repeat until i is less than len - 1
    while i < len(nums) - 1:

        if nums[i]+nums[j] == target:
            return [i, j]

        # case second pointer reached end
        # increment i, reset j
        if j == len(nums) - 1:
            i+=1
            j=i+1
        else:
            # keep incrementing j
            j+=1

    return []


def twoSumHashmap(nums: List[int], target: int) -> List[int]:

	if not nums or len(nums) == 1:
		return []
	
	hashMap = dict() # key: number, value: array of indexes with value

	for i in range(0, len(nums)):
		if nums[i] not in hashMap.keys():
			hashMap[nums[i]] = []
			hashMap[nums[i]].append(i)
		else:
			hashMap[nums[i]].append(i)

	for i in range(0, len(nums)):

		curr = nums[i]

		needed = target - curr

		if needed in hashMap.keys():
			lastIndex = hashMap[needed].pop()
			if lastIndex != i: # do not return the current value index
				return [i, lastIndex] # return the last index with this value

	return []


print(twoSumHashmap([2,7,11,15],9)) # 0,1
print(twoSumHashmap([3,2,4],6)) # 1,2
print(twoSumHashmap([3,3],6)) # 0,1
print(twoSumHashmap([2,5,5,11],10)) # 1,2