# https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1
# memorization
class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        dp = [[None for i in range(capacity+1)] for j in range(len(wt))]
        def fun(index,target):
            if index < 0 or target == 0:
                return 0
            if dp[index][target] is not None:
                return dp[index][target]
            nottake = fun(index-1,target)
            take = 0
            if wt[index] <= target:
                take = val[index] + fun(index,target - wt[index])
            dp[index][target] = max(nottake,take)
            return dp[index][target]
        
        return fun(len(wt)-1,capacity)
        
# TABULATION

class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        N = len(wt)
        dp = [[0 for i in range(capacity+1)] for j in range(N)]
        
        for w in range(capacity+1):
            dp[0][w] = (w//wt[0]) * val[0]
        
        for index in range(1,N):
            for target in range(capacity+1):
                nottake = dp[index-1][target]
                take = 0
                if wt[index] <= target:
                    take = val[index] + dp[index][target - wt[index]]
                dp[index][target] = max(nottake,take)
        
        return dp[N-1][capacity]

#SPACE OPTIMIZED

class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        N = len(wt)
        dp = [0 for i in range(capacity+1)]
        
        for w in range(capacity+1):
            dp[w] = (w//wt[0]) * val[0]
        
        for index in range(1,N):
            for target in range(capacity+1):
                nottake = dp[target]
                take = 0
                if wt[index] <= target:
                    take = val[index] + dp[target - wt[index]]
                dp[target] = max(nottake,take)
        
        return dp[capacity]