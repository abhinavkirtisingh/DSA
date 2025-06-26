
# https://www.geeksforgeeks.org/problems/longest-common-substring1452/1
class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        N = len(s1)
        M = len(s2)
        dp = [[0 for i in range(M+1)] for j in range(N+1)]
        ans = float('-inf')
        for i in range(1,N+1):
            for j in range(1,M+1):
                
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                ans = max(ans,dp[i][j])
        
        return ans
# space optimized

class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        N = len(s1)
        M = len(s2)
        prev = [0 for i in range(M+1)]
        
        ans = float('-inf')
        for i in range(1,N+1):
            cur = [0 for i in range(M+1)]
            for j in range(1,M+1):
                
                if s1[i-1] == s2[j-1]:
                    cur[j] = 1 + prev[j-1]
                
                ans = max(ans,cur[j])
            prev = cur.copy()
            
        
        return ans