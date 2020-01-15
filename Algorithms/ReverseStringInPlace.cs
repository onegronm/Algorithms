using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    /// <summary>
    /// Write a method that takes an array of characters and reverses the letters in place.
    /// </summary>
    public static class ReverseStringInPlace
    {
        /// <summary>
        /// Time complexity: O(n)
        /// Space complexity: constant (no additional space is needed) O(1)
        /// </summary>
        /// <param name="arrayOfChar"></param>
        public static void Reverse(char[] arrayOfChar)
        {
            int lastIndex = arrayOfChar.Length - 1;

            for (int i = 0; lastIndex > i; i++)
            {
                // save the value of the last element
                var last = arrayOfChar[lastIndex];

                // replace the last element with the value of the "first" element
                arrayOfChar[lastIndex] = arrayOfChar[i];

                // replace the "first" element with the value of the last element
                arrayOfChar[i] = last;

                // move lastIndex down one position
                lastIndex--;
            }

            // Solution

            /*
            int leftIndex = 0;
            int rightIndex = arrayOfChars.Length - 1;

            while (leftIndex < rightIndex)
            {
                // Swap characters
                char temp = arrayOfChars[leftIndex];
                arrayOfChars[leftIndex] = arrayOfChars[rightIndex];
                arrayOfChars[rightIndex] = temp;

                // Move towards middle
                leftIndex++;
                rightIndex--;
            }
            */
        }
    }
}
