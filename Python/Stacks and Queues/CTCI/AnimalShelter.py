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
						
	def __init__(self):
		self.dogs = deque()
		self.cats = deque()

	def enqueue(self, x: Animal) -> None:
		"""
		"""
		if isinstance(x, self.Dog):
			self.dogs.append(x)
		elif isinstance(x, self.Cat):
			self.cats.append(x)

	def dequeueAny(self) -> Animal:		
		"""
		"""
		if len(self.dogs) == 0:
			return self.cats.popleft()
		elif len(self.cats) == 0:
			return self.dogs.popleft()
		elif self.dogs[0].entryDate > self.cats[0].entryDate:
			return self.cats.popleft()
		else:
			return self.dogs.popleft()

	def dequeueDog(self) -> Animal:
		"""
		"""
		return self.dogs.popleft()

	def dequeueCat(self) -> Animal:
		"""
		"""
		return self.cats.popleft()

shelter = AnimalShelter()
dog = shelter.Dog("Spot")
shelter.enqueue(dog)
cat = shelter.Cat("Miko")
shelter.enqueue(cat)
dog = shelter.Dog("Skipper")
shelter.enqueue(dog)
cat = shelter.Cat("Nala")
shelter.enqueue(cat)
dog = shelter.Dog("Ceasar")
shelter.enqueue(dog)
cat = shelter.Cat("Biff")
shelter.enqueue(cat)
print(shelter.dequeueAny().name)
print(shelter.dequeueCat().name)
print(shelter.dequeueDog().name)
print(shelter.dequeueAny().name)
print(shelter.dequeueAny().name)
print(shelter.dequeueAny().name)

