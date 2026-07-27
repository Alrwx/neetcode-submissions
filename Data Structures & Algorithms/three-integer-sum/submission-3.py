class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)

        ans = []

        first, second, third = 0, 1, len(sorted_nums) - 1

        while first != len(sorted_nums) - 2:
            while second != third:
                summation = sorted_nums[first] + sorted_nums[second] + sorted_nums[third]
                if summation == 0:
                    ans.append([sorted_nums[first], sorted_nums[second], sorted_nums[third]])
                    second += 1
                elif summation > 0:
                    third -= 1
                else:
                    second += 1
            first += 1
            second = first + 1
            third = len(sorted_nums) - 1

        answer = []
        for i in ans:
            if i not in answer:
                answer.append(i)

        return answer