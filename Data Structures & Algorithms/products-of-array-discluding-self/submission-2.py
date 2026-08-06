class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product of every number except that specific index

        # 2 arrays, two pointer approach
        # one multiplying everything from the left side
        # one multiplying everything from the right side (right side is reversed)

        #when trying to find the number, we just  take the previous index of the left
        #times the previous index of the right 

        left, right = [nums[0]], [nums[len(nums)-1]]

        count = 0

        i, j = 1, len(nums) - 2

        while i <= len(nums) - 1 and j >= 0:
            left.append(left[i-1] * nums[i])
            right.append(right[i-1] * nums[j])

            if nums[i] == 0:
                count += 1

            if count > 1:
                return [0] * len(nums)

            i += 1
            j -= 1

        #list should be competed
        # reverse the list here
        right = right[::-1]

        #now we can do the indexing

        ans = []
        for i in range(len(nums)):
            if i - 1 < 0:
                ans.append(right[i+1])
            elif i + 1 > len(nums) - 1:
                ans.append(left[i-1])
            else:
                ans.append(left[i-1] * right[i+1])

        return ans
