# https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/538/


# intuition:
# visit each node
# keep track of repeated values with a sum variable
# when you reach the leaf, return the node's value and add 1 to sum
# if the current node value is the same the the child add 1 to sum
# a subtree starts at the bottom and goes up until it reaches
# a node with a different value

# what I tried
def countUnivalSubtrees(self, root):

	if not root:
		return 0

	def helper(node):

		if not node:
			return 0

		if not node.left and not node.right:
			return 1
		
		rightsum = helper(node.right, node.val)

		if rightSum > 0 and 

		if node.left and node.left.val == node.val:
		   sum += helper(node.left) + 1:

		if node.right and node.right.val == node.val:
		   sum += helper(node.right) + 1:

		return sum

	return helper(root)

def countUnivalSubtreesSolution(self, root: TreeNode) -> int:
        
    if not root:
        return 0

    def helper(node):
        # base case - if the node has no children this is a univalue subtree
        if not node.left and not node.right:
            # found a univalue subtree - increment
            self.count += 1 # <<< using a global variable to keep track of count
            return True

        is_Uni = True

        # check if all the node's children are unique subtrees and if they have the
        # same value. Also recursively call is_Uni for children
        if node.left:
            is_Uni = helper(node.left) and is_Uni and node.left.val == node.val

        if node.right:
            is_Uni = helper(node.right) and is_Uni and node.right.val == node.val

        # increment self.count and return a uniValue tree exists here
        self.count += is_Uni
        return is_Uni

    self.count = 0
    helper(root)	

    return self.count
        