# perform level order traversal
# the length of levels will return the maximum depth
def maxDepth(self, root):

	levels = []

	if not root:
		return len(levels);

	def helper(root, level):

		# at current level
		if len(levels) == level:
			levels.append([])

		levels[level].append(root.val)

		if root.left:
			helper(root.left, level + 1)
		if root.right:
			helper(root.right, level + 1)

	helper(root, 0)
	return len(levels)

# time O(n)
# space O(n) in worst case for skewed tree (only left nodes).
# best case, tree is completely balanced, the height of the tree would be log N.
# therefore space would be O(log N)
def maxDepthSolution(self, root):

	if root is None:
		return 0

	left_height = self.maxDepth(root.left)
	right_height = self.maxDepth(root.right)

	return max(left_height, right_height) + 1  # going from bottom up, passing 1 that belongs to the parent above. Counting of levels happens going up.