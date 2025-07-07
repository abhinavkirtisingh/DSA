# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
# Memorization

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        N = len(prices)
        dp = [[[None for cap in range(2)] for buy in range(2)] for index in range(N)]
        def f(index,buy,cap):

            if cap == 2 or index == N:
                return 0
            if dp[index][buy][cap] is not None:
                return dp[index][buy][cap]
            if buy:
                dp[index][buy][cap] = max(f(index+1,0,cap) - prices[index], f(index+1,1,cap))
                return dp[index][buy][cap]
            dp[index][buy][cap] = max(prices[index] + f(index+1,1,cap+1), f(index+1, 0, cap))
            return dp[index][buy][cap]
        
        return f(0,1,0)