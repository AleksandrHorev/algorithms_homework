# https://leetcode.com/problems/search-in-a-binary-search-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Only for testing purpose
    def addLeft(self, node):
        self.left = node

    def addRight(self, node):
        self.right = node

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def search(node):
            if (not node): return None
            if (node.val == val):
                return node
            else:
                leftSearch = search(node.left)
                if (leftSearch): return leftSearch
                rightSearch = search(node.right)
                if (rightSearch): return rightSearch
            
        return search(root)

        