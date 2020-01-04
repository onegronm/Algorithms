using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    public class ArraysAndStrings
    {
        // Time complexity: O(n log n) + O (n)
        // Space complexity: O(1)

        //public bool IsUnique(string word)
        //{
        //    bool result = true;
        //    var arr = word.ToCharArray();

        //    Array.Sort(arr);

        //    for (int i = 1; i < arr.Length; i++)

        //    {
        //        if (arr[i] == arr[i - 1]) return false;
        //    }

        //    return result;
        //}


        // Below is an optimized version of IsUnique(string word)
        // Time complexity = O(n)
        // Space complexity = O(1)
        public bool IsUnique(string word)
        {
            if (word.Length > 128) return false;

            bool result = true;
            bool[] char_set = new bool[128];
            for (int i = 0; i < word.Length; i++)
            {
                int val = word[i];

                if (char_set[val]) return false;

                char_set[val] = true;
            }
            return result;
        }
        
        // Time complexity =  O(a log a + b log b)
        // Space complexity = O(a + b)
        //public bool CheckPermutation(string a, string b)
        //{
        //    if (a.Length != b.Length) return false;
        //    if (a.Length == 0 && b.Length == 0) return true;

        //    var arrA = a.ToCharArray();
        //    var arrB = b.ToCharArray();

        //    Array.Sort(arrA);
        //    Array.Sort(arrB);

        //    for (int i = 0; i < arrA.Length; i++)
        //    {
        //        if (arrA[i] != arrB[i]) return false;
        //    }

        //    return true;
        //}

        // Optimized using a Dictionary
        // Time complexity = O(n) where n is the length of string a
        // Space complexity = O(n) where total number of items in dictionary is at most 2n (characters in a + b)

        public bool CheckPermutation(string a, string b)
        {
            if (a == b) return true;
            if (a.Length != b.Length) return false;

            // Key: character
            // Value: character count
            Dictionary<char, int> dic = new Dictionary<char, int>();

            // Count occurrences of each character in string a 
            // and insert/update dictionary
            for (int i = 0; i < a.Length; i++)
            {
                int count = 0;
                if (dic.TryGetValue(a[i], out count))
                {
                    count++;
                    dic[a[i]] = count;
                }
                else
                {
                    dic.Add(a[i], 1);
                }
            }

            // Repeat similar process for string b, but only decrease character count
            for (int i = 0; i < a.Length; i++)
            {
                int count = 0;
                if (dic.TryGetValue(b[i], out count))
                {
                    // this means string b had more occurences of this character than a
                    if (count < 0)
                        return false;

                    count--;
                    dic[b[i]] = count;
                }
                else return false; // b has a character that a doesn't have
            }

            // final check. All counts should equal to zero
            for (int i = 0; i < a.Length; i++)
            {
                int count = 0;
                if (dic.TryGetValue(a[i], out count))
                {
                    if (count != 0) return false;
                }
            }

            return true;

        }

        // you can treat characters by their integer representation        
        public bool CheckPermutation2(string a, string b)
        {
            if (a.Length != b.Length) return false;

            int[] letters = new int[128];

            char[] sArray = a.ToCharArray();

            foreach (char c in sArray)
                letters[c]++;

            for (int i = 0; i < b.Length; i++)
            {
                letters[b[i]]--;

                if (letters[b[i]] < 0)
                {
                    return false;
                }
            }

            return true;
        }

        // 3. URLify
        // Hints: it's often easiest to modify strings by going from the end of the string to the beginning
        // You might find you need to know the number of spaces. Can you just count them?
        // Example: "Mr. Smith   " -> "Mr.%20Smith"
        // Assume the string is long enough to fit the '%20'
        // Time complexity: O(n)
        // Space complexity: O(n)
        // Requires creating a copy of the string.
        public string URLify1(string s, int size)
        {
            StringBuilder ans = new StringBuilder();

            for (int i = 0; i < size; i++)
            {
                if (s[i] == ' ')
                {
                    ans.Append("%20");
                }
                else
                {
                    ans.Append(s[i]);
                }                               
            }

            return ans.ToString();
        }

        public string URLify(string s, int size)
        {
            char[] str = s.ToCharArray(); // use character array as strings are immutable

            int spaceCount = 0;
            for (int i = 0; i < size; i++)
            {
                if (s[i] == ' ')
                    spaceCount++;
            }

            int index = size + spaceCount * 2;

            for (int i = size - 1; i >= 0; i--)
            {
                if (str[i] == ' ')
                {
                    str[index - 1] = '0';
                    str[index - 2] = '2';
                    str[index - 3] = '%';

                    index = index - 3;
                }
                else
                {
                    str[index - 1] = str[i];
                    index--;
                }
            }

            return new string(str);
        }

        // 4. Palindrome Permutation
        public bool IsPalindromePermutation(string s)
        {
            // Hints
            // 1. You should not check for all permutations. This would be very inneficient.
            // 2. What characteristics would a string that is a permutation of a palindrome have?
            // 3. Have you tried a hash table? You should be able to get this down to O(n)
            // 4. Can you reduce the space usage by using a bit vector?

            StringBuilder str = new StringBuilder();

            for (int i = 0; i < s.Length; i++)
            {
                if (s[i] != ' ') str.Append(s[i]);
            }

            var sArray = str.ToString().ToCharArray();
            Array.Sort(sArray); // n log n            

            int count = 0;

            for (int i = 1; i < sArray.Length; i++)
            {
                if (sArray[i] == ' ') continue;

                if (sArray[i] == sArray[i - 1]) count++;
                
            }

            int numOfPairs = sArray.Length / 2;

            if (count == numOfPairs) return true;

            return false;
        }

        // 4. Alternate solution using a hash table
        // Time complexity: O(n)
        public bool isPermutationOfPalindrome(string phrase)
        {
            int[] table = buildCharFrequencyTable(phrase); // build hash table
            return checkMaxOneOdd(table);
        }

        bool checkMaxOneOdd(int[] table)
        {
            bool foundOne = false;
            foreach (int count in table)
            {
                if (count % 2 == 1)
                {
                    if (foundOne) return false;
                    else foundOne = true;
                }
            }
            return true;
        }
        
        int[] buildCharFrequencyTable(string phrase)
        {
            // Build an array a - z length. Non-letter characters will have a length of -1
            int[] table = new int['z' - 'a' + 1];

            foreach (char c in phrase.ToCharArray())
            {
                int x = getCharNumber(c);
                if (x != -1)
                {
                    table[x]++;
                }
            }

            return table;
        }

        int getCharNumber(char c)
        {
            int val = c;
            int a = 'a';
            int z = 'z';

            if (a <= val && val <= z)
            {
                return val - a;
            }

            return -1;
        }

        public void Run()
        {
            // 1. Is Unique
            bool bResult = IsUnique("hello");
            bool bResult2 = IsUnique("hh");
            bool bResult3 = IsUnique("h");
            bool bResult4 = IsUnique("");
            bool bResult5 = IsUnique("abcde");

            // 2. Check permutation
            bResult = CheckPermutation2("hello", "olleh");
            bResult2 = CheckPermutation2("", "");
            bResult3 = CheckPermutation2("hello", "lleho");
            bResult4 = CheckPermutation2("hello", "world");

            // 3. URLify
            string sResult = URLify("Mr John Smith     ", 13);

            // 4. Palindrome Permutation
            bResult = isPermutationOfPalindrome("tact coa");
            bResult2 = isPermutationOfPalindrome("otto");
            bResult3 = isPermutationOfPalindrome("hello");
        }
    }
}
