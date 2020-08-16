# new year chaos: https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# time O(n) + O(2*n) = O(n)
# O(1) additional space
def minimumBribe(q):

	# PREP
	# start with the largest number
	# traverse from right to left
	# if the number is below its original position, rotate to original position
	# count how many rotations are needed to put it back in original spot
	# if rotations > 2, then too chaotic
	# else, keep adding until you reach index 0

	bribes = 0
	index = len(q)-1

	while index >= 0:

		# check if number is under original position
		originalPosition = q[index]-1

		if index < originalPosition: # a bribe is a number that moved left from its original position

			if (originalPosition - index) > 2: # case the number would require more than 2 bribes to reach current position
				print("Too chaotic")
				return

			# rotate the number back to it's original position
			rotations = originalPosition - index
			for j in range(rotations):
				q[index+j], q[index+j+1] = q[index+j+1], q[index+j]
			bribes += rotations
		else:
			index -= 1

		# 2 1 5 3 4
		# 2 1 3 4 5
		
		# [1, 2, 5, 3, 7, 8, 6, 4] index=5
		# 1 2 5 3 7 6 4 8 index=4 (2)
		# 1 2 5 3 6 4 7 8 index=4 (2)
		# 1 2 5 3 4 6 7 8 index=4 (1)
		# 1 2 3 4 5 6 7 8 index=2 (2)

	print(bribes)

queue = [2, 1, 5, 3, 4]

minimumBribe(queue) #3

queue = [2, 5, 1, 3, 4]

minimumBribe(queue) #Too chaotic

queue = [5, 1, 2, 3, 7, 8, 6, 4]

minimumBribe(queue) #Too chaotic

queue = [1, 2, 5, 3, 7, 8, 6, 4]

# 1, 2, 5, 3, 7, 8, 6, 4
# 1 2 5 3 7 6 4 8 (2)
# 1 2 5 3 6 4 7 8 (2)
# 1 2 5 3 4 6 7 8 (1)
# 1 2 3 4 5 6 7 8 (2)

minimumBribe(queue) # 7

queue = [1, 2, 5, 3, 4, 7, 8, 6]

minimumBribe(queue) #4

queue = [5, 1, 2, 3, 7, 8, 6, 4]

minimumBribe(queue) #Too chaotic


