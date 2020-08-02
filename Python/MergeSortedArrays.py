# In order to win the prize for most cookies sold, my friend Alice and I 
# are going to merge our Girl Scout Cookies orders and enter as one unit.

# Each order is represented by an "order id" (an integer).

# We have our lists of orders sorted numerically already, in lists. 

# Write a function to merge our lists of orders into one sorted list.

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# We could simply concatenate (join together) the two lists into one, then sort the result:
# Time cost
# concatenating - You are creating a new list object each time by concatenating. This requires copying all elements from the old list into a new one, plus one extra. 
# So yes, using l = l + [i] is an O(N) algorithm, not O(1).
# Sorted() builds a new sorted list from an iterable 
# average/worst-case performance is O(n log n)
# O(n) + O(n lg n) = O(n lg n)
# We can do better. With this algorithm, we're not really taking advantage of the fact that
# Timsort: https://en.wikipedia.org/wiki/Timsort
# Sorting algorithms in Python https://stackabuse.com/sorting-algorithms-in-python/#mergesort
def merge_sorted_lists(arr1, arr2):
	return sorted(arr1 + arr2);


# the input lists are themselves already sorted. How can we save time by using this fact?

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_sorted_lists(my_list, alices_list))
