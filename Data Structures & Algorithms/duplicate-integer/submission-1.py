class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i-1] in nums[i:]:
                return True
        return False