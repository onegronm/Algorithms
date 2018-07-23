using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public class ArrayPartitionI
    {
        /// <summary>
        /// Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible. 
        /// n is a positive integer, which is in the range of [1, 10000].
        /// All the integers in the array will be in the range of[-10000, 10000].
        /// </summary>
        /// <param name="nums"></param>
        /// <returns></returns>
        public int ArrayPairSum(int[] nums)
        {
            return 0;

            /* My N Log N brute force solution
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
