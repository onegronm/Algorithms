using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public class BestTimeToBuyAndSellStockII
    {
        // Time complexity: O(n). Single pass.
        // Space complexity: O(1). Constant space needed.
        public int MaxProfit(int[] prices)
        {
            int maxProfit = 0;

            if (prices == null || prices.Length < 2)
                return maxProfit;

            for (int i = 1; i < prices.Length; i++)
            {
                if(prices[i] > prices[i-1])
                {
                    maxProfit += prices[i] - prices[i - 1];
                }
            }

            return maxProfit;
        }
    }
}
