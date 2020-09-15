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


