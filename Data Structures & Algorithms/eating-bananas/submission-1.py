class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            num = l + ((r - l) // 2)

            count = 0
            for i in range(len(piles)):
                count = count + (math.ceil(piles[i] / num))

            if count <= h:
                r = num - 1
                res = min(res, num)
            else:
                l = num + 1
        return res