﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public class TwoSum
    {
        // Time complexity: O(n). We traverse the list containing n elements exactly twice. 
        // Hash table reduces lookup time to O(1)
        // Space complexity: O(n). The space required depends on the number of items stored in the hash table,
        // which stores exactly n elements.
        public int[] FindTwoSum(int[] nums, int target)
        {
            List<int> result = new List<int>();

            if (nums == null || nums.Length == 0) return result.ToArray();

            // key is the number, value is the index of the last occurrence of the number in the input array
            Dictionary<int, int> dic = new Dictionary<int, int>();

            for (int i = 0; i < nums.Length; i++)
            {
                int found;
                if (!dic.TryGetValue(nums[i], out found))
                {
                    dic.Add(nums[i], i);
                }
                else
                {
                    dic[nums[i]] = i;
                }
            }

            for (int i = 0; i < nums.Length; i++)
            {
                int val = nums[i];

                int n = target - val;

                Console.WriteLine(val + " " + n);


                // int index = Array.IndexOf(nums, n); // this has O(n) runtime
                int index = -1;

                Console.WriteLine(index);

                if (dic.TryGetValue(n, out index) && index >= 0 && i != index) // make sure we're not using the same number
                {
                    result.Add(i);
                    result.Add(index);
                    break;
                }
            }

            return result.ToArray();
        }
    }
}
