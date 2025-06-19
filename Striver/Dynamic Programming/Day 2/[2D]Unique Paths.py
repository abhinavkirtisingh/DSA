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

#tabulation
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for i in range(m)] for j in range(n)]
        
        dp[0][0] = 1

        for i in range(n):
            for j in range(m):

                if (i,j) != (0,0) and i >= 0  and j >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[n-1][m-1]
# space optimized        
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        row = [0 for i in range(m)]
        prevCol = 1
        temp = [0 for i in range(m)]
        for i in range(n):
            for j in range(m):
                temp[j] = prevCol + row[j]
                prevCol = temp[j]
                row[j] = temp[j]
                temp[j] = 0
            prevCol = 0
        return row[-1]
        
