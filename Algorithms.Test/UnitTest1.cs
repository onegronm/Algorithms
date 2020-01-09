using System;
using System.Collections.Generic;
using Arrays;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Algorithms.Test
{
    [TestClass]
    public class MergingMeetingsTest
    {
        [TestMethod]
        public void TestCase1()
        {
            var result = MergingMeetingTimes.Merge_ranges_extra_space(new List<Meeting>
            {
                new Meeting(6, 8),
                new Meeting(1, 9),
                new Meeting(2, 4),
                new Meeting(4, 7)
            });

            Assert.IsTrue(result[0].StartTime == 1);
            Assert.IsTrue(result[0].EndTime == 9);
        }
    }
}
