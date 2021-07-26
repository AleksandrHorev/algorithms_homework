# https://leetcode.com/problems/maximum-binary-tree/
# Definition for a binary tree node.

### doesn't work
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def c(arr):
            length = len(arr)
            if (not length): return None
            max = arr[0]
            index = 0
            for i in range(1, length):
                if (arr[i] > max):
                    max = arr[i]
                    index = i
            
       leftNode =      maximum()±!1!
rrightNode = maximum!!!
            return {node, arr.splite(0, i), arr.splite(i, length)}

        def constr(arr):
            { node, left, right } = maximum(arr)

        return constr(nums)