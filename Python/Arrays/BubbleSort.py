# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
# Time complexity: O(n^2) even if the array is sorted
def BubbleSort(arr):
	n = len(arr)

	# traverse through all array elements. First index is 0.
	for i in range(n):

		# last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 

# BubbleSort(arr)

# It can be optimized by stopping the algorithm if inner loop didn’t cause any swap.
# Worst-case O(n*n) if the array is reverse sorted
# Best-case O(n) if the array is sorted
def BubbleSortBetter(arr):
	n = len(arr)

	# traverse through all array elements. First index is 0.
	for i in range(n):

		# last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True

		# If no two elements were swapped 
        # by inner loop, then break 
		if swapped == True:
			break

BubbleSortBetter(arr)


print("Sorted array is:")
for i in range(len(arr)):
	print(arr[i])