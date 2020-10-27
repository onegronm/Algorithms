# describe how you could use a single array to implement three stacks
# similar to the N stack problem

# hints:
# divide array in 3 parts for each stack
# shift stacks around
# circular array

# Approach 1: fixed division
class ThreeInOneFixedDivision:

	def __init__(self, stackSize):

		self.numberOfStacks = 3
		self.stackCapacity = stackSize
		self.sizes = [0] * 3
		self.values = [0] * stackSize * self.numberOfStacks		
		
	def push(self, stack, value):
		if self.isFull(stack):
			raise Exception("Stack is full.")

		self.sizes[stack] += 1 # increment sizes array
		self.values[self.indexOfTop(stack)] += value

	def isFull(self, stack):
		return self.sizes[stack] == self.stackCapacity

	def indexOfTop(self, stack):
		offSet = stack * self.stackCapacity
		size = self.sizes[stack]
		return offSet + size - 1

stacks = ThreeInOneFixedDivision(3)
stacks.push(0,12)
stacks.push(0,2)
stacks.push(0,100)
stacks.push(1,38)
stacks.push(1,77)
stacks.push(1,42)
stacks.push(2,54)
stacks.push(2,81)
stacks.push(2,63)
print(stacks)