class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set(nums)

        return len(nums) != len(visited)