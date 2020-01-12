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
    public class ReverseStringInPlaceTest
    {
        [TestMethod]
        public void ReverseStringInPlaceTest_SimpleReverseTest()
        {
            var actual = "hello".ToCharArray();
            var expected = "olleh".ToCharArray();

            ReverseStringInPlace.Reverse(actual);

            // Assert.AreEqual(actual, expected);
            // All array types are implicitly derived from System.Array, which itself is derived from System.Object. 
            // This means that all arrays are always REFERENCE TYPES which are allocated on the managed heap, and your app's variable contains a reference to the array and not the array itself.
            CollectionAssert.AreEqual(actual, expected);
        }

        [TestMethod]
        public void ReverseStringInPlaceTest_EmptyStringTest()
        {
            var actual = "".ToCharArray();
            var expected = "".ToCharArray();

            ReverseStringInPlace.Reverse(actual);

            CollectionAssert.AreEqual(actual, expected);
        }

        [TestMethod]
        public void ReverseStringInPlaceTest_SingleCharacterStringTest()
        {
            var actual = "A".ToCharArray();
            var expected = "A".ToCharArray();

            ReverseStringInPlace.Reverse(actual);

            CollectionAssert.AreEqual(actual, expected);
        }

        [TestMethod]
        public void ReverseStringInPlaceTest_LongStringTest()
        {
            var actual = "ABCDE".ToCharArray();
            var expected = "EDCBA".ToCharArray();

            ReverseStringInPlace.Reverse(actual);

            CollectionAssert.AreEqual(actual, expected);
        }
    }
}
