from typing import List
import unittest

class TreeNode:

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def addLeft(self, val):
		self.left = TreeNode(val)
		return self.left

	def addRight(self, val):
		self.right = TreeNode(val)
		return self.right

class Solution:
	"""
	"""
	#recursive
	#def traverse(self, node: TreeNode) -> List[int]:
	#	output = []

	#	if not node:
	#		return []

	#	output += self.traverse(node.left)
	#	output.append(node.val)
	#	output += self.traverse(node.right)

	#	return output

	#iterative
	def traverse(self, node: TreeNode) -> List[int]:
		"""
		"""
		output = []
		stack = []

		self.addLeftToStack(node, stack)

		while stack:
			root = stack.pop()
			output.append(root.val)
			self.addLeftToStack(root.right, stack)

		return output

	def addLeftToStack(self, root: TreeNode, stack: List[TreeNode]):
		while root:
			stack.append(root)
			root = root.left

class Test(unittest.TestCase):

	def test1(self):
		node = TreeNode(1)
		node.addLeft(2)
		node.addRight(3)
		s = Solution()
		self.assertTrue(s.traverse(node) == [2,1,3])

	def test2(self):
		node = TreeNode(1)
		left = node.addLeft(2)
		left.addLeft(4)
		left.addRight(5)
		right = node.addRight(3)
		right.addLeft(6)
		right.addRight(7)
		s = Solution()
		self.assertTrue(s.traverse(node) == [4,2,5,1,6,3,7])

	def test3(self):
		node = TreeNode(1)
		s = Solution()
		self.assertTrue(s.traverse(node) == [1])

unittest.main(verbosity=2)