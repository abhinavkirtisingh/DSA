def frogJump(heights, k):

    N = len(heights)
    dp = {}
    def fun(index):

        if index <= 0:
            return 0
        if index in dp:
            return dp[index]
        ans = float('inf')
        for j in range(1,k+1):
            if index-j >= 0:
                ans = min(ans, abs(heights[index-j] - heights[index]) + fun(index-j))
        dp[index] = ans
        return dp[index] 

    
    return fun(N-1)