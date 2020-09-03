from collections import deque

# my attempt (wrong)
def inorderTraversalIterative(self, root):

	if root is None:
		return []

	if root.left is None and root.right is None:
		return [root]

	output = []
	stack = deque([root])

	while stack:

		root = stack.pop()

        if root.right is not None:
            stack.append(root.right)
            if root.left is None:
                output.append(root.val)

        if root.left is not None:
            stack.append(root.left)
            output.append(root.left.val)
            output.append(root.val)

		# i keep running into circular references. How do I avoid going down the left side again when i get
		# back to the middle node?

		# maybe it shouldn't be in the stack


		
	return output

# answer
def addLeftToStack(self, stack, root):
        while root is not None:
            stack.append(root)
            root = root.left

def inorderTraversal(self, root: TreeNode) -> List[int]:
        
    stack = deque()
    output = []

    # add the leftmost branch to the stack
    self.addLeftToStack(stack, root)

    # while there are elements in the stack, pop and move the minimum
    # possible distance to the right
    while stack:
        root = stack.pop()
        output.append(root.val)

        self.addLeftToStack(stack, root.right)

    return output

# my attempt (correct)
# time and space complexity: O(n)
def inorderTraversalRecursive(self, root: TreeNode) -> List[int]:

    output = []

    if root is not None:
        output += inorderTraversalRecursive(root.left)
        output.append(root.val)
        output += inorderTraversalRecursive(root.right)

    return output
        
