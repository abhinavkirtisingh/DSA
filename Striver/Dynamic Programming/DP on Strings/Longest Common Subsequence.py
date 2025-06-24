# https://leetcode.com/problems/longest-common-subsequence/submissions/1674400263/
# Memorization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        N = len(text1)
        M = len(text2)
        dp = [[None for i in range(M+1)] for j in range(N+1)]
        def fun(index1,index2):
            if index1 < 0 or index2 <0:
                return 0
            if dp[index1][index2] is not None:
                return dp[index1][index2]
            if text1[index1] == text2[index2]:
                return 1 + fun(index1-1,index2-1)
            dp[index1][index2] = max(fun(index1-1,index2), fun(index1,index2-1))
            return dp[index1][index2]
            
        
        return fun(N-1,M-1)


#tabulation
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        N = len(text1)
        M = len(text2)
        dp = [[0 for i in range(M+1)] for j in range(N+1)]
                    
        for index1 in range(1,N+1):
            for index2 in range(1,M+1):
                if text1[index1-1] == text2[index2-1]:
                    dp[index1][index2] =  1 + dp[index1-1][index2-1]
                else:
                    dp[index1][index2] = max(dp[index1-1][index2], dp[index1][index2-1])

        return dp[N][M]

#space optimized
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        N = len(text1)
        M = len(text2)
        dp = [0 for i in range(M+1)] 
        temp = [0 for i in range(M+1)] 
        
        for index1 in range(1,N+1):
            for index2 in range(1,M+1):
                if text1[index1-1] == text2[index2-1]:
                    temp[index2] = 1 + dp[index2-1]

                else:
                    temp[index2] = max(temp[index2-1],dp[index2])
            dp = temp.copy() 
            temp = [0 for i in range(M+1)]

        return dp[M]


            
        


            
        
