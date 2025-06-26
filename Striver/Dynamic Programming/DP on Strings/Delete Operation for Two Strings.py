#https://leetcode.com/problems/delete-operation-for-two-strings/description/
# Tabulation
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):

                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        n1 = max(n,m) - dp[n][m]
        n2 = min(n,m) - dp[n][m]
        return n1 + n2
#space optimized 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        prev = [0 for i in range(m+1)]
        cur = [0 for x in range(m+1)]

        for i in range(1,n+1):
            
            for j in range(1,m+1):

                if word1[i-1] == word2[j-1]:
                    cur[j] = 1 + prev[j-1]
                else:
                    cur[j] = max(prev[j],cur[j-1])
            prev = cur.copy()
            cur = [0 for x in range(m+1)]
        n1 = max(n,m) - prev[m]
        n2 = min(n,m) - prev[m]
        return n1 + n2
        