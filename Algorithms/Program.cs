using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Arrays
{
    class Program
    {
        /*
         * a single doubling append is an O(n) time operation since we have to
         * copy all n items from our array.
         * 
         * while the time cost of each special O(n) doubling append doubles 
         * each time, the number of O(1)O(1) appends you get until the next
         * doubling append also doubles. 
         * 
         * This kind of "cancels out," and we can say each append has an average 
         * cost or amortized cost of O(1). 
         * 
         * If we were worried about that O(n)O(n)-time worst-case cost of appends, 
         * we might try to use a normal, non-dynamic array.
         * 
         * The advantage of dynamic arrays over arrays is that you don't have to 
         * specify the size ahead of time, but the disadvantage is that some appends
         * can be expensive. That's the tradeoff.
         */


        static void Main(string[] args)
        {            
            ArraysAndStrings arraysAndStrings = new ArraysAndStrings();

            arraysAndStrings.Run();

            MergingMeetingTimes mergingMeetingTimes = new MergingMeetingTimes();

            Console.Read();
        }
    }
}
