
# intuition: traverse by order storing nodes on a list of lists
# each level is stored in a list
# then iterate over each list
# place a pointer left and right
# as long as L and R are the same
# the level is symmetric (return false if not)
# if all levels are symmetric (never returned False)
# then the tree is symmetric
# must save nulls in list
# intuition is correct


# Another approach is to take a preorder and postorder traversal of the tree 
# and compare the lists returned by each. If equal then true, else false.

def isSymmetricRecursive(self,root):

    if not root:
        return True
        
    levels = []

    if not root:
        return levels

    # perform post order traversal
    def helper(node, level):

        if len(levels) == level:
            levels.append([])
              
        # make sure null nodes are handled.
        if not node:
            levels[level].append(None)
        else:
            levels[level].append(node.val)            
            helper(node.left, level + 1)
            helper(node.right, level + 1)

    helper(root, 0)

    # verify if levels are symmetric
    for l in range(0, len(levels)):

        level = levels[l]

        i = 0
        j = len(level) - 1

        while i < j:

            if level[i] != level[j]:
                return False

            i += 1
            j -= 1

    return True


def isSymmetric2(self, root):

    if not root:
        return True;

    def isSymmetric(left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        return left.val == right.val and isSymmetric(left.left, right.right) and isSymmetric(left.right, right.left)

    return isSymmetric(root.left, root.right)