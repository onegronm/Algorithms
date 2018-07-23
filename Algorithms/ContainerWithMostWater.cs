using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public class ContainerWithMostWater
    {
        public int MaxArea(int[] height)
        {
            int i = 0;
            int j = height.Length - 1;

            int h = 0, l = 0;
            int maxArea = 0;

            while (i < j)
            {
                l = j - i;

                // lowest height takes precedence
                if (height[i] < height[j])
                {
                    h = height[i];
                    i++;
                }
                else
                {
                    h = height[j];
                    j--;
                }

                if (h * l > maxArea)
                    maxArea = h * l;
            }

            return maxArea;
        }
    }
}
