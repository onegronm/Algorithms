# https://leetcode.com/problems/intersection-of-two-arrays/

import unittest
from typing import List

class Solution:
    # my first attempt
    # runtime: O(n log n)
    # additional space: O(0)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        """
        if not nums1 or not nums2:
            return []
        
        result = []

        nums1.sort()
        nums2.sort()

        a = 0
        b = 0
        
        while a < len(nums1) and b < len(nums2):

            if a < len(nums1) and b < len(nums2) and nums1[a] == nums2[b]:
                result.append(nums1[a])
                a += 1
                b += 1

                while a > 0 and a < len(nums1) and nums1[a] == nums1[a-1]:
                    a += 1

                while b > 0 and b < len(nums2) and nums2[b] == nums2[b-1]:
                    b += 1            

            elif nums1[a] < nums2[b]:
                # shift a upwards until it reaches b
                while a < len(nums1) and nums1[a] < nums2[b]:
                    a += 1

            elif nums1[a] > nums2[b]:
                # shift b upwards until it reaches a
                while b < len(nums2) and nums2[b] < nums1[a]:
                    b += 1

        return result


class Test(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        result = solution.intersection([1],[1])
        self.assertTrue(result[0] == 1)
        self.assertTrue(len(result) == 1)

    def test_case_2(self):
        solution = Solution()
        result = solution.intersection([],[])
        self.assertTrue(len(result) == 0)

    def test_case_3(self):
        solution = Solution()
        result = solution.intersection([1],[])
        self.assertTrue(len(result) == 0)

    def test_case_4(self):
        solution = Solution()
        result = solution.intersection([1,2,2,1],[2,2])
        self.assertTrue(result[0] == 2)
        self.assertTrue(len(result) == 1)

    def test_case_5(self):
        solution = Solution()
        result = solution.intersection([4,9,5],[9,4,9,8,4])
        self.assertTrue(result[0] == 4)
        self.assertTrue(result[1] == 9)
        self.assertTrue(len(result) == 2)

    def test_case_5(self):
        solution = Solution()
        result = solution.intersection([1],[1,2])

unittest.main(verbosity=2)
