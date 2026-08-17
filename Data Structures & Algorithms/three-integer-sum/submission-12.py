class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorting everything first, and then we can work with this
        #3 pointers, first, second, third

        #first will be our anchor
        #second and third will be used to find other triplets
        # we'll use a two pointer approach

        #this should be o(n^2)

        res = []

        nums.sort()

        first, second, third = 0, 1, len(nums) - 1

        while first != len(nums) - 2:
            second = first + 1
            third = len(nums) - 1
            while second < third:
                tot = nums[first] + nums[second] + nums[third]

                if tot < 0:
                    second += 1
                elif tot > 0:
                    third -= 1
                else:
                    ans = [nums[first],nums[second],nums[third]]
                    if ans not in res:
                        res.append(ans)
                    second += 1
            first += 1

        return res
