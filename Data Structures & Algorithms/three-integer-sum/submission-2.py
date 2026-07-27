class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        done = set()
        nums = sorted(nums)
        first, second, third = 0, 1, 2

        ans = 0
        if len(nums) == 3:
            ans = nums[first] + nums[second] + nums[third]
            if ans == 0:
                return [[nums[first],nums[second],nums[third]]]
            else:
                return []

        for i in range(first, len(nums)-2):
            print(i, "first")
            second = i + 1
            for j in range(second, len(nums)-1):
                print(j, "second")
                third = j + 1
                for k in range(third, len(nums)):
                    print(k, "third")
                    ans = nums[i] + nums[j] + nums[k]
                    
                    if ans == 0:
                        triplets = [nums[i], nums[j], nums[k]]
                        done.add(tuple(triplets))
        result = []
        for item in done:
            result.append(item)
        return result