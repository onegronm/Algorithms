using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public class MajorityElement
    {
        // Time complexity: O(n). We iterate over nums once and make a constant dictionary insertion
        // on each iteration. Therefore, the algorithm runs in O(n) time.
        // Space complexity: O(n). Dictionary can contain at most n-(n/2) associations so it occupies O(n) space.
        // This is because the array of length n can contain n distinct values. Since the array is guaranteed to contain
        // a majority element
        public int FindMajorityElement(int[] nums)
        {
            // first build a number frequency table
            Dictionary<int, int> frequency = new Dictionary<int, int>();

            foreach (int num in nums)
            {
                int count = 0;
                if (frequency.TryGetValue(num, out count))
                {
                    frequency[num]++;
                }
                else
                {
                    frequency.Add(num, 1);
                }
            }

            // second find out which frequency is greater than n/2 and return it
            int majorityElement = nums[0];

            foreach (int k in frequency.Keys)
            {
                int count = 0;

                frequency.TryGetValue(k, out count);

                if (count > nums.Length / 2)
                    majorityElement = k;
            }

            return majorityElement;
        }
    }
}
