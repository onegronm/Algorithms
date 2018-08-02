using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public class TrappingRainWater
    {
        // Solution 1: Dynamic Programming (iterate over left and right. Find difference in heights.)
        public int Trap(int[] height)
        {
            if (height == null)
                return 0;

            int ans = 0;
            int size = height.Length;

            int[] left_max = new int[size];
            int[] right_max = new int[size];

            // Iterate over left and right parts again and again just to find the highest bar size up to that index

            // Algorithm
            // 1. Find maximum height of bar from left end up to index in the array left_max
            // 2. Find maximum height of bar from right end up to index in the array right_max
            
            left_max[0] = height[0];
            for (int i = 1; i < size; i++)
            {
                left_max[i] = Math.Max(height[i], left_max[i - 1]);
            }

            right_max[size - 1] = height[size - 1];
            for (int i = size - 2; i >= 0; i--)
            {
                right_max[i] = Math.Max(height[i], right_max[i + 1]);
            }

            for (int i = 0; i < size; i++)
            {
                ans += Math.Min(left_max[i], right_max[i]) - height[i];
            }

            return ans;

        }
    }
}
