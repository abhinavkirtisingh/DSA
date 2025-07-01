class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        N = len(s)
        M = len(p)
        dp = [[None for i in range(M)] for j in range(N)]
        def f(index1,index2) -> bool:

            if index1 < 0 or index2 <0:
                if index1 < 0 and (index2 <0):                
                    return True
                if index2 >= 0 and p[index2] == '*' and index1 < 0:
                    return f(index1,index2-1)
                return False
            if dp[index1][index2] is not None:
                return dp[index1][index2] 
            if p[index2] == '?' or p[index2] == s[index1]:
                dp[index1][index2] = f(index1-1,index2-1)
                return dp[index1][index2] 
            if p[index2] == '*':
                dp[index1][index2] = f(index1,index2-1) or f(index1-1,index2) 
                return dp[index1][index2] 
            
            return False
        return f(N-1,M-1)