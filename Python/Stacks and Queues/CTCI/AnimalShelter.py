from datetime import datetime
from collections import deque

class AnimalShelter:

	class Animal:
		def __init__(self, name):
			self.name = name
			self.entryDate = datetime.now()

	class Dog(Animal):
		def __init__(self, name):
			super().__init__(name)

	class Cat(Animal):
		def __init__(self, name):
			super().__init__(name)

	def __init_(self):
		self.dogQueue = deque()
		self.catQueue = deque()

	def enqueue(self, x: Animal) -> None:
		"""
		"""
		if type(x) == type(Dog):
			self.dogQueue.append(x)
		elif type(x) == type(Cat):
			self.catQueue.append(append)


	def dequeueAny(self) -> Animal:		
		"""
		"""
		if self.dogQueue[0].entryDate > self.catQueue[0].entryDate:
			return self.dogQueue.popleft()
		
		return self.catQueue.popleft()

	def dequeueDog(self) -> Animal:
		"""
		"""

	def dequeueCat(self) -> Animal:
		"""
		"""

