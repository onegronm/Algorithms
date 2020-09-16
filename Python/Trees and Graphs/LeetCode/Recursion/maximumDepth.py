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
	
