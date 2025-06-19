#https://leetcode.com/problems/unique-paths-ii/
#memorization
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        N = len(obstacleGrid)
        M = len(obstacleGrid[0])
        dp = [[None for i in range(M)] for j in range(N)]
        def fun(i,j):
            if i >= N or j >= M or obstacleGrid[i][j]:
                return 0
            if (i,j) == (N-1,M-1):
                return 1
            if dp[i][j] is not None:
                return dp[i][j]
            
            dp[i][j] = fun(i+1,j) + fun(i,j+1)
                        
            return dp[i][j]
        
        return fun(0,0)

#tabulation
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        N = len(obstacleGrid)
        M = len(obstacleGrid[0])
        if obstacleGrid[N-1][M-1]:
            return 0
        dp = [[0 for i in range(M)] for j in range(N)]
        dp[0][0]=1
        for i in range(N):
            for j in range(M):
                up = 0
                left = 0
                if (i,j) == (0,0):
                    continue
                if i >= 0:
                    up = dp[i-1][j] if obstacleGrid[i-1][j] != 1 else 0
                if j >= 0:
                    down = dp[i][j-1] if obstacleGrid[i][j-1] != 1 else 0
                dp[i][j] = up + down
        return dp[N-1][M-1]
        
        
# space optimized
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        N = len(obstacleGrid)
        M = len(obstacleGrid[0])
        if obstacleGrid[N-1][M-1]:
            return 0
        prevRow = [0 for i in range(M)]
        prevCol = 1
        temp = [0 for i in range(M)]
        for i in range(N):
            for j in range(M):
                
                if obstacleGrid[i][j]:
                    prevCol = 0
                    temp[j] = 0
                    prevRow[j] = 0
                    continue
                temp[j] = prevCol + prevRow[j]
                prevCol = temp[j]
                prevRow[j] = temp[j]
                temp[j] = 0
            prevCol = 0
        return prevRow[-1]
