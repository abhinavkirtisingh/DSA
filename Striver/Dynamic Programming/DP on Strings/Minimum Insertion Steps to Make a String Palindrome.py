# Optimized with LCS AND longest palindromic subsequence concept
class Solution:
    def minInsertions(self, s: str) -> int:
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

        return N - dp[M] #main logic
        


        