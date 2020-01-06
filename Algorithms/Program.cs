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

            MergingMeetingTimes.Merge_ranges(new List<Meeting> {
                new Meeting(0,1), new Meeting(3, 5), new Meeting(4, 8), new Meeting(9, 10)
            });

            Console.Read();
        }
    }
}




/*

    .OrderBy()

    This method is implemented by using deferred execution. The immediate return value is an
    object that stores all the information that is required to perform the action. The query
    represented by this method is not executed until the object is enumerated either by 
    calling its GetEnumerator method directly or by using foreach in Visual C# or For Each in Visual Basic.

    sort operation stays the typical for QuickSort O(N*logN) average / O(N2) worst case
    Mathematical analysis of quicksort shows that, on average, the algorithm takes O(n log n) 
    comparisons to sort n items. In the worst case, it makes O(n2) comparisons, though this behavior is RARE.
    
    .Add() 
    
    operation runs in O(1) time. List is a dynamic array with a number of elements
    that are needed before resizing is required (capacity). If Count exceeds Capacity while
    adding elements, the capacity is increased by automatically reallocating the internal 
    array before copying the old elements and adding the new elements.
    
    If Count is less than Capacity, this method is an O(1) operation. 
    f the capacity needs to be increased to accommodate the new element, this method becomes an O(n) operation, where n is Count.

    .Capacity 
    
    retrieving the value of this property is an O(1) operation; setting the property is an O(n) operation, where n is the new capacity.

    .Distinct() 
    
    operation runs in O(n) time

    .Where() 
    
    operation runs in O(n)

    .Contains() depends on the underlying data structure – in the case of a List, O(n)

    .ToList()
    it is an O(n) operation though it will likely only require attention in performance critical operations.
    The ToList() operation will use the List(IEnumerable<T> collection) constructor. This constructor must make a copy of the array (more generally IEnumerable<T>)
    A List<T> also uses a construct called a dynamic array which needs to be resized on demand, this resize event copies the contents of an old array to the new array. So it starts off small and increases in size if required.
    This is the difference between the Capacity and Count attributes on List<T>. 
    Capacity refers to the size of the array behind the scenes, 
    Count is the number of items in the List<T> which is always <= Capacity. 
    So when an item is added to the list, increasing it past Capacity, the size of the
    List<T> is doubled and the array is copied.

    .Select()

    .FirstOrDefault()
    https://www.nerdhold.com/coder/2014/11/25/linq-and-time-complexity/
 */
