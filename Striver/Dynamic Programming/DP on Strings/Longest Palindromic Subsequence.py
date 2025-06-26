# https://leetcode.com/problems/longest-palindromic-subsequence/
# memorization
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        N = len(s)
        dp = [[None for i in range(N)] for j in range(N)]
        def fun(index1,index2):
            if index1 == N or index2 < 0:
                return 0
            if dp[index1][index2] is not None:
                return dp[index1][index2]
            if s[index1] == s[index2]:
                dp[index1][index2] = 1 + fun(index1+1,index2-1)
                return dp[index1][index2]
            dp[index1][index2] = max(fun(index1+1,index2), fun(index1,index2-1))
            return dp[index1][index2]
        
        return fun(0,N-1)

# tabulation:
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        N = len(s)
        dp = [[0 for i in range(N+2)] for j in range(N+2)]
        def fun(index1,index2):
            if index1 == N or index2 < 0:
                return 0
            if dp[index1][index2] is not None:
                return dp[index1][index2]
            if s[index1] == s[index2]:
                dp[index1][index2] = 1 + fun(index1+1,index2-1)
                return dp[index1][index2]
            dp[index1][index2] = max(fun(index1+1,index2), fun(index1,index2-1))
            return dp[index1][index2]
        ans = float('-inf')
        for index1 in range(N-1,-1,-1):
            for index2 in range(N):
                if s[index1] == s[index2]:
                    dp[index1][index2] = 1 + dp[index1+1][index2-1]
                else:
                    dp[index1][index2] = max(dp[index1+1][index2], dp[index1][index2-1])
                ans = max(ans, dp[index1][index2])
        
        return ans

# space optimized using lcs 

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        N = len(s)
        M = len(s)
        dp = [0 for i in range(M+1)] 
        temp = [0 for i in range(M+1)] 
        text2 = s[::-1]
        for index1 in range(1,N+1):
            for index2 in range(1,M+1):
                if s[index1-1] == text2[index2-1]:
                    temp[index2] = 1 + dp[index2-1]

                else:
                    temp[index2] = max(temp[index2-1],dp[index2])
            dp = temp.copy() 
            temp = [0 for i in range(M+1)]

        return dp[M]
        
        