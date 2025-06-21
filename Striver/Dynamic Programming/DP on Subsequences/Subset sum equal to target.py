#https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
# Memorization

class Solution:
    def isSubsetSum (self, arr, target):
        # code here 
        N = len(arr)
       
        dp = [[None for i in range(target+1)] for j in range(N)]
        
        def fun(index,sm):
            if sm > target:
                return False
            if index == N:
                return sm == target
            if dp[index][sm] is not None:
                return dp[index][sm]
            
            dp[index][sm] = fun(index + 1,sm+arr[index]) or fun(index+1,sm)
            
            return dp[index][sm]
        
        return fun(0,0)

# Tabulation
class Solution:
    def isSubsetSum (self, arr, target):
        # code here 
        N = len(arr)
       
        dp = [[False if i > 0 else True for i in range(target+1)] for j in range(N)]
        
        if arr[0] <= target:
            dp[0][arr[0]] = True
        
        for i in range(1,N):
            for t in range(1,target+1):
                nottake = dp[i-1][t]
                take = False
                
                if arr[i] <= t:
                    take = dp[i-1][t - arr[i]]
                
                dp[i][t] = nottake or take
        return dp[N-1][target]

#Space Optimized
class Solution:
    def isSubsetSum (self, arr, target):
        # code here 
        N = len(arr)
       
        prev = [False if i > 0 else True for i in range(target+1)]
        cur = [False if i > 0 else True for i in range(target+1)]
        if arr[0] <= target:
            prev[arr[0]] = True
        
        for i in range(1,N):
            for t in range(1,target+1):
                nottake = prev[t]
                take = False
                
                if arr[i] <= t:
                    take = prev[t - arr[i]]
                
                cur[t] = nottake or take
            prev = cur.copy()
            cur = [False if i > 0 else True for i in range(target+1)]
        return prev[target]