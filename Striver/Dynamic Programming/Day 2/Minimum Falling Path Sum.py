#https://leetcode.com/problems/minimum-falling-path-sum/
#memorization
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        N = len(matrix)
        M = len(matrix[0])
        dp = [[None for i in range(M)] for j in range(N)]
        def fun(i,j):
            
            if i == N-1 and 0 <= j <= M-1:
                return matrix[i][j]
            if i >= N or j >= M or i < 0 or j < 0:
                return float('inf')
            if dp[i][j] is not None:
                return dp[i][j]
            dp[i][j] = matrix[i][j] + min(fun(i+1,j-1),fun(i+1,j),fun(i+1,j+1))
            
            return dp[i][j]
        
        ans = float('inf')

        for i in range(M):
            ans = min(ans,fun(0,i))
            
        return ans
#tabulation

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        N = len(matrix)
        M = len(matrix[0])
        
        for i in range(1,N):
            for j in range(M):
                up=left=right = float('inf')
                if i-1 >= 0:
                    up = matrix[i-1][j]
                if i-1 >= 0 and j-1 >= 0:
                    left = matrix[i-1][j-1]
                if i-1 >= 0 and j+1 <=M-1:
                    right = matrix[i-1][j+1]
                matrix[i][j] = matrix[i][j] + min(up,left,right)

        return min(matrix[-1])
#space optimized
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        N = len(matrix)
        if N == 1:
            return min(matrix[0])
        M = len(matrix[0])
        temp = matrix[0].copy()
        temp2 = [float('inf') for i in range(M)]
        for i in range(1,N):
            for j in range(M):
                up=left=right = float('inf')
                up = temp[j]
                if j-1 >= 0:
                    left = temp[j-1]
                if j+1 <= M-1:
                    right = temp[j+1]
                ans = matrix[i][j] + min(up,left,right)
                temp2[j] = ans
            temp = temp2.copy()

        return min(temp2)