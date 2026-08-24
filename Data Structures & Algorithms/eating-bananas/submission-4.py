class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #maximum k will just be max(piles)
        #minimum will be 1

        #we can do binary search to find midpoint and then use that to check if it'd work, saving that to ans.
        mink = max(piles)
        
        low, high = 1, mink

        while low <= high:
            mid = low + (high - low) // 2

            count = 0
            for i in range(len(piles)):
                count += math.ceil(piles[i] / mid)

            if count <= h:
                mink = min(mid, mink)
                high = mid - 1
            else:
                low = mid + 1


        return mink