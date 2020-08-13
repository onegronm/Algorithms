# https://www.hackerrank.com/challenges/dynamic-array/problem

# note:
# print(1%2) # one doesn't go into two any times so the original one is still left over
# to create list of empty lists DO NOT use [ [] ] * N, as that will result in the list containing the same list object N times
# ^ is the XOR operator in python. Use the XOR operator ^ between two values to perform bitwise "exclusive or"

# The function is expected to return an INTEGER_ARRAY with the values of last answer when query is 2
# The function accepts following parameters:
#  1. INTEGER n (# of sequences)
#  2. 2D_INTEGER_ARRAY queries (the queries)

#edge cases:
# 1)invalid query type (raises an exception)
# 2)1 or no sequence. (always updates index 0 of seqList)
# 3)length of query != 3 (raise excepction when < 3. Over 3 elements are ignored)
# 4)no queries (returns empty integer array. No changes)
# 5)odd sequences

#time complexity O(n)
#space complexity ?

def dynamicArray(n, queries):

	seqList = [[] for i in range(n)]
	answers = []
	lastAnswer = 0

	for i in range(len(queries)):

		#get the current query
		query = queries[i]

		if len(query) < 3:
			raise Exception("Invalid query.")

		#get the query type (1 or 2)
		queryType = query[0]

		#get the parameters
		x = query[1]
		y = query[2]

		#case append y to sequence
		if(queryType == 1):
			seqList[(x ^ lastAnswer) % n].append(y)
		#case find the value of element y % size in seq (where size is the size of seq) and assign it to last answer
		elif(queryType == 2):
			seq = seqList[(x ^ lastAnswer) % n]
			lastAnswer = seq[y % len(seq)]
			answers.append(lastAnswer)
		else:
			raise Exception("Invalid query type.")

	return answers

n = 2
queries = [
	[1, 0, 5],
	[1, 1, 7],
	[1, 0, 3],
	[2, 1, 0],
	[2, 1, 1]
]

print(dynamicArray(n, queries))

n = 3
queries = [
	[1, 0, 5],
	[1, 1, 7],
	[1, 0, 3],
	[2, 1, 0],
	[2, 1, 1]
]

print(dynamicArray(n, queries))

n = 2
queries = []

print(dynamicArray(n, queries))


