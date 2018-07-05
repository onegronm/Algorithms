using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public class SpiralMatrix
    {
        public IList<int> SpiralOrder(int[,] matrix)
        {
            IList<int> result = new List<int>();

            if (matrix.GetLength(1) == 0) return result; // there are no rows

            int leftBound = 0;
            int rightBound = matrix.GetLength(0); // #columns
            int upperBound = 0;
            int lowerBound = matrix.GetLength(1); // #rows

            while (leftBound <= rightBound && upperBound <= lowerBound)
            {
                for (int col = leftBound; col <= rightBound; col++)
                {
                    result.Add(matrix[upperBound, col]); // row THEN column
                }
                upperBound++;

                for (int row = upperBound; row <= lowerBound; row++)
                {
                    result.Add(matrix[row, rightBound]);
                }
                rightBound--;

                for (int col = rightBound; upperBound <= lowerBound && col >= leftBound; col--)
                {
                    result.Add(matrix[lowerBound, col]);
                }
                lowerBound--;

                for (int row = lowerBound; leftBound <= rightBound && row >= upperBound; row--)
                {
                    result.Add(matrix[row, leftBound]); 
                }
                leftBound++;
            }

            return result;
        }
    }
}
