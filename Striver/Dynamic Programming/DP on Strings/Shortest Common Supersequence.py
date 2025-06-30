# get the lcs dp
# start from n,m and whenever their is a match move diagonally and include the element once
# else move go to the max(dp[i][j-1],dp[i-1][j]), If dp[i-1][j] > dp[i][j-1] then add string[i] in answer and move up. Do same in case of dp[i][j-1] > dp[i-1][j]
# https://leetcode.com/problems/shortest-common-supersequence/
#changes

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        N = len(str1)
        M = len(str2)

        dp = [[0 for i in range(M+1)] for j in range(N+1)]

        for i in range(1,N+1):
            for j in range(1, M+1):

                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        i = N
        j = M
        st = ''
        while i > 0 and j > 0:

            if str1[i-1] == str2[j-1]:
                st += str1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j] > dp[i][j-1]:
                st += str1[i-1]
                i-=1
            else:
                st += str2[j-1]
                j-=1
        
        if i > 0:
            st += str1[i-1::-1]
        if j > 0:
            st += str2[j-1::-1]
        return st[::-1]