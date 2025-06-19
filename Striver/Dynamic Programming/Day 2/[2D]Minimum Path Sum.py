# https://leetcode.com/problems/minimum-path-sum/submissions/1667762498/
#MEMORIZATION
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        N = len(grid)
        M = len(grid[0])
        dp = [[None for i in range(M)] for j in range(N)]
        def fun(i,j):
            if (i,j) == (N-1,M-1):
                return grid[i][j]
            if i >= N or j >= M:
                return float('inf')
            if dp[i][j] is not None:
                return dp[i][j]
            dp[i][j] = grid[i][j] + min(fun(i+1,j), fun(i,j+1))
            
            return dp[i][j]
        return fun(0,0)

#TABULATION 
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        N = len(grid)
        M = len(grid[0])
        dp = [[0 for i in range(M)] for j in range(N)]
        dp[0][0] = grid[0][0]
        for i in range(N):
            for j in range(M):
                if (i,j) == (0,0):
                    continue
                up = float('inf')
                left = float('inf')
                if i > 0:
                    up = dp[i-1][j]
                if j > 0:
                    left = dp[i][j-1]
                
                dp[i][j] = grid[i][j] + min(up,left)
        return dp[N-1][M-1]

# space optimized
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        N = len(grid)
        M = len(grid[0])
        
        prevRow = [float('inf') for i in range(M)]
        prevCol = grid[0][0]
        temp = [float('inf') for i in range(M)]
        for i in range(N):
            for j in range(M):
                if (i,j) == (0,0):
                    prevRow[j] = 0                    

                temp[j] = grid[i][j] + min(prevRow[j],prevCol)
                prevCol = temp[j]
                prevRow[j] = temp[j]
                temp[j] = float('inf')
            prevCol = float('inf')
        return prevRow[-1]