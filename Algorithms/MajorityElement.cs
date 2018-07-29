using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public class MajorityElement
    {
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
