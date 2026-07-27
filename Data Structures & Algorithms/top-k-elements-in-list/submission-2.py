class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        bucket = [[]]
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for i in range(len(nums)):
            bucket.append([])

        for num, count in freq.items():
            bucket[count].append(num)

        res = []
        count = k
        for i in range(len(bucket)-1, 0, -1):
            if bucket[i]:
                for i in bucket[i]:
                    res.append(i)
                    count = count - 1
                    if count <= 0:
                        return res
        
        return res