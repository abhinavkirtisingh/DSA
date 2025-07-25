# Memorization
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        N = len(prices)
        dp = [[[None for i in range(k+1)] for j in range(2)] for ki in range(N)]
        def f(index,buy,tran):
            if tran == 0 or index == N:
                return 0
            if dp[index][buy][tran] is not None:
                return dp[index][buy][tran]
            if buy:
                dp[index][buy][tran] = max(f(index+1,0,tran) - prices[index], f(index+1,1,tran))
                return dp[index][buy][tran]
            dp[index][buy][tran] = max(prices[index] + f(index+1,1,tran-1), f(index+1,0,tran))
            return dp[index][buy][tran]
        
        return f(0,1,k)

# N X (K X 2) 
# Memorization
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        N = len(prices)
        dp = [[None for i in range(2*k)] for j in range(N)]
        def f(index,tran):

            if tran == (2*k) or index == N:
                return 0
            if dp[index][tran] is not None:
                return dp[index][tran]
            if tran%2 == 0:
                dp[index][tran] = max(f(index+1,tran+1) - prices[index], f(index+1,tran))
                return dp[index][tran]
            dp[index][tran] = max(prices[index] + f(index+1,tran+1), f(index+1,tran))
            return dp[index][tran]
        
        return f(0,0)

# Tabulation N X (K X 2)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        N = len(prices)
        dp = [[0 for i in range((2*k)+1)] for j in range(N+1)]
        for index in range(N-1,-1,-1):
            for tran in range((2*k)):
                if tran%2 == 0:
                    dp[index][tran] = max(dp[index+1][tran+1] - prices[index], dp[index+1][tran])
                else:
                    dp[index][tran] = max(prices[index] + dp[index+1][tran+1], dp[index+1][tran])

        return dp[0][0]

# Space optimized N X (K X 2)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        N = len(prices)
        dp = [0 for i in range((2*k)+1)] 
        prev = [0 for i in range((2*k)+1)]
        for index in range(N-1,-1,-1):
            for tran in range((2*k)):
                if tran%2 == 0:
                    dp[tran] = max(prev[tran+1] - prices[index], prev[tran])
                else:
                    dp[tran] = max(prices[index] + prev[tran+1], prev[tran])
            
                prev = dp.copy()

        return dp[0]