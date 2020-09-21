# https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/

def hasPathSum(self, root: TreeNode, sum: int):

	if not root:
		return False;

	# helper keeps track of sum
	def helper(node, _sum, currSum):

		if not node:
			return False

		currSum += node.val

		# first need exit condition
		if not node.left and not node.right:
			return currSum == _sum

		return helper(node.left, _sum, currSum) or helper(node.right, _sum, currSum)

	return helper(root, sum, 0)