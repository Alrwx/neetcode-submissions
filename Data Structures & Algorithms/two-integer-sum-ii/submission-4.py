class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left and right pointer
        # since its non-decreasing we know that anything onthe right is BIGGER than anything on the left

        #use a 2 pointer approach to sum the 2 pointers, if its too big we move down the right, if too small we move up the left
        #we continue until sum
        #cannot use hashmap, since it requires no additonal space

        left, right = 0, len(numbers) - 1

        while left < right:
            #finding the sum of the pointers
            tot = numbers[left] + numbers[right]
            
            if tot < target:
                left += 1

            elif tot > target:
                right -= 1

            else:
                return [left + 1, right + 1]