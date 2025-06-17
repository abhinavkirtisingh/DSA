#memmo
def fib(n,dp):
    print(dp)
    if n == 0 or n == 1:
        return n
    if n in dp:
        return dp[n]
    dp[n] = fib(n-1,dp) + fib(n-2,dp)
    return dp[n]

dp = {}
print(fib(10,dp))

#tabulation
def fibTab(n):
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

print(fibTab(10))