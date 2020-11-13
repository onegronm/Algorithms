# Use your Stack class to implement a new class MaxStack with a method get_max() that returns the largest element in the stack. 
# https://www.interviewcake.com/question/python3/largest-stack?course=fc1&section=queues-stacks
# https://leetcode.com/problems/max-stack/
# difficulty: medium

# my first attempt:
# improvements
# use another stack to track the state of highest values
# need to sort?
# a: yes, use another stack
#class MaxStack(object):

#    def __init__(self):
#        """Initialize an empty stack"""
#        self.items = []
#        self.max = [] # stores the index of the max value

#    def push(self, item):
#        """Push a new item onto the stack"""
#        self.items.append(item)

#    def pop(self):
#        """Remove and return the last item"""
#        # If the stack is empty, return None
#        # (it would also be reasonable to throw an exception)
#        if not self.items:
#            return None

#        return self.items.pop()

#    def top(self):
#        """Return the last item without removing it"""
#        if not self.items:
#            return None

#        return self.items[-1]

#    def peekMax(self) -> int:
#        """
#        """
#        if not self.items:
#            return None

#        self.findNextMax()

#        return self.items[self.max[-1]]
        

#    def popMax(self) -> int:
#        """
#        """
#        self.findNextMax()

#        maxVal = self.items.pop(self.max.pop())

#        return maxVal

#    def findNextMax(self):

#        self.max.clear()

#        _max = self.items[0]

#        # find the highest value in the items stack
#        for i in range(0, len(self.items)):
#            if self.items[i] >= _max:
#                _max = self.items[i] 

#        # add all indexes of max occurrence
#        for i in range(0, len(self.items)):
#            if self.items[i] == _max:
#                self.max.append(i)

# two-stacks solution
# popMax O(N)
# other ops O(1)
# improvement: can we do popMax() in O(lg N) time?
class MaxStack():

    def __init__(self):
        """Initialize an empty stack"""
        self.stack = []
        self.maxStack = []

    def push(self, item):
        """Push a new item onto the stack"""
        max = item
        if self.maxStack:
            max = self.maxStack[-1]

        if max > item:
            self.maxStack.append(max) # <<< key for two-stack solution. If the item is not greater than max, we save max again in the second stack (greatest item is remembered)
        else:
            self.maxStack.append(item) 

        self.stack.append(item)
        

    def pop(self):
        """Remove and return the last item"""
        self.maxStack.pop()

        return self.stack.pop()

    def top(self):
        """Return the last item without removing it"""
        return self.stack[-1]

    def peekMax(self) -> int:
        """
        """
        return self.maxStack[-1]
        

    def popMax(self) -> int:
        """
        A third local stack is used as a buffer
        """
        max = self.peekMax()
        buffer = []

        while self.stack and self.top() != max:
            buffer.append(self.pop()) # <<< call self.pop method not self.stack.pop()

        self.pop()

        while buffer:
            self.push(buffer.pop()) # <<< call self.push not self.stack.append()

        return max







print("Test 1:")
["MaxStack","push","push","push","top","popMax","top","peekMax","pop","top"]
[[],[5],[1],[5],[],[],[],[],[],[]]

stack = MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
print(stack.top()); #-> 5
print(stack.popMax()); #-> 5
print(stack.top()); #-> 1
print(stack.peekMax()); #-> 5
print(stack.pop()); #-> 1
print(stack.top()); #-> 5

print("Test 2:")
["MaxStack","push","push","popMax","peekMax"]
[[],[5],[1],[],[]]
# Expected: [null,null,null,5,1]

stack = MaxStack();
stack.push(5); 
stack.push(1);
print(stack.popMax()); #-> 5
print(stack.peekMax()); #-> 1

print("Test 3:")
stack = MaxStack();
stack.push(5);
stack.push(5);
print(stack.popMax()); #
print(stack.popMax()); #

print("Test 4:")

["MaxStack","push","push","push","popMax","popMax","top"]
[[],[5],[1],[-5],[],[],[]]
stack = MaxStack()
stack.push(5)
stack.push(1)
stack.push(-5)
print(stack.popMax()) # 5
print(stack.popMax()) # 1
print(stack.top()) # -5

print("Test 5")
["MaxStack","push","peekMax","push","popMax","push","push","push","top","push","peekMax","push","popMax","peekMax"]
[[],[-23],[],[-74],[],[-4],[20],[68],[],[83],[],[73],[],[]]
stack = MaxStack()
stack.push(-23)
print(stack.peekMax())
stack.push(-74)
print(stack.popMax())
stack.push(20)
stack.push(68)
print(stack.top())
stack.push(83)
print(stack.peekMax())
stack.push(73)
print(stack.popMax())
print(stack.peekMax())

print("Test 6")
["MaxStack","push","peekMax","pop"]
[[],[5],[],[]]

stack = MaxStack()
stack.push(5)
print(stack.peekMax())
print(stack.pop())

["MaxStack","push","peekMax","push","popMax","push","push","push","top","push","peekMax","push","popMax","peekMax"]
[[],[-23],[],[-74],[],[-4],[20],[68],[],[83],[],[73],[],[]]

["MaxStack","push","popMax","push","push","push","pop","peekMax","push","pop","pop","push","peekMax","peekMax","push","peekMax","push","peekMax"]
[[],[-2],[],[-45],[-82],[29],[],[],[40],[],[],[66],[],[],[-61],[],[98],[]]

["MaxStack","push","push","push","popMax","popMax","top","peekMax","push","peekMax","push","pop","push","peekMax","push","top","pop","pop","push","popMax"]
[[],[-49],[-18],[-11],[],[],[],[],[21],[],[94],[],[-54],[],[58],[],[],[],[-88],[]]



stack = MaxStack()
stack.push(-49)
stack.push(-18)
stack.push(-11)
stack.popMax()
stack.popMax()
stack.top()
stack.peekMax()
stack.push(21)
stack.peekMax()
stack.push(94)
stack.pop()
stack.push(-54)
stack.peekMax()
stack.push(58)
stack.top()
stack.pop()
stack.pop()
stack.push(88)
stack.popMax()