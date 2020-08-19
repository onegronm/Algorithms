# https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3240/

# O(n) time and space
def sortedSquares(A):

	n = len(A)
	leftBound = 0
	rightBound = n - 1
	i = n - 1

	result = [None] * n

	while rightBound >= leftBound:

		if abs(A[rightBound]) >= abs(A[leftBound]) or rightBound == leftBound:
			result[i]=(A[rightBound] * A[rightBound])
			rightBound -= 1
		else:
			result[i]=(A[leftBound] * A[leftBound])
			leftBound += 1		
		
		i -= 1

	return result

A = [-4,-1,0,3,10]
print(sortedSquares(A))



