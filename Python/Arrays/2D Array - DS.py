# https://www.hackerrank.com/challenges/2d-array/problem

def hourGlassSum(arr):

	leftBound = 0
	rightBound = leftBound + 2
	upperBound = 0
	lowerBound = upperBound + 2

	highestSum = 0

	while rightBound < len(arr[0]) and lowerBound < len(arr):

		# do something...
		return highestSum


	return 1


arr = [
	[1, 1, 1, 0, 0, 0],
	[0, 1, 0, 0, 0, 0],
	[1, 1, 1, 0, 0, 0],
	[0, 0, 2, 4, 4, 0],
	[0, 0, 0, 2, 0, 0],
	[0, 0, 1, 2, 4, 0]
]

print(hourGlassSum(arr))