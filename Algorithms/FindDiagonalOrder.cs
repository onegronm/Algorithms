using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public class FindDiagonalOrder
    {
        // It's hard to come up with this solution on your own.
        // Only approach may have to be memorization

        public int[] _findDiagonalOrder(int[,] matrix)
        {
            if (matrix == null || matrix.GetLength(1) == 0) return new int[0];

            int m = matrix.GetLength(0); // columns
            int n = matrix.GetLength(1); // rows

            // setup result and working variables
            int[] result = new int[m * n];
            int col = 0, row = 0, d = 1;

            for (int i = 0; i < m * n; i++)
            {
                result[i] = matrix[row, col];
                row -= d;
                col += d;

                if (row >= m) { row = m - 1; col += 2; d = -d; }
                if (col >= n) { col = n - 1; row += 2; d = -d; }
                if (row < 0) { row = 0; d = -d; }
                if (col < 0) { col = 0; d = -d; }
            }

            return result;
        }

        static void Main(string[] args)
        {

        }
    }
}
