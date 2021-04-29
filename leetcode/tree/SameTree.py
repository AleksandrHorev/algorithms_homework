# https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, l: TreeNode, r: TreeNode) -> bool:
        def compare(p: TreeNode, q: TreeNode) -> bool:
            if(not p and not q):
                return True
            if ((p and not q) or (not p and q)):
                return False
            if(p.val == q.val):
                return compare(p.left, q.left) and compare(p.right, q.right)
            return False
        return compare(l, r)

test = Solution().isSameTree(TreeNode(1), TreeNode(1))
print(test)