using Arrays;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Algorithms.Test
{
    [TestClass]
    public class Arrays_ReverseWordsInPlaceTest
    {
        // base case
        [TestMethod]
        public void Arrays_ReverseWordsInPlaceTest_OneWordMessage()
        {
            var actual = "cake".ToCharArray();
            var expected = "cake".ToCharArray();

            ReverseWords.Reverse(actual);

            CollectionAssert.AreEqual(actual, expected);
        }

        // base case extended
        [TestMethod]
        public void Arrays_ReverseWordsInPlaceTest_TwoWordMessage()
        {
            var actual = "cake thief".ToCharArray();
            var expected = "thief cake".ToCharArray();

            ReverseWords.Reverse(actual);

            CollectionAssert.AreEqual(actual, expected);
        }

        // base case extended
        [TestMethod]
        public void Arrays_ReverseWordsInPlaceTest_ThreeWordMessage()
        {
            var actual = "cake pound steal".ToCharArray();
            var expected = "steak pound cake".ToCharArray();
                
            ReverseWords.Reverse(actual);

            CollectionAssert.AreEqual(actual, expected);            
        }

        // edge case - same length
        [TestMethod]
        public void Arrays_ReverseWordsInPlaceTest_MultipleWordsSameLength()
        {
            var actual = "the cat ate the rat".ToCharArray();
            var expected = "rat the ate cat the".ToCharArray();

            ReverseWords.Reverse(actual);

            CollectionAssert.AreEqual(actual, expected);
        }

        // edge case - different length
        [TestMethod]
        public void Arrays_ReverseWordsInPlaceTest_MultipleWordsDifferentLength()
        {
            var actual = "chocolate bundt cake is yummy".ToCharArray();
            var expected = "yummy is cake bundt chocolate".ToCharArray();

            ReverseWords.Reverse(actual);

            CollectionAssert.AreEqual(actual, expected);
        }

        // edge case - empty
        [TestMethod]
        public void Arrays_ReverseWordsInPlaceTest_EmptyString()
        {
            var actual = "".ToCharArray();
            var expected = "".ToCharArray();

            ReverseWords.Reverse(actual);

            CollectionAssert.AreEqual(actual, expected);
        }

        
    }
}
