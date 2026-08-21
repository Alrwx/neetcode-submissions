class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        l, r = 0, 1

        #two pointer appraoch]
        #left buy
        #right sell
        #we calc the betw left and right and save that to our max

        maxP = 0

        while r <= len(prices) - 1:
            #check first
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                maxP = max(maxP, prof)

            else:
                l = r
            r += 1

        return maxP


