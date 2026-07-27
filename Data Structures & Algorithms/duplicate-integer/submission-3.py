class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for thing in nums:
            if thing not in seen:
                seen.add(thing)
            else:
                return True

        return False