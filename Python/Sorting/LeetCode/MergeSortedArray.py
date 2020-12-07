# https://leetcode.com/problems/merge-sorted-array/
# easy
import unittest
from typing import List

# O(m+n) time and O(m) additional space
# improvement: use O(1) space by starting from the end of nums1
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # create aux array of size m
        aux = [0] * m

        # copy m items into aux
        for i in range(0,m):
            aux[i] = nums1[i]

        i = 0
        j = 0

        # sort logic from merge sort
        for k in range(0,len(nums1)):
            # case exhausted nums2
            if i >= n and j < m: 
                nums1[k] = aux[j]
                j += 1
            # case exhausted aux
            elif j >= m and i < n:
                nums1[k] = nums2[i]
                i += 1
            elif nums2[i] < aux[j] and i < n:
                nums1[k] = nums2[i]
                i += 1
            elif j < m:
                nums1[k] = aux[j]
                j += 1

class Test(unittest.TestCase):
    def test_case_1(self):
        """
        """
        s = Solution()
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        s.merge(nums1,m,nums2,n)
        self.assertListEqual(nums1, [1,2,2,3,5,6])

    def test_case_2(self):
        """
        """
        s = Solution()
        nums1 = [2,5,6,0,0,0]
        m = 3
        nums2 = [1,2,3]
        n = 3
        s.merge(nums1,m,nums2,n)
        self.assertListEqual(nums1, [1,2,2,3,5,6])

unittest.main(verbosity=2)