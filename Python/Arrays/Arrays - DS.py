# Given an array of integers, print each element in reverse order as a single line of space-separated integers.

# edge cases
# list is empty

def reverseArray(a):
	
	length = len(a)
	output = [None] * length

	for i in range(0, len(a)):
		output[i] = a[length - 1]
		length -= 1

	return output;

print (reverseArray([1, 4, 3, 2]))
print (reverseArray([6676,3216,4063,8373,423,586,8850,6762]))
print (reverseArray([]))
