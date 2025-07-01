# https://leetcode.com/problems/edit-distance/description/
# memorization
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)
        dp = [[None for i in range(M)] for j in range(N)]
        def f(index1,index2):
            if index1 < 0 or index2 < 0:
                if index1 >= 0:
                    return index1 + 1
                return index2 + 1
            if dp[index1][index2] is not None:
                return dp[index1][index2]
            if word1[index1] == word2[index2]:
                dp[index1][index2] = f(index1-1,index2-1) 
                return f(index1-1,index2-1)   
            dp[index1][index2] = min(f(index1-1,index2-1), f(index1,index2-1),f(index1-1,index2)) + 1
            return dp[index1][index2]
            
        return f(N-1,M-1)

# tabulation
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)
        dp = [[0 for i in range(M+1)] for j in range(N+1)]
        
        for i in range(1,N+1):
            dp[i][0] = i
        for i in range(1,M+1):
            dp[0][i] = i
        for index1 in range(1,N+1):
            for index2 in range(1,M+1):
                if word1[index1-1] == word2[index2-1]:
                    dp[index1][index2] = dp[index1-1][index2-1] 
                else:   
                    dp[index1][index2] = min(dp[index1-1][index2-1], 
                                        dp[index1][index2-1],
                                        dp[index1-1][index2]) + 1

        return dp[N][M]

# space optimized
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)
        dp = [i for i in range(M+1)] 
        
        for index1 in range(1,N+1):
            temp = [float('inf') for i in range(M+1)] 
            temp[0] = index1
            for index2 in range(1,M+1):
                if word1[index1-1] == word2[index2-1]:
                    temp[index2] = dp[index2-1] 
                else:   
                    temp[index2] = min(dp[index2-1], 
                                        temp[index2-1],
                                        dp[index2]) + 1
            dp = temp.copy()
        return dp[M]