class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, n in enumerate(nums):
            nfind = target - n
            if nfind in prev:
                return [prev[nfind], i]
            prev[n] = i