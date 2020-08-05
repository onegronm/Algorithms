# In order to win the prize for most cookies sold, my friend Alice and I 
# are going to merge our Girl Scout Cookies orders and enter as one unit.

# Each order is represented by an "order id" (an integer).

# We have our lists of orders sorted numerically already, in lists. 

# Write a function to merge our lists of orders into one sorted list.

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# ***** SOLUTION 1 *****
# We could simply concatenate (join together) the two lists into one, then sort the result:
# Time cost
# concatenating - You are creating a new list object each time by concatenating. This requires copying all elements from the old list into a new one, plus one extra. 
# So yes, using l = l + [i] is an O(N) algorithm, not O(1).
# Sorted() builds a new sorted list from an iterable 
# average/worst-case performance is O(n log n)
# O(n) + O(n lg n) = O(n lg n)
# Timsort: https://en.wikipedia.org/wiki/Timsort
# Sorting algorithms in Python https://stackabuse.com/sorting-algorithms-in-python/#mergesort
# def merge_sorted_lists(arr1, arr2):
#	 return sorted(arr1 + arr2);
# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
# print(merge_sorted_lists(my_list, alices_list))



# ***** Solution 2 ******
# We can do better. With this algorithm, we're not really taking advantage of the fact that
# the input lists are themselves already sorted. How can we save time by using this fact?
# Technique: 3 pointers. One for each list.
# Edge cases:
# either list has no elements or 1 element
# one list is larger than the other
# one list runs out of elements before we finish merging
def merge_lists(list1, list2):
	merged_list_size = len(list1) + len(list2)
	merged_list = [None] * merged_list_size;

	merged_list_index = 0
	list1_first_index = 0
	list2_first_index = 0

	while merged_list_index < merged_list_size:

		list1_exhausted = list1_first_index >= len(list1)
		list2_exhausted = list2_first_index >= len(list2)

		if  (not list1_exhausted and (not list2_exhausted and list1[list1_first_index] <= list2[list2_first_index])) or list2_exhausted:
			# next item is in list 1
			merged_list[merged_list_index] = list1[list1_first_index]
			list1_first_index += 1 # when list 1 is exhausted, +=1 will exceed the bounds of the array in the next loop
		elif (not list2_exhausted and (not list1_exhausted and list2[list2_first_index] <= list1[list1_first_index])) or list1_exhausted:
			# next item is in list 2
			merged_list[merged_list_index] = list2[list2_first_index]
			list2_first_index += 1
		#elif list1_exhausted: (merged in case 2)
		#	# list 1 exhausted
		#	merged_list[merged_list_index] = list2[list2_first_index]
		#	list2_first_index += 1
		#else: (merged in case 1)
		#	# list 2 exhausted
		#	merged_list[merged_list_index] = list1[list1_first_index]
		#	list1_first_index += 1


		merged_list_index += 1




	return merged_list
	


print(merge_lists(my_list, alices_list))

list_1 = []
list_2 = []

print(merge_lists(list_1, list_2))


list_1 = [1]
list_2 = []

print(merge_lists(list_1, list_2))