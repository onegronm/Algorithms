# https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3237/

def findNumbers(nums):

	count = 0
	n = len(nums)

	for i in range(n):
		if (len(str(nums[i]))%2) == 0:
			count += 1

	return count


nums = [555,901,482,1771]
print(findNumbers(nums))
