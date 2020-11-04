# implement a MyQueue class which implements a queue using two stacks
# https://leetcode.com/problems/implement-queue-using-stacks/
# difficulty: easy


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inbox = []
        self.outbox = []      
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inbox.append(x)  
        self.size += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.size -= 1

        # if there are items in the out stack, pop
        if self.outbox:
            return self.outbox.pop()

        # if not, then fill out stack with in stack items in reverse
        while self.inbox:
            self.outbox.append(self.inbox.pop())

        # return the first item in out stack
        return self.outbox.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.outbox:
            return self.outbox[self.size - 1]
        elif self.inbox:
            return self.inbox[0]
        else:
            return None
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.inbox) == 0 and len(self.outbox) == 0


q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())
print(q.pop())
print(q.empty())

["MyQueue","push","push","push","peek","pop","peek","pop","peek","empty","pop","empty"]
[[],[1],[2],[3],[],[],[],[],[],[],[],[]]

q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
print(q.peek())
print(q.pop())
print(q.peek())
print(q.pop())
print(q.peek())
print(q.empty())
print(q.pop())
print(q.empty())