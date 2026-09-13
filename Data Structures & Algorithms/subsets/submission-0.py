class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        #datastructure for dfs, make it global for outside access
        #current subset
        curr = []
        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            #decision to include nums[i]
            curr.append(nums[i])
            dfs(i+1) # the left branch of the tree

            #decision NOT to include nums[i]
            curr.pop() # pop the val that was just included
            dfs(i+1)

        dfs(0)
        return res