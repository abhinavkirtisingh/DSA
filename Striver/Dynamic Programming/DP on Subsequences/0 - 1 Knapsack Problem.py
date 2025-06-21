# https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
#memorization
class Solution:
    def knapsack(self, W, val, wt):
        # code here
        
        N = len(val)
        dp = [[None for i in range(W+1)] for j in range(N)]
        def fun(index,weight):
            
            if index == N or weight <= 0:
                return 0
            if wt[index] > weight:
                return fun(index+1,weight)
            if dp[index][weight] is not None:
                return dp[index][weight]
            dp[index][weight] = max(val[index] + fun(index+1,weight - wt[index]),fun(index+1,weight))
            return dp[index][weight]
        
        return fun(0,W)

#tabulation
class Solution:
    def knapsack(self, W, val, wt):
        # code here
        
        N = len(val)
        dp = [[0 for i in range(W+1)] for j in range(N)]
        
        for w in range(wt[0],W+1):
            dp[0][w] = val[0]
        
        for ind in range(1, N):
            for weight in range(0,W+1):
                
                nottake = dp[ind-1][weight]
                take = float('-inf')
                if wt[ind] <= weight:
                    take = val[ind] + dp[ind-1][weight - wt[ind]]
                dp[ind][weight] = max(take,nottake)
        
        return dp[N-1][W]

#space optimized 

class Solution:
    def knapsack(self, W, val, wt):
        # code here
        
        N = len(val)
        prev = [0 for i in range(W+1)]
        
        for w in range(wt[0],W+1):
            prev[w] = val[0]
        
        for ind in range(1, N):
            for weight in range(W,-1,-1):
                
                nottake = prev[weight]
                take = float('-inf')
                if wt[ind] <= weight:
                    take = val[ind] + prev[weight - wt[ind]]
                prev[weight] = max(take,nottake)
        
        return prev[W]
        
            
            
        
