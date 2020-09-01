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