# also in LeetCode: https://leetcode.com/problems/dinner-plate-stacks/
# difficulty: hard
import heapq

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


# I could not figure out how to find the left-most or right-most available stack in constant time
# it I were to save the position of non-empty stacks in a list, I would need to sort them by index
# use a stack? a hash-map?
# leaning towards a stack but how to keep the correct order?
# A: use a heap queue algorithm, also known as the priority queue algorithm.

class DinnerPlatesSolution:

    def __init__(self, capacity: int):
        self.stacks = []
        self.q = [] # record the available stack, will use heap to quickly find the smallest available stack
        self.c = capacity

    # pushes the given integer val into the leftmost stack with size less than capacity
    def push(self, val: int) -> None:

        # To push, we need to find the leftmost available position
        # first, let's remove any stacks on the left that are full
        # 1) self.q: if there is still available stack to insert plate
        # 2) self.q[0] < len(self.stacks): the leftmost available index self.q[0] is smaller than the current size of the stacks
        # 3) len(self.stacks[self.q[0]]) == self.c: the stack has reached full capacity
        while self.q and self.q[0] < len(self.stacks) and len(self.stacks[self.q[0]]) == self.c:
            # we remove the filled stack from the queue of available stacks
            heapq.heappop(self.q)
        
        # if self.q is empty, there are no available stacks to insert plate
        if not self.q:
            # open up a new stack to insert
            heapq.heappush(self.q, len(self.stacks))

        # for the newly added stack, add a new stack to self.stacks accordingly
        if self.q[0] == len(self.stacks):
            self.stacks.append([])

        # append the value to the leftmost available stack
        # (first item in the heap queue is the smallest)
        self.stacks[self.q[0]].append(val)

    def pop(self) -> int:

        # first remove all empty stacks to find the right most stack
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

         # now we reach the right most stack
        return self.popAtStack(len(self.stacks)-1)

    def popAtStack(self, index: int) -> int:

        # if the index is valid
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            # add this stack to the list of available
            heapq.heappush(self.q, index)

            # pop and return the value
            return self.stacks[index].pop()

        # there's no stack available so return -1
        return -1


        

D = DinnerPlatesSolution(2)
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

D = DinnerPlatesSolution(2)
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

D = DinnerPlatesSolution(2)
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