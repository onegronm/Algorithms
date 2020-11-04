# write a program to sort a stack such that the smallest items are on top.
# You can use an additional temporary stack, but you may not copy elements into 
# any other data structure (such as an array)

class SortStack:

	def __init__(self):
		self.inStack = []
		self.outStack = []
		self.size = 0

	def push(self, x):
		if not self.inStack:
			self.inStack.append(x)		
		else:
			if x > self.peek():
				# copy smaller items than x into temporary stack
				while self.inStack and x > self.inStack[-1]:
					self.outStack.append(self.inStack.pop())

				self.inStack.append(x)

				# copy items in temp stack back
				while self.outStack:
					self.inStack.append(self.outStack.pop())

	def pop(self):
		return self.inStack.pop()

	def peek(self):
		return self.inStack[-1]


s = SortStack();
s.push(1)
s.push(10)
s.push(5)
s.push(7)
s.push(2)
print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
s.push(1)
print(s.pop())
s.push(10)
print(s.pop())
s.push(5)
s.push(7)
print(s.pop())
print(s.pop())
s.push(2)
