# Use your Stack class to implement a new class MaxStack with a method get_max() that returns the largest element in the stack. 
# https://www.interviewcake.com/question/python3/largest-stack?course=fc1&section=queues-stacks
# https://leetcode.com/problems/max-stack/
# difficulty: medium

class MaxStack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
        self.maxValuesStack = []
        self.maxValuesIndexes = {} # hash table to keep track of max value indexes

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

        if len(self.maxValuesStack) == 0 or item >= self.maxValuesStack[-1]:
            self.maxValuesStack.append(item)

            if item not in self.maxValuesIndexes.keys():
                self.maxValuesIndexes[item] = []

            self.maxValuesIndexes[item].append(len(self.items) - 1)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        value = self.items.pop()

        if self.maxValuesStack and value == self.maxValuesStack[-1]:
            self.maxValuesStack.pop()

        return value

    def top(self):
        """Return the last item without removing it"""
        if not self.items:
            return None

        return self.items[-1]

    def peekMax(self) -> int:
        """
        """
        if not self.maxValuesStack:
            return self.items[-1]

        return self.maxValuesStack[-1]
        

    def popMax(self) -> int:
        """
        """
        if not self.maxValuesStack:
            return None

        maxVal = self.maxValuesStack.pop()

        returnVal = self.items.pop(self.maxValuesIndexes[maxVal][-1])

        # pop from list of maxValue indexes
        self.maxValuesIndexes[maxVal].pop()

        # if max values stack is empty and items is not empty, find the next max value
        if len(self.maxValuesIndexes[maxVal]) == 0 and len(self.items) > 0:
            self.findNextMax()

        return returnVal

    def findNextMax(self):

        max = self.items[0]

        # find the highest value in the items stack
        for i in range(0, len(self.items)):
            if self.items[i] >= max:
                max = self.items[i]

        if max not in self.maxValuesIndexes.keys(): # if item is in maxValuesIndexes then it must already be in the values stack
            self.maxValuesIndexes[max] = []
            self.maxValuesStack.append(max)        

            # add all indexes of max occurrence
            for i in range(0, len(self.items)):
                if self.items[i] == max:
                    self.maxValuesIndexes[max].append(i)


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
stack.peekMax()
stack.push(-74)
stack.popMax()
stack.push(20)
stack.push(68)
stack.top()
stack.push(83)
stack.peekMax()
stack.push(73)
stack.popMax()
stack.peekMax()


