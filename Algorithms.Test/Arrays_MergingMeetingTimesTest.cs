using System;
using System.Collections.Generic;
using Arrays;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Algorithms.Test
{
    [TestClass]
    public class Arrays_MergingMeetingTimesTest
    {
        [TestMethod]
        public void Arrays_TestCase1()
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

        [TestMethod]
        public void Arrays_TestCase2()
        {
            var result = MergingMeetingTimes.Merge_ranges(new List<Meeting>
            {
                new Meeting(0,1), new Meeting(3, 5), new Meeting(4, 8), new Meeting(9, 10)
            });

            Assert.IsTrue(result[0].StartTime == 0);
            Assert.IsTrue(result[0].EndTime == 1);
            Assert.IsTrue(result[1].StartTime == 3);
            Assert.IsTrue(result[1].EndTime == 8);
            Assert.IsTrue(result[2].StartTime == 9);
            Assert.IsTrue(result[2].EndTime == 10);
        }

        
    }
}
