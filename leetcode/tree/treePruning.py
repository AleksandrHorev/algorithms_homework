# https://leetcode.com/problems/binary-tree-pruning/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def constr(node):
            if (not node): return None
            if (node.val == 0):
                if (node.left):
                    node.left = constr(node.left)
                if (node.right):
                    node.right = constr(node.right)
                if (not node.left and not node.right):
                    return None
                return node
            if (node.left):
                node.left = constr(node.left)
            if (node.right):
                node.right = constr(node.right)
            return node

        return constr(root)