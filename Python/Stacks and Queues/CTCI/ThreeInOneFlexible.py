# entire implementation is far too much work for an interview
# you could be responsible for writing pseudocode or implementing only certain components

class MultiStack:

	class StackInfo:

		def __init__(self, start, capacity, max):
			self.size = 0
			self.start = start
			self.capacity = capacity
			self.max = max # the size of the values array

		# we will need this method to shift all elements in stack over by one
		def isWithinStackCapacity(self, index):
			if index < 0 or index >= max:
				return False

			# if index wraps around, adjust it
			contiguousIndex = index
			if index < start:
				contiguousIndex = index + self.max

			end = self.start + self.capacity

			return start < contiguousIndex and contiguousIndex < end

		def lastCapacityIndex(self):
			return self.start + self.capacity - 1

		def lastElementIndex(self):
			return self.start + self.size - 1

		def isEmpty(self):
			return self.size == 0

		def isFull(self):
			return self.size == self.capacity


