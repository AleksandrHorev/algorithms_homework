# https://leetcode.com/problems/binary-tree-cameras/
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    countCameras = 0
    def minCameraCover(self, root) -> int:
      self.countCameras=0
      if self.checkNode(root)==0:
          self.countCameras+=1
      
      return self.countCameras

    def checkNode(self, node: TreeNode):
          if not node:
              return 1
          l = self.checkNode(node.left)
          r = self.checkNode(node.right)
          
          if l==0 or r==0:
              self.countCameras+=1
              return 2
          elif l==2 or r==2:
              return 1
          else:
              return 0
        

# test = Solution().minCameraCover(TreeNode(0))
# test = Solution().minCameraCover(TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0, None, TreeNode(0)))))) #[0,0,null,0,null,0,null,null,0] 2
# test = Solution().minCameraCover(TreeNode(0, TreeNode(0, TreeNode(0), TreeNode(0)))) #[0,0,null,0,0] 1
# test = Solution().minCameraCover(TreeNode(0, TreeNode(0,TreeNode(0),TreeNode(0))))# [0,0,null,0,0]
# test = Solution().minCameraCover(TreeNode(0, None, TreeNode(0, None, TreeNode(0, None, TreeNode(0)))))# [0,null,0,null,0,null,0] 2
# test = Solution().minCameraCover(TreeNode(0, TreeNode(0), TreeNode(0, None, TreeNode(0))))# [0,0,0,null,null,null,0] 2
# test = Solution().minCameraCover(TreeNode(0, TreeNode(0, TreeNode(0)), TreeNode(0, None, TreeNode(0, None, TreeNode(0)))))# [0,0,0,0,null,null,0,null,null,0] 2
# test = Solution().minCameraCover(TreeNode(0, TreeNode(0, None, TreeNode(0, TreeNode(0, None, TreeNode(0,TreeNode(0)))))))# [0,0,null,null,0,  0,null,null,0,0] 2
test = Solution().minCameraCover(TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0, None, TreeNode(0)), TreeNode(0, TreeNode(0, None, TreeNode(0)))), TreeNode(0,TreeNode(0),TreeNode(0))))))# [0,0,null,0,null,0,0,0,0,0,0,null,0,null,0,null,null,null,null,null,null,0] 4
# test = Solution().minCameraCover(TreeNode(0, TreeNode(0, None, TreeNode(0,TreeNode(0,None, TreeNode(0,TreeNode(0))))), TreeNode(0)))# [0,0,0,null,0,null,null,0,null,null,0,0] 3
print(test)