# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #recursively
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # if p.val != q.val:
        #     return False

        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        #iteratively

        stack = [(p, q)]

        while stack:
            l, r = stack.pop()

            if not l and not r:
                continue
            if not l or not r or l.val != r.val:
                return False

            stack.append((l.left,r.left))
            stack.append((l.right,r.right))
        
        return True
