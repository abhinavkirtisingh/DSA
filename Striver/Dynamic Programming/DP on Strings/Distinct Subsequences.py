
# https://leetcode.com/problems/distinct-subsequences/submissions/1681015605/

# Memorization
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        N = len(s)
        M = len(t)
        dp = [[None for i in range(M)] for j in range(N)]

        def f(index1,index2):
            if index1 < 0 or index2 < 0:
                if index2 < 0:
                    return 1
                return 0
            if dp[index1][index2] is not None:
                return dp[index1][index2]          
            if s[index1] == t[index2]:
                dp[index1][index2] = f(index1-1,index2) + f(index1-1,index2-1) 
                return dp[index1][index2]
            dp[index1][index2] = f(index1-1,index2)
            return dp[index1][index2]
        return f(N-1,M-1)

# tabulation
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        N = len(s)
        M = len(t)
        dp = [[0 for i in range(M+1)] for j in range(N+1)]
        
        for j in range(N+1):
            dp[j][0] = 1
        
        for index1 in range(1,N+1):
            for index2 in range(1,M+1):
                if s[index1-1] == t[index2-1]:
                    dp[index1][index2] = dp[index1-1][index2] + dp[index1-1][index2-1] 
                else:  
                    dp[index1][index2] = dp[index1-1][index2]
        return dp[N][M]

# space optimized

class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        N = len(s)
        M = len(t)
        dp = [0 for i in range(M+1)]
        dp[0] = 1
        
        for index1 in range(1,N+1):
            temp = [0 for i in range(M+1)]
            temp[0] =1
            for index2 in range(1,M+1):
                if s[index1-1] == t[index2-1]:
                    temp[index2] = dp[index2] + dp[index2-1] 
                else:  
                    temp[index2] = dp[index2]
            dp = temp.copy()
        return dp[M]
