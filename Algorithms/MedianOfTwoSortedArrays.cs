using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public class MedianOfTwoSortedArrays
    {
        // Time complexity: O(log(m + n))
        // Space complexity: O(m + n)
        public double FindMedianSortedArrays(int[] num1, int[] nums2)
        {
            int[] arr = JoinArrays(num1, nums2);

            int l = arr.Length;

            int middleNumberIndex = 0;
            double median = 0;

            middleNumberIndex = ((l + 1) / 2) - 1;
            if ((l + 1) % 2 == 0)
            {               
                median = arr[middleNumberIndex];
            }
            else
            {
                median = (arr[middleNumberIndex] + arr[middleNumberIndex + 1]) / 2.0;
            }

            return median;
        }

        /// <summary>
        /// Join two arrays using a two-pointer technique
        /// </summary>
        /// <param name="m"></param>
        /// <param name="n"></param>
        /// <returns></returns>
        public int[] JoinArrays(int[] m, int[] n)
        {
            int[] arr = new int[m.Length + n.Length];

            int mLeft = 0, nLeft = 0;
            int mRight = m.Length - 1, nRight = n.Length - 1;

            int i = 0;
            int j = (m.Length + n.Length) - 1;

            while(i <= j)
            {
                // Handle when there are no more elements in n (left exceeded right)
                if(nLeft > nRight)
                {
                    arr[i] = m[mLeft];
                    mLeft++;

                    if(i < j)
                    {
                        arr[j] = m[mRight];
                        mRight--;
                    }
                }
                // Handle when there are no more elements in m (left exceeded right)
                else if(mLeft > mRight)
                {
                    arr[i] = n[nLeft];
                    nLeft++;

                    if (i < j)
                    {
                        arr[j] = n[nRight];
                        nRight--;
                    }                        
                }
                else
                {
                    // Let's first compare left bounds on both arrays
                    if (m[mLeft]* m[mLeft] <= n[nLeft]* n[nLeft])
                    {
                        arr[i] = m[mLeft];
                        mLeft++;
                    }
                    else
                    {
                        arr[i] = n[nLeft];
                        nLeft++;
                    }

                    // Now compare right bounds of arrays
                    if (m[mRight]* m[mRight] > n[nRight]* n[nRight])
                    {
                        arr[j] = m[mRight];
                        mRight--;
                    }
                    else
                    {
                        arr[j] = n[nRight];
                        nRight--;
                    }
                }                

                i++;
                j--;
            }

            return arr;
        }

        public static void Main()
        {
            int[] nums1 = { 1, 3 };
            int[] nums2 = { 2 };

            MedianOfTwoSortedArrays main = new MedianOfTwoSortedArrays();

            var a = main.JoinArrays(nums1, nums2);
            

            int[] nums3 = { 1, 2 };
            int[] nums4 = { 3, 4 };

            var b = main.JoinArrays(nums3, nums4);
            var b2 = main.FindMedianSortedArrays(nums3, nums4);

            int[] nums5 = { 1};
            int[] nums6 = { 4, 2 };

            var c = main.JoinArrays(nums5, nums6);

            int[] nums7 = { 1, 3, 5, 7, 9 };
            int[] nums8 = { 2, 4, 6, 8, 10 };

            var d = main.JoinArrays(nums7, nums8);
            var d2 = main.FindMedianSortedArrays(nums7, nums8);

        }
    }
}
