class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            ind = start + ((end - start) // 2)

            if nums[ind] > target:
                end = ind - 1
            elif nums[ind] < target:
                start = ind + 1
            else:
                return ind
        return -1