# https://www.interviewcake.com/question/python3/queue-two-stacks?course=fc1&section=queues-stacks
class QueueWithStacks:
	"""
	"""

	def __init__(self):
		self.inbox = []
		self.outbox = []
		self.size = 0

	def enqueue(self, x):
		self.inbox.append(x)
		self.size += 1

	def dequeue(self):
		if self.outbox:
			return self.outbox.pop()

		# move items to out stack in reverse order
		while self.inbox:
			self.outbox.append(self.inbox.pop())

		self.size -= 1

		return self.outbox.pop()

