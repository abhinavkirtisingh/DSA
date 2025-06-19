#https://leetcode.com/problems/triangle/
#Memorization
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        dp = []
        for i in range(N):
            temp = [None for ele in range(i+1)]
            dp.append(temp)
        def fun(i,j):
            
            if i >= N:
                return 0
            if dp[i][j] is not None:
                return dp[i][j]
            dp[i][j] = triangle[i][j] + min(fun(i+1,j), fun(i+1,j+1))
            return dp[i][j]           
            
        
        return fun(0,0)

#Tabulation:
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        dp = []
        for i in range(N-1):
            temp = [0 for ele in range(i+1)]
            dp.append(temp)
        dp.append(triangle[-1].copy())

        for i in range(N-2,-1,-1):
            for j in range(i+1):
                dp[i][j] = min(triangle[i][j] + dp[i+1][j],triangle[i][j] + dp[i+1][j+1])
        
        return dp[0][0]

# Space Optimized

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        
        
        prevRow = triangle[-1].copy()

        for i in range(N-2,-1,-1):
            for j in range(i+1):
                temp = min(triangle[i][j] + prevRow[j], triangle[i][j] + prevRow[j+1])
                prevRow[j] = temp
                temp = 0

        
        return prevRow[0]