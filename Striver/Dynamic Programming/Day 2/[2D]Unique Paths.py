# https://leetcode.com/problems/unique-paths/
# memorization
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[None for i in range(m)] for j in range(n)]
        def fun(i,j):
            if i >= n or j >= m:
                return 0
            if (i,j) == (n-1,m-1):
                return 1
            if dp[i][j] is not None:
                return dp[i][j]
            dp[i][j] = fun(i+1,j) + fun(i,j+1)
            return dp[i][j]
        
        return fun(0,0)
        
