# Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


def TwoSum(numbers: List[int], target: int) -> List[int]:

	if not numbers or len(numbers) == 1:
		return []
	
	hashMap = {}

	for i in range(0, len(numbers)):

		if numbers[i] not in hashMap.keys():
			if i+1 < len(numbers) and numbers[i+1] == numbers[i]:
				hashMap[numbers[i]] = i + 1 # if this number repeats, use the second index
			else:
				hashMap[numbers[i]] = i # if there are repeated numbers, we only care of the first index

	for i in range(0, len(numbers)):

		curr = numbers[i]
		complement = target - curr

		if complement in hashMap.keys():
			return [i + 1, hashMap[complement] + 1] # must be non-zero based index

	return []

print(TwoSum([2,7,11,15], 9)) # [1,2]
print(TwoSum([0,0,3,4], 0)) # [1,2]
