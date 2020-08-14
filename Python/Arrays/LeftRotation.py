# https://www.hackerrank.com/challenges/array-left-rotation/problem

# n - number of integers
# d - number of rotations
# arr - elements of the array in the initial state

# time O(n)
# space O(n)
def leftRotation(n, d, arr):

	# loop x number of rotations
		# on each rotation, shift each item on index to the left
		# would require 2 loops (n^2)
		# if the first element, move to the back. Save last element in a temp variable. Then move left

	# loop x number of elements in arr
		# take the # of rotations to calculate new index
		# newIndex = i - d
		# if newIndex < 0, then newIndex = len(arr) + newIndex
		# 0, 1, 2, 3

	# 0, d = 3 => 3/4 = 0.75 < 1 so will not rotate the entire array.
	# new index = 0 - 3 = -3 < 0 so then -3 + len(arr) = -3 + 4. New index is one OK

	# 1, d = 5 => 5/4 = 1.25 so will rotate the entire array once + .25
	# new index = 1 (from index, not value) - (.25 X len(arr)) = 1 - 1 = 0. New index is zero OK

	# 1, d = 55
	# d / len(arr) = 55 / 4 = 13.75. Will rotate entire array 13 times + .75
	# new index = 1 - (0.75 x len (arr)) = 1 - 3 = -2 < 0
	# so len(arr) + (-2) = 2 OK

	# 5,1,9,4,2
	# 9, d = 57
	# d / len(arr) = 57%5 = 2
	# index of 9 - 2 = 2 - 2 = 0

	# newIndex = i - (d%n)
	# case i - (d%n) < 0 then newIndex = len(arr) + (i - (d%n)) else i - (d%n)

	# create a copy to save list in original order
	arr_copy = list(arr)

	for i in range(len(arr)):
		newIndex = i - (d%n)

		if(newIndex < 0):
			newIndex = len(arr) + newIndex

		arr[newIndex] = arr_copy[i]
	
	result = ""

	# print array into string of spaced separated integers
	for i in range(len(arr)):
		result += (str(arr[i]) + " ")

	return result;

n = 5
d = 4
a = [1, 2, 3, 4, 5]

print(leftRotation(n, d, a))