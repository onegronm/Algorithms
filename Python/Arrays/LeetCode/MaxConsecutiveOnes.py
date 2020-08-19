# https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3238/

def findMaxConsecutiveOnes(nums):

	max = 0
	nonZero = False

	sum = 0
	for i in range(0, len(nums)):

		nonZero = nums[i] == 1

		if nonZero:
			sum += 1
		else:
			if sum > max:
				max = sum
				
			sum = 0

	if sum > max:
		max = sum

	return max


arr = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(arr))
