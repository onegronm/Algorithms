using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public class TwoSum
    {
        public int[] FindTwoSum(int[] nums, int target)
        {
            List<int> result = new List<int>();


            if (nums == null || nums.Length == 0) return result.ToArray();

            // key is the number, value is the index of the last occurrence of the number in the input array
            Dictionary<int, int> dic = new Dictionary<int, int>();

            for (int i = 0; i < nums.Length; i++)
            {
                int found;
                if(!dic.TryGetValue(nums[i], out found))
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

                // int index = Array.IndexOf(nums, n); // this has O(n) runtime
                int index = -1;
                dic.TryGetValue(n, out index);

                if(index >= 0 && i != index) // make sure we're not using the same number
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
