# describe how you could use a single array to implement three stacks

# hints:
# divide array in 3 parts for each stack
# shift stacks around
# circular array

# input: number of stacks, stack default size
# method: shift stacks around (circular array) until array is full
# when full, create new array double the size
# assume all stacks are of the same type

class ThreeInOne:

	def __init__(self, numberOfStacks, defaultStackSize):
		
		self.stack = [None] * defaultStackSize * numberOfStacks
		x = 1

stacks = ThreeInOne(3,3)
#stacks.push(0,12)
#stacks.push(0,2)
#stacks.push(1,2)


	