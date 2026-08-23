from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        ordered = counts.most_common(k)

        res = [i for i,j in ordered]

        return res