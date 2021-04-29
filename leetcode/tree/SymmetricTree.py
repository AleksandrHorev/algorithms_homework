# https://leetcode.com/problems/symmetric-tree/submissions/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    stack = []
    result = True
    def isSymmetric(self, root: TreeNode) -> bool:
        if (root.left):
            self.putToStack(root.left)
        if (root.right):
            self.popFromStack(root.right)
        if(len(self.stack) > 0):
          self.result = False
        return self.result
        
    def putToStack(self, node: TreeNode) -> None:
        if (node):
            self.stack.append(node)
            if (node.left):
              self.putToStack(node.left)
            if (node.right):
              self.putToStack(node.right)

    def popFromStack(self, node: TreeNode) -> None:
        if (len(self.stack) > 0 and node):
          nodeFromStack = self.stack.pop(0)
          if (nodeFromStack.val == node.val):
            if (node.left):
              self.popFromStack(node.right)
            if (node.right):
              self.popFromStack(node.left)
          else:
            self.result = False

test = Solution().isSymmetric(TreeNode(1))
print(test)