# Use your Stack class to implement a new class MaxStack with a method get_max() that returns the largest element in the stack. get_max() should not remove the item.
# https://www.interviewcake.com/question/python3/largest-stack?course=fc1&section=queues-stacks
# https://leetcode.com/problems/max-stack/
# difficulty: easy

class MaxStack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
        self.maxValuesStack = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

        if len(self.maxValuesStack) == 0 or item > self.maxValuesStack[-1]:
            self.maxValuesStack.append(item)

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
            return None

        return self.maxValuesStack[-1]
        

    def popMax(self) -> int:
        """
        """
        if not self.maxValuesStack:
            return None

        val = self.maxValuesStack.pop()
        self.items.remove(val)

        return val


