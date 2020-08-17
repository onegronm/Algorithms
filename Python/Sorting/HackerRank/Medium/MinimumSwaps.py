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
# This works this way because this case is somewhat unique: all elements in the array
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
