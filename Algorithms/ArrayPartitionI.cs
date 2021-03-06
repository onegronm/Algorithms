﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public class ArrayPartitionI
    {
        //public static void Main(string[] args)
        //{
        //    ArrayPartitionI program = new ArrayPartitionI();

        //    int[] nums = { 1, 3, 2, 2 };

        //    var result = program.ArrayPairSum(nums);
        //}

        /// <summary>
        /// Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible. 
        /// n is a positive integer, which is in the range of [1, 10000].
        /// All the integers in the array will be in the range of[-10000, 10000].
        /// </summary>
        /// <param name="nums"></param>
        /// <returns></returns>
        public int ArrayPairSum(int[] nums)
        {

            // Optimized solution using a hash map
            // Time complexity: O(n). The whole hashmap arr of size n is traversed only once.
            // Space complexity: O(n). A hashmap arr of size n is used.

            int[] arr = new int[20001];

            int lim = 10000;

            foreach (int num in nums)
            {
                arr[num + lim]++;
            }

            int d = 0, sum = 0;

            for (int number = -10000; number <= 10000; number++)
            {
                int numberIndex = number + lim;
                int freq = arr[numberIndex];

                sum += ((freq + 1 - d) / 2) * number; // the frequency calculation is very confusing
                d = (2 + freq - d) % 2;
            }

            return sum;

            /* My N Log N brute force solution
            
            Time complexity: O(nlogn). Sorting takes O(nlogn) time. We iterate over the array only once.
            Space complexity: O(1). Constant extra space is used.

            int sum = 0;

            Array.Sort(nums);

            for (int i = 0; i < nums.Length; i++)
            {
                if (i % 2 == 0) sum += nums[i];
            }

            return sum;
            */
        }
    }
}
