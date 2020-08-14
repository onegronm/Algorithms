# https://www.hackerrank.com/challenges/sparse-arrays/problem
# assume characters are encoded in ASCII (0 <= c <= 127)

# first solution O(n^2)
# could not figure out a more efficient solution with a hash map
# how to represent string as a unique key? A: the string is the key
def matchingStrings(strings, queries):

	result = [0] * len(queries)

	for i in range(len(queries)):
		for j in range(len(strings)):
			if strings[j] == queries[i]:
				result[i] += 1

	return result # array of integers (occurence of queries)


# best answer. Use a DICTIONARY with the query string as the KEY
def matchingStringsOptimized(strings, queries):

	words = {}

	for i in range(len(strings)):
		if words.get(strings[i], -1) is -1:
			words[strings[i]] = 1
		else:
			words[strings[i]] += 1

	result = []
	for i in range(len(queries)):
		result.append(words.get(queries[i], 0)) # 0 is default value if key is not found

	return result;


strings = [
	'aba',
	'baba',
	'aba',
	'xzxb'
]

queries = [
	'aba',
	'xzxb',
	'ab'
]

print(matchingStrings(strings, queries))

print(matchingStringsOptimized(strings, queries))



