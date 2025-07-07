# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#MEMORIZATION 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        N = len(prices)
        dp = [[None for i in range(2)] for j in range(N)]
        def f(index,yn):
            
            if index == N:
                return 0
            if dp[index][yn] is not None:
                return dp[index][yn]
            if yn:
                dp[index][yn] = max(f(index+1,0) - prices[index], f(index+1,1))
                return dp[index][yn]
            dp[index][yn] = max(prices[index] + f(index+1,1), f(index+1,0))
            return dp[index][yn]
        
        return f(0,1)

#Tabulation

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        N = len(prices)
        dp = [[0 for i in range(2)] for j in range(N+1)]
        dp[N][0] = 0
        dp[N][1] = 0
        

        for index in range(N-1,-1,-1):
            p = 0
            for yn in range(2):            
                if yn:
                    p = max(dp[index+1][0] - prices[index], dp[index+1][1])
                else: 
                    p = max(prices[index] + dp[index+1][1], dp[index+1][0])
                dp[index][yn] = p
        return dp[0][1]

# space optimized
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        N = len(prices)
        dp = [0 for i in range(2)]
        cur = [0 for i in range(2)]
        
        

        for index in range(N-1,-1,-1):
            p = 0
            for yn in range(2):            
                if yn:
                    p = max(dp[0] - prices[index], dp[1])
                else: 
                    p = max(prices[index] + dp[1], dp[0])
                cur[yn] = p
            dp = cur.copy()
        return dp[1]
