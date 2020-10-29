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
        self.leftMostStackNotFullIndex = 0      
        self.stackCapacity = capacity

    # pushes the given integer val into the leftmost stack with size less than capacity
    def push(self, val: int) -> None:
        # update value in the active stack
        stack = self.stacks[self.leftMostStackNotFullIndex]

        if stack.isFull():
            self.leftMostStackNotFullIndex += 1

            # create new stack if does not exist and update the stack pointer
            if len(self.stacks) <= self.leftMostStackNotFullIndex:
                stack = self.Stack(self.stackCapacity)
                self.stacks.append(stack)

        stack = self.stacks[self.leftMostStackNotFullIndex]
        # update the stack values
        stack.values[stack.size] = val
        stack.size += 1

    # returns the value at the top of the rightmost non-empty stack and removes it from that stack
    # returns -1 if all stacks are empty
    def pop(self) -> int:        
        stack = self.stacks[self.leftMostStackNotFullIndex]

        if stack.isEmpty():
            self.leftMostStackNotFullIndex -= 1

            if self.leftMostStackNotFullIndex < 0:
                return -1 # all stacks are empty

            stack = self.stacks[self.leftMostStackNotFullIndex]

        stack.values[stack.size] = None
        stack.size -= 1

    def popAtStack(self, index: int) -> int:
        stack = self.stacks[index]

        if stack.isEmpty():
            return -1

        val = stack.values[stack.size - 1]
        stack.values[stack.size - 1] = None
        stack.size -= 1

        # after popping the stack, update the left most stack pointer
        if index < self.leftMostStackNotFullIndex:
            self.leftMostStackNotFullIndex = index

        return val


D = DinnerPlates(2)
D.push(1)
D.push(2)
D.push(3)
D.push(4)
D.push(5)
print(D.popAtStack(0)) # Returns 2
D.push(20)
D.push(21)
print("")