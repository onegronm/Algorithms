# Write a function fib() that takes an integer n and returns the nth Fibonacci number
# The Fibonacci series is a numerical series where each item is the sum of the two previous items.
# 0, 1, 1, 2, 3, 5, 8, 13, ...

# time complexity: O(log n) WRONG! each call makes two more calls. This is exponential growth. O(2^n)
# space O(n) how deep do we go in the call stack? depth of tree is proportional to n so O(n)

#f(2) 3
#f(1) f(0)

#f(3) = 5
#f(2) f(1)
#f(1) f(0)

#f(4) = 15 (2^4) = 16
#f(3) f(2)
#f(2) f(1) f(1) f(0)
#f(1) f(0) f(0) f(0) f(0) f(0) f(0) f(0)

# the number of function calls doubles with each level. Each call to fib() makes two more calls.
# this forms a binary tree where number of nodes is 2^n

def fib(n):

	if n <= 0:
		return 0
	elif n == 1:
		return 1

	return fib(n-1) + fib(n-2)



#print(fib(0)) # 0
#print(fib(1)) # 1
#print(fib(2)) # 1
#print(fib(3)) # 2
#print(fib(4)) # 3
#print(fib(5)) # 5
#print(fib(6)) # 8
#print(fib(7)) # 13


# how can we avoid doing repeat work? Test using a dictionary. If we have already calculated the value
# of f(n), return it. Requires iterative method? How else could we keep dictionary in scope? By passing reference or
# wrapping fib() in a class with an instance variable where we store the answer for any n that we compute:
# this technique of keeping a record (usually in a dictionary) so a function doesn´t run again for the same inputs
# is called MEMOIZATION
# Memoization is a common strategy for dynamic programming problems, which are problems where the solution is composed of solutions to the same problem with smaller inputs (as with the Fibonacci problem, above)

# time complexity: O(n)
# space: O(n) by dict + O(n) from occupying space in the call stack = O(n)
def fibMemo(n, dict):

	if n == 0 or n == 1:
		return n

	if dict.get(n, -1) > 0:
		return dict[n]
	else:
		dict[n] = fibMemo(n-1, dict) + fibMemo(n-2, dict)

	return dict[n]


#dict = {}

#print(fibMemo(100, dict)) #3s !!!
#print(fib(30)) # 11s

# can this be done in O(1) space? Can we avoid the extra space expense from one or both?
# use bottom up technique
# time O(n)
# space O(1)
def fibBottomUp(n):

	if n == 0 or n == 1:
		return n

	left = 0
	right = 1
	result = 1 # sum of the first two digits
	
	for i in range(2, n):
		 
		result = left + right
		left = right
		right = result

	return result


print(fibBottomUp(0))
print(fibBottomUp(1))
print(fibBottomUp(2))
print(fibBottomUp(3))
print(fibBottomUp(4))
print(fibBottomUp(5))
print(fibBottomUp(6))
print(fibBottomUp(7))
print(fibBottomUp(8))
print(fibBottomUp(9))