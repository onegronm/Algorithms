using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public class MaximumSubarray
    {
        //public static void Main(string[] args)
        //{
        //    MaximumSubarray program = new MaximumSubarray();

        //    int[] nums = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
        //    int[] nums2 = { -2, -3, -1 };
        //    int[] nums3 = { -1, -2 };
        //    int[] nums4 = { -2, -1 };
        //    int[] nums5 = { -1 };
        //    int[] nums6 = { 1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4 };

        //    int result = program.MaxSubArray(nums);
        //    int result2 = program.MaxSubArray(nums2);
        //    int result3 = program.MaxSubArray(nums3);
        //    int result4 = program.MaxSubArray(nums4);
        //    int result5 = program.MaxSubArray(nums5);
        //    int result6 = program.MaxSubArray(nums6);

        //    Console.WriteLine(result);
        //    Console.Read();
        //}

        // O(n) solution using Dynamic Programming
        public int MaxSubArray(int[] nums)
        {
            int maxSubArray = nums[0];

            if (nums == null || nums.Length == 0)
                return maxSubArray;

            for (int i = 1; i < nums.Length; i++)
            {
                if (nums[i] + nums[i - 1] > nums[i])
                {
                    nums[i] += nums[i - 1];
                }

                if(nums[i] > maxSubArray)
                {
                    maxSubArray = nums[i];
                }
            }

            return maxSubArray;
        }

        //public int MaxSubArray(int[] nums)
        //{
        //    int sum = 0;

        //    if (nums == null || nums.Length == 0)
        //        return sum;

        //    // 1. Calculate the sum of all elements
        //    foreach (int num in nums)
        //        sum += num;

        //    int max = sum;

        //    int i = 0, j = nums.Length - 1;

        //    int sumOfDiscardedNumbers = 0;

        //    while (i < j)
        //    {
        //        int leftArraySum = sum - nums[j] - sumOfDiscardedNumbers;
        //        int rightArraySum = sum - nums[i] - sumOfDiscardedNumbers;                

        //        if (leftArraySum > max)
        //        {
        //            max = leftArraySum;
        //        }

        //        if (rightArraySum > max)
        //        {
        //            max = rightArraySum;
        //        }

        //        if (rightArraySum > leftArraySum)
        //        {
        //            sumOfDiscardedNumbers += nums[i];
        //            i++;
        //        }
        //        else
        //        {
        //            sumOfDiscardedNumbers += nums[j];
        //            j--;
        //        }                    
        //    } 

        //    return max;
        //}
    }
}
