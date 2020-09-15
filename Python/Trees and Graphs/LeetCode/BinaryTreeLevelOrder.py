# breadth-first search (BFS)
# time complexity: O(n) since each node is visited once
# space complexity: O(n) to keep the output structure which contains N node values
def levelOrder(self, root):

	levels = []

	if not root:
		return levels

	def helper(node, level):
		# start at the current level
		if len(levels) == level:
			levels.append([])

		# append the current node value
		levels[level].append(node.val)

		# process child nodes for the next level
		if node.left:
			helper(node.left, level + 1)
		if node.right:
			helper(node.right, level + 1)

	helper(root, 0)
	return levels

# Let's keep nodes of each tree level in the queue structure, which typically orders elements in a FIFO (first-in-first-out) manner.
#  Queue structure would be an overkill since it's designed for a safe exchange between multiple threads and hence requires locking which leads to a performance loss.
# time O(n)
# space O(n)
# We have to maintain a queue to help us to do the traversal. And the size of the queue will be at most N because each node will be pushed into the queue exactly once. Therefore, the space complexity of level-order traversal is also O(N).
def levelOrderIterative(self, root):

	levels = []
	if not root:
		return levels

	level = 0
	queue = deque([root,])

	while queue:

		# start at the current level
		levels.append([])

		# number of elements in the current level
		level_length = len(queue)

		for i in range(level_length):
			node = queue.popleft() # Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.
			# fulfill the current level
			levels[level].append(node.val)

			# add child nodes of the current level
			# in the queue for the next level
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)

		# go to the next level
		level += 1

	return levels


