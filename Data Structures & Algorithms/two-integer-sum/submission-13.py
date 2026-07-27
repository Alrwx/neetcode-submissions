class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            indexes[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indexes and indexes[diff] != i:
                return [i, indexes[diff]]