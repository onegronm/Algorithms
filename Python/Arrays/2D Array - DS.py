# https://www.hackerrank.com/challenges/2d-array/problem

# time complexity O(n) x O(m) = O(n * m) cartesian product. Could grow quadratically.
def hourGlassSum(arr):

	if len(arr) == 0 or len(arr[0]) == 0:
		return 0

	leftBound = 0
	upperBound = 0
	lowerBound = upperBound + 2

	highestSum = 0

	# the left bound cannot exceed index 3 of arr[0]
	# the lower bound cannot exceed the length of arr
	while leftBound <= len(arr[0]) - 3:

		sumTop = arr[upperBound][leftBound] + arr[upperBound][leftBound + 1] + arr[upperBound][leftBound + 2]
		
		sumMiddle = arr[upperBound + 1][leftBound + 1]

		sumBottom = arr[lowerBound][leftBound] + arr[lowerBound][leftBound + 1] + arr[lowerBound][leftBound + 2]
		
		totalSum = sumTop + sumBottom + sumMiddle

		# in the first loop, assign first sum as highest sum
		if upperBound == 0 and leftBound == 0:
			highestSum = totalSum

		# check if current hourglass sum is highest
		if totalSum > highestSum:
			highestSum = totalSum

		# case reached the lass hourglass in arr (limits of lower and left bounds)
		if lowerBound == len(arr) - 1 and leftBound == len(arr[0]) - 3:
			return highestSum
		# case reached last hourglass in the current row
		# update left, upper, and lower bounds
		elif leftBound == len(arr[0]) - 3:
			leftBound = 0
			upperBound += 1
			lowerBound += 1
		else:
			# case there are more hourglasses left in row. Keep moving right
			leftBound += 1

		#print(totalSum)

	return highestSum


arr = [
	[1, 1, 1, 0, 0, 0],
	[0, 1, 0, 0, 0, 0],
	[1, 1, 1, 0, 0, 0],
	[0, 0, 2, 4, 4, 0],
	[0, 0, 0, 2, 0, 0],
	[0, 0, 1, 2, 4, 0]
]

print(hourGlassSum(arr))

arr = []

print(hourGlassSum(arr))