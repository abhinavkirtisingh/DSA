# Memorization
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        N = len(prices)
        dp = [[None for i in range(2)] for j in range(N)]
        def f(index,buy):

            if index >= N:
                return 0
            if dp[index][buy] is not None:
                return dp[index][buy]
            if buy:
                dp[index][buy] = max(f(index+1,0) - prices[index], f(index+1,1))
                return dp[index][buy]
            dp[index][buy] = max(prices[index] + f(index+2,1), f(index+1,0))
            return dp[index][buy]
        
        return f(0,1)