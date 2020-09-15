using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public static class ReverseWords
    {
        /// <summary>
        /// Write a method ReverseWords() that takes a message as an array of characters and reverses the order of the words in place.
        /// </summary>
        /// <param name="message"></param>
        public static void Reverse(char[] message)
        {
            // manipulating a string in place may involve the use of two indexes for left and right and/or a temporary variable

            // go catch fish left starts at g. right starts at f
            // fo catch gish increment left and right until right is finished
            // fi catch gosh
            // fiscatch go h
            // fishatch go c first word is finished. Left starts at h in "fish". Right starts at space after 'go'.
            // fish tch goac
            // fish cch goat start over from second c in cch for left
            // fish cah goct
            // fish cat goch
            // fish catcgo h
            // fish catcho g
            // fish catch og
            // fish catch go

            // HINT: what if reversed all the strings?
            // hsif hctac og

            // HINT: can we apply the same concept to words instead of characters?

            // How do we figure out where words begin and end?
            // a word begins in the first index or first character after a space
            // a word ends at the last index or if it's followed by a space

            int right = message.Length - 1;

            // Walk towards the middle, from both sides
            for (int left = 0; right > left; left++)
            {
                char temp = message[left];
                message[left] = message[right];
                message[right] = temp;
                right--;
            }
        }
    }
}
