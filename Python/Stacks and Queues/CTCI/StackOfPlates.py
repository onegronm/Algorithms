# also in LeetCode: https://leetcode.com/problems/dinner-plate-stacks/
# difficulty: hard

class DinnerPlates:

    class Stack:

        def __init__(self, capacity):
            self.capacity = capacity
            self.values = [None] * capacity
            self.size = 0

        def isEmpty(self):
            return self.size == 0

        def isFull(self):
            return self.size == self.capacity

    def __init__(self, capacity: int):
        self.stacks = [self.Stack(capacity)]
        self.leftMostStackNotFullIndex = 0 # index to push
        self.rightMostNonEmptyStackIndex = 0 # index to pop
        self.stackCapacity = capacity

    # pushes the given integer val into the leftmost stack with size less than capacity
    def push(self, val: int) -> None:
        stackIndex = self.findLeftMostStackNotFullIndex()

        if stackIndex == -1: # no other stacks available, so create new one
            stack = self.Stack(self.stackCapacity)
            self.stacks.append(stack)
            self.leftMostStackNotFullIndex = len(self.stacks) - 1
        else:
            stack = self.stacks[stackIndex]

        # update the stack values
        stack.values[stack.size] = val
        stack.size += 1

    # returns the value at the top of the rightmost non-empty stack and removes it from that stack
    # returns -1 if all stacks are empty
    def pop(self) -> int:
        if self.allStacksAreEmpty():
            return -1

        stack = self.stacks[self.findRightMostNonEmptyStackIndex()]
        val = stack.values[stack.size - 1]
        stack.values[stack.size - 1] = None
        stack.size -= 1

        if not val:
            return -1

        return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or self.allStacksAreEmpty():
            return -1

        stack = self.stacks[index]

        if stack.isEmpty():
            return -1

        val = stack.values[stack.size - 1]
        stack.values[stack.size - 1] = None
        stack.size -= 1

        return val    

    def findLeftMostStackNotFullIndex(self) -> int:
        
        for i in range (0, len(self.stacks)):
            if not self.stacks[i].isFull():
                return i
        # if -1, then there are no other available stacks
        return -1

    def findRightMostNonEmptyStackIndex(self) -> int:
        for i in range (len(self.stacks) - 1, -1, -1):
            if not self.stacks[i].isEmpty():
                return i

        return -1

    def allStacksAreEmpty(self) -> bool:
        result = True

        for i in range(0, len(self.stacks)):
            if not self.stacks[i].isEmpty():
                result = False

        return result


D = DinnerPlates(2)
D.push(1)
D.push(2)
D.push(3)
D.push(4)
D.push(5)
print(D.popAtStack(0)) # Returns 2
D.push(20)
D.push(21)
print(D.popAtStack(0)) # Returns 20
print(D.popAtStack(2)) # Returns 21
print(D.pop()) # Returns 5
print(D.pop()) # Returns 4
print(D.pop()) # Returns 3
print(D.pop()) # Returns 1
print(D.pop()) # Returns -1. There are no stacks
# print("break")


["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[7],[8],[20],[21],[0],[2],[],[],[],[],[]]

D = DinnerPlates(2)
D.push(1)
D.push(2)
D.push(3)
D.push(4)
D.push(7)
print(D.popAtStack(8))
D.push(20)
D.push(21)
print(D.popAtStack(0))
print(D.popAtStack(2))
print(D.pop())
print(D.pop())
print(D.pop())
print(D.pop())
print(D.pop())


["DinnerPlates","push","push","push","push","push","popAtStack","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[1],[1],[0],[],[],[],[],[]]

D = DinnerPlates(2)
D.push(1)
D.push(2)
D.push(3)
D.push(4)
D.push(5)
print(D.popAtStack(1))
print(D.popAtStack(1))
print(D.popAtStack(0))
print(D.pop())
print(D.pop())
print(D.pop())
print(D.pop())
print(D.pop())