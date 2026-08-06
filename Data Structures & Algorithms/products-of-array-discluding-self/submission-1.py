class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        mult, zer = 1, 0

        for num in nums:
            if num:
                mult *= num
            else:
                zer += 1

        if zer > 1:
            return [0] * len(nums)

        for i in range(len(nums)):
            if zer > 1:
                return answer
            elif zer == 1:
                if nums[i] == 0:
                    answer[i] = mult
            else:
                answer[i] = mult // nums[i]
        return answer