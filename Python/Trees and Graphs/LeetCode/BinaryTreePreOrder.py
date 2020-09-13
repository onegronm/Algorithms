from collections import deque

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# approach 1: iterative
# deferred nodes are stored in a stack
# time complexity: O(n) where n is the number of nodes.
# space complexity: O(n) where n is the number of nodes.
# there is an optimized solution O(H) where H is the height of the tree
# check https://www.geeksforgeeks.org/iterative-preorder-traversal/
def preOrderTraversalIterative(root):
	"""
    :type root: TreeNode
    :rtype: List[int]
    """
	if root is None:
		return []

	stack = deque([root])
	output = []

	while stack:

		root = stack.pop()

		if root is not None:
			output.append(root.val)

		if root.right is not None:
			stack.append(root.right)

		# left is pushed after right so left is the last item in the stack and gets visited first
		if root.left is not None:
			stack.append(root.left)

	return output


# approach 2: recursive
# deferred nodes are implicitly stored in the call stack
# time complexity: O(n) all nodes are visited once
# space complexity: O(n) as space required is proportional to the height of 
# the tree which can be equal to the number of nodes in the tree for skewed trees
def preOrderTraversalRecursive(self, root):

	output = []

	if root is not None:
		output.append(root.val)
		output += self.preOrderTraversalRecursive(root.left)
		output += self.preOrderTraversalRecursive(root.right)

	return output