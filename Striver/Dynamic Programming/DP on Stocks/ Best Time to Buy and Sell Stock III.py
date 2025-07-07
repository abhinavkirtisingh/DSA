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

# Tabulation

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        N = len(prices)
        dp = [[[0 for cap in range(3)] for buy in range(2)] for index in range(N+1)]        

        for index in range(N-1,-1,-1):

            for buy in range(2):

                for cap in range(1,3):
                    if buy:
                        dp[index][buy][cap] = max(dp[index+1][0][cap] - prices[index], dp[index+1][1][cap])
                    else:
                        dp[index][buy][cap] = max(prices[index] + dp[index+1][1][cap-1], dp[index+1][0][cap])

        
        return dp[0][1][2]

# Space optimized
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        N = len(prices)
        after = [[0 for cap in range(3)] for buy in range(2)] 
        cur = [[0 for cap in range(3)] for buy in range(2)] 

        for index in range(N-1,-1,-1):

            for buy in range(2):

                for cap in range(1,3):
                    if buy:
                        cur[buy][cap] = max(after[0][cap] - prices[index], after[1][cap])
                    else:
                        cur[buy][cap] = max(prices[index] + after[1][cap-1], after[0][cap])
            after = cur.copy()
        
        return after[1][2]

# N X 4 Solution
#Memorization
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        dp = [[None for i in range(4)] for j in range(N)]

        def f(index,tran):
            if tran == 4 or index == N:
                return 0
            if dp[index][tran] is not None:
                return dp[index][tran]
            if tran%2 == 0:
                dp[index][tran] = max(f(index+1,tran+1) - prices[index], f(index+1,tran))
                return dp[index][tran]
            dp[index][tran] = max(prices[index] + f(index+1,tran+1), f(index+1,tran))
            return dp[index][tran]
        
        return f(0,0)