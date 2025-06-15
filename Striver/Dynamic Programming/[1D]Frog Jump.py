#tabulation
class Solution:
    def minCost(self, height):
        # code here
        
        n = len(height)
        if n == 1:
            return 0
        
        dp = [0] * n
        dp[1] = abs(height[1] - height[0])
        for i in range(2,n):
            dp[i] = min(abs(height[i-1] - height[i]) + dp[i-1], abs(height[i-2] - height[i]) + dp[i-2])
        return dp[-1]

#memorization

class Solution:
    def minCost(self, height):
        # code here
        
        n = len(height)
        if n == 1:
            return 0
        dp = [None] * n
        dp[1] = abs(height[0] - height[1])
        def fun(index):
            if index <= 0:
                return 0
            if dp[index] is not None:
                return dp[index]
            dp[index] = min(abs(height[index] - height[index-1]) + fun(index-1),abs(height[index] - height[index-2]) + fun(index-2))
            
            return dp[index]
        
        return fun(n-1)