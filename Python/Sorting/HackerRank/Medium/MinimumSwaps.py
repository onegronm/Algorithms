# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# theory: https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
# use selection sort?
# use hash map?
# cycle decomposition appears to be the favored approach
# https://codereview.stackexchange.com/questions/172060/finding-the-minimum-number-of-swaps-to-sort-a-list
# one of those problems where you need to know the algorithm beforehand.
# in google phone screen interview

# important factors to consider
# a cycle of n nodes will require n-1 swaps
# a cycle with 2 nodes needs 1 swap. a cycle with 3 nodes needs 2 swaps and so on
# finds the cycles first and then uses their lengths to count the swaps.

# why it works
# this works this way because this case is somewhat unique: all elements in the array
# are unique, and once sorted, all element values match their corresponding indices.... 
# as in 1 is in position 1, 2 will be in position 2, 4 in 4, etc. That is why you can
# find one element out of place(because index!=value) and immediately jump to the place
# it SHOULD BE (index==value), and do the same thing with the out-of-place element found there. 
# Eventually you will find the element that belongs to the initial index you were checking, 
# the first out-of-place element, and that whole series of elements becomes a "cycle", 
# you can perform an exact finite series of swaps to get all of those elements into their 
# corresponding indices... like the video describes haha but long story short it works this way 
# because in this array, once sorted, index==element for all indices.
# https://www.youtube.com/watch?v=J9ikRMK8Yhs

# the list can be decomposed into cycles with lengths (a-1)+(b-1)+(c-1)+...+(z-1)
# it takes n-1 swaps to implement a cycle of length n
# answer is sum of (n-1) where n is the length of the cycle

# time complexity: O(n log n)
# space complexity: O(n)
def minimumSwaps(arr):

	n = len(arr)
	# use a hash map to keep track of each number "visited"
	# for each element in arr, start a cycle
	# when cycle returns to origin, add to swap count
	# move to the next item in arr
	# if visited, then move on to the next one
	# keep doing this until no more items are left in arr

	# Create two arrays and use  
    # as pairs where first array  
    # is element and second array 
    # is position of first element
	arrpos = [*enumerate(arr)]

	# * unpacks the iterable into separate objects

	# Sort the array by array element  
    # values to get right position of  
    # every element as the elements  
    # of second array. 
    # A lambda function that adds 10 to the number passed in as an argument, and print the result:
	# x = lambda a : a + 10
	# print(x(5))
	# sorting takes n log n time
	arrpos.sort(key = lambda it:it[1]) # basically, sort by arrpos[i][1] values

	# To keep track of visited elements
	visited = {k:False for k in range(n)}
			
	answer = 0

	for i in range(n):

		# element in place or already visited
		if visited[i] or arrpos[i][0] == i:
			continue;

		cycle_size = 0
		j = i

		while not visited[j]:		
			# mark node as visited
			visited[j] = True
			# find next node
			j = arrpos[j][0]
			# increment cycle size
			cycle_size +=1

		answer += (cycle_size - 1)

	return answer


arr = [4, 3, 1, 2]

print(minimumSwaps(arr))

