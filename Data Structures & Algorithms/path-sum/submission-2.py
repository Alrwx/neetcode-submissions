# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #base case, doesn't exist

        if not root:
            return False

        #does exist, check to see if it reached the leaf
        tsum = targetSum - root.val
        if not root.left and not root.right:
            return tsum == 0
        
        return self.hasPathSum(root.left, tsum) or self.hasPathSum(root.right, tsum)

        return False