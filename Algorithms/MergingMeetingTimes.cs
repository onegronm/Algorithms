using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Linq;

namespace Arrays
{
    /*
     
    Your company built an in-house calendar tool called HiCal. 
    You want to add a feature to see the times in a day when everyone is available.
    To do this, you’ll need to know when any team is having a meeting. 
    In HiCal, a meeting is stored as a tuple of integers (start_time, end_time).
    These integers represent the number of 30-minute blocks past 9:00am.

    (2, 3)  # Meeting from 10:00 – 10:30 am
    (6, 9)  # Meeting from 12:00 – 1:30 pm

    Write a function merge_ranges() that takes a list of multiple meeting time
    ranges and returns a list of condensed ranges.

    For example, given:

    [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

    your function would return:

    [(0, 1), (3, 8), (9, 12)]

    Do not assume the meetings are in order. The meeting times are coming from multiple teams.
    
    Write a solution that's efficient even when we can't put a nice upper bound on 
    the numbers representing our time ranges. Here we've simplified our times down 
    to the number of 30-minute slots past 9:00 am. But we want the function to work 
    even for very large numbers, like Unix timestamps. In any case, the spirit of 
    the challenge is to merge meetings where start_time and end_time don't have 
    an upper bound.
         
    */

    /// <summary>
    /// Complexity: O(nlgn) time and O(n)O(n) space.
    /// Even though we only walk through our list of meetings once to merge them, we sort all the meetings first, giving us a runtime of O(n\lg{n})O(nlgn). It's worth noting that if our input were sorted, we could skip the sort and do this in O(n)O(n) time!
    /// We create a new list of merged meeting times. In the worst case, none of the meetings overlap, giving us a list identical to the input list. Thus we have a worst-case space cost of O(n)O(n).
    /// </summary>
    public static class MergingMeetingTimes
    {
        public static void Merge_ranges(List<Meeting> meetingTimeRanges)
        {
            List<Meeting> mergedMeetings = new List<Meeting>();

            /*
             
            Breakdown

            What if we had two ranges?

            [(1, 3), (2, 4)]

            These meetings clearly overlap, so we should merge them to give:

            [(1, 4)]

            But how did we know that these meetings overlap?

            We could tell the meetings overlapped because the end time of the first 
            one was after the start time of the second one! But our ideas of "first"
            and "second" are important here—this only works after we ensure that we 
            treat the meeting that starts earlier as the "first" one.

            How would we formalize this as an algorithm? Be sure to consider these edge cases:

            1. The end time of the first meeting and the start time of the second meeting are equal. For example: [(1, 2), (2, 3)]
                These do not overlap
            2. The second meeting ends before the first meeting ends. For example: [(1, 5), (2, 3)]
                The bigger range takes precedence

            Here's a formal algorithm:

            1. We treat the meeting with earlier start time as "first," and the other as "second."
            2. If the end time of the first meeting is equal to or greater than the start time of the second meeting, we merge the two meetings into one time range. The resulting time range's start time is the first meeting's start, and its end time is the later of the two meetings' end times.
            3. Else, we leave them separate.

            So, we could compare every meeting to every other meeting in this way, merging them or leaving them separate.

            Comparing all pairs of meetings would take O(n^2) time. We can do better!
            
            If we're going to beat O(n^2) time, maybe we're going to get O(n)O(n) time? Is there a way to do this in one pass?
             
            It'd be great if, for each meeting, we could just try to merge it with the next meeting. But that's definitely not sufficient, because the ordering of our meetings is random. There might be a non-next meeting that the current meeting could be merged with.
             
            (so far sorting is not in scope)

            What if we sorted our list of meetings by start time? (!) Then any meetings that could be merged would always be adjacent!

            So we could sort our meetings, then walk through the sorted list and see if each meeting can be merged with the one after it.

            Sorting takes O(n\lg{n})O(nlgn) time in the worst case. If we can then do the merging in one pass, that's another O(n) time, for O(n lgn) overall. That's not as good as O(n)O(n), but it's better than O(n^2)
            
            */


            // First, we SORT our input list of meetings by start time so any meetings that might need to be merged are now next to each other.
            var sortedMeetings = SortList(meetingTimeRanges);

            // Initialize mergedMeetings with th earliest meeting
            mergedMeetings.Add(sortedMeetings[0]);

            // merging is done in one pass and takes n time O(n)
            foreach (var currentMeeting in sortedMeetings)
            {
                var lastMergedMeeting = mergedMeetings.Last();

                if (currentMeeting.StartTime <= lastMergedMeeting.EndTime)
                {
                    // If the current meeting overlaps with the last merged meeting,
                    // use the later end time of the two
                    lastMergedMeeting.EndTime =
                        Math.Max(lastMergedMeeting.EndTime, currentMeeting.EndTime);
                }
                else
                {
                    // Add the current meeting since it doesn't overlap
                    mergedMeetings.Add(currentMeeting);
                }
            }

            // print results
            Console.WriteLine("Merging Meeting Times:");
            foreach (var item in mergedMeetings)
            {
                Console.WriteLine(item.ToString());
            }

            // runtime = O(n log n + n + n) = O(n lgn + 2n) = O(n lg n)
        }

        private static List<Meeting> SortList(List<Meeting> meetingRanges)
        {
            // sorting with order by takes O(n lg n time) time (quickSort)
            // .ToList() takes O(n) time
            // total = n lg n + n = n lg n

            // make a copy so we don't destroy the input
            return meetingRanges.Select(m => new Meeting(m.StartTime, m.EndTime))
                .OrderBy(m => m.StartTime).ToList();
        }

        private static List<Meeting> SortListDescending(List<Meeting> meetingRanges)
        {
            return meetingRanges.Select(m => new Meeting(m.StartTime, m.EndTime))
                .OrderByDescending(m => m.StartTime).ToList();

            // n lg n + n
        }


        // Could we do this "in place" on the input list and save some space? What are the pros and cons of doing this in place?

        /// <summary>
        /// Method that takes a set of intervals, merges overlapping intervals and prints the result. 
        /// A O(n Log n) and O(1) Extra Space Solution.
        /// </summary>
        /// <param name="meetingTimeRanges"></param>
        public static List<Meeting> Merge_ranges_extra_space(List<Meeting> meetingTimeRanges)
        {
            /*
            
            We can avoid use of extra space by doing merge operations in-place. Below are detailed steps.

            1) Sort all intervals in decreasing order of start time.
            2) Traverse sorted intervals starting from first interval, 
                do following for every interval.
                    a) If current interval is not first interval and it 
                        overlaps with previous interval, then merge it with
                        previous interval. Keep doing it while the interval
                        overlaps with the previous one.         
                    b) Else add current interval to output list of intervals.
            */

            // Sort Intervals in decreasing order of start time 
            var sortedMeetings = SortListDescending(meetingTimeRanges);

            int index = 0;
            // Traverse sorted intervals starting from first interval
            // The current interval is the first element of the list so start from index 1
            for (int i = 1; i < sortedMeetings.Count; i++)
            {
                // If this is not first Interval and overlaps  
                // with the previous one 
                if (sortedMeetings[index].StartTime <= sortedMeetings[i].EndTime)
                {
                    // Merge previous and current intervals
                    sortedMeetings[index].EndTime = Math.Max(sortedMeetings[index].EndTime, sortedMeetings[i].EndTime);
                    sortedMeetings[index].StartTime = Math.Min(sortedMeetings[index].StartTime, sortedMeetings[i].StartTime);
                }
                else
                {
                    index++;

                    if (index > 1)
                    {
                        sortedMeetings[index] = sortedMeetings[i];
                    }
                }
            }

            // print results
            Console.WriteLine("Merging Meeting Times:");
            // Now arr[0..index-1] stores the merged Intervals  
            Console.WriteLine("The Merged Intervals are: ");
            for (int i = 0; i <= index; i++)
            {
                Console.WriteLine("[" + sortedMeetings[i].StartTime + ","
                                            + sortedMeetings[i].EndTime + "]");
            }

            return sortedMeetings;
        }

    }

    /// <summary>
    /// Create an object to represent the tuple
    /// </summary>
    public class Meeting
    {
        public int StartTime { get; set; }

        public int EndTime { get; set; }

        public Meeting(int startTime, int endTime)
        {
            // Number of 30 min blocks past 9:00 am
            StartTime = startTime;
            EndTime = endTime;
        }

        public override string ToString()
        {
            return $"({StartTime}, {EndTime})";
        }
    }

    
}