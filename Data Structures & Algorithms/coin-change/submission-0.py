class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # we can approach this from the bottom up, so from 0-7 
        # we already know that the specific coins will just be 1

        #so we can create an array of n+1 coins, and then we can find how many we need by taking their distance from 0


        dp = [amount + 1] * (amount + 1) # we want amount + 1 indices, since we include 0
        # we also want the number to be the biggest possible since we are finding the minimum

        dp[0] = 0 #everything should start from 0 here

        for i in range(1, amount+1): # now we start looking at the upper numbers
            coin = dp[i]
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        
        return dp[amount] if dp[amount] < amount + 1 else -1
            


