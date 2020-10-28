# entire implementation is far too much work for an interview
# you could be responsible for writing pseudocode or implementing only certain components

# same as N stack problem

class MultiStack:

	class StackInfo:

		def __init__(self, start, capacity, max):
			self.size = 0
			self.start = start
			self.capacity = capacity
			self.max = max # the size of the values array

		# we will need this method to shift all elements in stack over by one
		def isWithinStackCapacity(self, index):
			return 0

		def lastCapacityIndex(self):
			return self.start + self.capacity - 1

		def lastElementIndex(self):
			return self.start + self.size - 1

		def isEmpty(self):
			return self.size == 0

		def isFull(self):
			return self.size == self.capacity

	def __init__(self, numberOfStacks, defaultStackSize):
		self.numberOfStacks = numberOfStacks
		self.defaultStackSize = defaultStackSize
		self.info = [None] * numberOfStacks # array of StackInfo
		self.values = [0] * numberOfStacks * defaultStackSize

		# initialize StackInfo array
		for i in range(0, numberOfStacks):
			self.info[i] = self.StackInfo(i * defaultStackSize, defaultStackSize, len(self.values))

		def push(self, stackNumber, value):
			if self.allStacksAreFull():
				raise Exception("All stacks are full")

			stack = info[stackNumber]

			# expand if necessary
			if stack.isFull():
				self.expand(stackNumber)

			# update stack value
			stack.size += 1
			self.values[self.adjustIndex(stack.lastElementIndex())] = value

		# adjust index to be in between 0 and values.length - 1
		def adjustIndex(self, index):
			max = len(self.values)
			return ((index % max) + max) % max

		def allStacksAreFull(self):
			isFull = True
			for i in range(0,len(self.numberOfStacks)):
				if not self.info[i].isFull():
					isFull = False
			return isFull

		# expand stack by shifting over other stacks
		def expand(self, stackNumber):
			self.shift((stackNumber + 1) % len(self.values)) # TODO
			self.info[stackNumber].capacity += 1



stacks = MultiStack(3,3)