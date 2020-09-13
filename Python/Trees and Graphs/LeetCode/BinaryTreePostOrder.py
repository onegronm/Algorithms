from collections import deque
        

# level: hard
# Important, when you pop a node, ensure its children are traversed.
# time: O(N) where N is the number of nodes. We visit each node exactly once.
# space: up to O(H) to keep the stack, where H is a tree height. This could be N in the worst case. (thin only left nodes)
def postorderTraversal(self, root: TreeNode) -> List[int]:
        
    stack = deque()
    output = []
    cur = root

    while stack or cur is not None:

        while not self.isLeaf(cur):
            stack.append(cur)
            cur = cur.left

        if cur is not None:
            output.append(cur.val)

        while stack and cur is stack[-1].right: # peek by finding the last element (rightmost)
            cur = stack.pop()
            output.append(cur.val)

        if not stack:
            cur = None
        else:
            cur = stack[-1].right

    return output

def isLeaf(self, r):

    if r is None:
        return True

    return r.left is None and r.right is None

def postorderRecursive(self, root: TreeNode):

    if root is None:
        return []

    output = []
    output += self.postorderRecursive(root.left)
    output += self.postorderRecursive(root.right)
    output.append(root.val)

    return output



