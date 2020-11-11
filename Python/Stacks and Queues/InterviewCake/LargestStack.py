# Use your Stack class to implement a new class MaxStack with a method get_max() that returns the largest element in the stack. get_max() should not remove the item.
# https://www.interviewcake.com/question/python3/largest-stack?course=fc1&section=queues-stacks
# https://leetcode.com/problems/max-stack/
# difficulty: easy

class MaxStack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
        self.maxValuesStack = []
        self.maxIndex = {}

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

        if len(self.maxValuesStack) == 0 or item >= self.maxValuesStack[-1]:
            self.maxValuesStack.append(item)
            # save the index of the maximum
            self.maxIndex[item] = len(self.items) - 1

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
        if not self.maxValuesStack and not self.items:
            return None

        if not self.maxValuesStack:
            return self.items[-1]

        return self.maxValuesStack[-1]
        

    def popMax(self) -> int:
        """
        """
        if not self.maxValuesStack and not self.items:
            return None

        if self.maxValuesStack:
            val = self.maxValuesStack.pop()
        else:
            val = self.items.pop()

        if val in self.maxIndex.keys():
            self.items.pop(self.maxIndex[val])
        else:
            self.items.pop()

        return val

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

["MaxStack","push","push","popMax","peekMax"]
[[],[5],[1],[],[]]
# Expected: [null,null,null,5,1]

stack = MaxStack();
stack.push(5); 
stack.push(1);
print(stack.popMax()); #-> 5
print(stack.peekMax()); #-> 5


stack = MaxStack();
stack.push(5); 
stack.push(5);
print(stack.popMax()); #
print(stack.popMax()); #

