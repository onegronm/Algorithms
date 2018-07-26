using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public class MaximumSubarray
    {
        public static void Main(string[] args)
        {
            MaximumSubarray program = new MaximumSubarray();

            int[] nums = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
            int[] nums2 = { -2, -3, -1 };
            int[] nums3 = { -1, -2 };
            int[] nums4 = { -2, -1 };
            int[] nums5 = { -1 };

            int result = program.MaxSubArray(nums);
            int result2 = program.MaxSubArray(nums2);
            int result3 = program.MaxSubArray(nums3);
            int result4 = program.MaxSubArray(nums4);
            int result5 = program.MaxSubArray(nums5);

            Console.WriteLine(result);
            Console.Read();
        }

        public int MaxSubArray(int[] nums)
        {
            // let's try a different approach with recursion
            // on each function call pass the sum of ignored I and J

            int sum = 0;
            int max = 0;

            if (nums == null || nums.Length == 0)
                return sum;

            // 1. Calculate the sum of all elements
            foreach (int num in nums)
                sum += num;

            max = sum;

            int i = 0, j = nums.Length - 1;

            int totalIgnoredI = 0;
            int totalIgnoredJ = 0;

            while (i < j)
            {
                int subtractLeft = sum - nums[i] - totalIgnoredI;
                int subtractRight = sum - nums[j] - totalIgnoredJ;

                bool found = false;

                if (subtractLeft > max)
                {
                    max = subtractLeft;
                    totalIgnoredI += nums[i];
                    i++;
                    found = true;

                }

                if (subtractRight > max)
                {
                    max = subtractRight;
                    totalIgnoredJ += nums[j];
                    j--;
                    found = true;
                }

                if (!found)
                {
                    totalIgnoredJ += nums[j];
                    totalIgnoredI += nums[i];

                    i++;
                    j--;

                }                
            }

            return max;
        }
    }
}
