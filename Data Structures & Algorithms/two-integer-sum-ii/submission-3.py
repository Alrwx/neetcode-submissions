class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow = 0
        fast = 0
        find = None

        while find != numbers[fast]:
            find = target - numbers[slow]
            if find == numbers[fast]:
                break
            # print(fast)
            fast+= 1
            
            if fast > len(numbers) - 1:
                slow += 1
                fast = slow + 1
            



        
        return [slow + 1, fast + 1]
            
