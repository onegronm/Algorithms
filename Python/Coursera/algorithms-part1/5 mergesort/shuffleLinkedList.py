# Given a singly-linked list containing n items, rearrange the items uniformly at random. Your algorithm should consume a logarithmic (or constant) amount of extra memory and run in time proportional to n log n in the worst case. 
# difficulty: hard
# related topics: shuffling, linked lists
# https://github.com/jsong00505/CodingStudy/blob/master/coursera/algorithms/part1/week3/mergesort/shuffling_linked_list.py
import random

class LinkedList(object):

	def __init__(self):
		self.val = 0
		self.next = None

	def __init__(self, x):
		self.val = x
		self.next = None

class ShufflingLinkedList:

	def shuffle(self, head: LinkedList) -> LinkedList:
		
		if not head or not head.next:
			return head

		# find the halfway point. send two pointers down the list: one moving at speed one, and one moving at speed two. As soon as the one at speed two hits the end, you know that the one at speed one is at the halfway point.
		slow = head
		fast = head

		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next

		left = head
		right = slow.next # first node after halfway point
		slow.next = None # separate left and right linked lists

		left = shuffle(left)
		right = shuffle(right)

		return merge(left, right)

	def merge(self, left, right):

		aux = LinkedList()
		l = left
		r = right
		current = aux

		while l and r:
			rand = random.randint(0,1)

			if rand == 0:
				current.next = l
				current = current.next
				l = l.next
			else:
				current.next = r
				current = current.next
				r = r.next

		# exhausted l or r
		if l:
			current.next = l # If the left side is not traversed, connect it to current
		elif r:
			current.next = r # If the right side is not traversed, connect it to current

		return aux.next # Return the merged list


		
