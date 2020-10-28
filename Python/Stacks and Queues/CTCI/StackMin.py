# how would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop, and min should all operate in O(1) time

# difficulty: easy

# approach: keep a separate stack with the minimum values

class StackMin:

	class Stack:		

		class Node:
			def __init__(self, item):
				self.item = item
				self.next = None

		def __init__(self):
			self.size = 0
			self.first = None

		def isEmpty(self):
			return not self.first

		def push(self, value):
			oldFirst = self.first
			newNode = self.Node(value)
			newNode.next = oldFirst
			self.first = newNode
			self.size += 1

		def pop(self):
			if self.isEmpty():
				raise Exception("Stack is empty.")
			item = self.first.item
			self.first = self.first.next
			return item

		def peek(self):
			return self.first.item

	def __init__(self):
		self.stack = self.Stack()
		self.minValuesStack = self.Stack()

	def push(self, value):
		self.stack.push(value)

		if self.minValuesStack.isEmpty() or value < self.minValuesStack.peek():
			self.minValuesStack.push(value)

	def pop(self):
		value = self.stack.pop()

		if value == self.minValuesStack.peek():
			self.minValuesStack.pop()

	def minimum(self):
		return self.minValuesStack.peek()


stack = StackMin()
stack.push(8)
stack.push(4)
stack.push(6)
stack.push(2)
stack.push(5)
stack.push(6)
stack.push(1)
print(stack.minimum())
stack.pop()
print(stack.minimum())
stack.pop()
print(stack.minimum())
stack.pop()
print(stack.minimum())
stack.pop()
print(stack.minimum())
stack.pop()
print(stack.minimum())
stack.pop()
print(stack.minimum())
stack.pop()