# https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1
#User function Template for python3
class Solution:
	def minDifference(self, arr):
		# code here
		N = len(arr)
		sm = sum(arr)
        dp = [[False for j in range(sm+1)] for i in range(N)]
        for i in range(N):
            dp[i][0] = True
        
        if arr[0] <= sm:
            dp[0][arr[0]] = True 
	#memorization for reference
        # def fun(index,target):
        #     if target == 0:
        #         return True
        #     if index == 0:
        #         return arr[0] == target
        #     if dp[index][target] is not None:
        #         return dp[index][target]
            
        #     nottake = fun(index-1,target)
        #     take = False
        #     if arr[index] <= target:
        #         take = fun(index-1,target-arr[index])
        #     dp[index][target] = take or nottake
        #     return dp[index][target]
        
        for index in range(1,N):
            for target in range(sm+1):
                nottake = dp[index-1][target]
                take = False
                if arr[index] <= target:
                    take = dp[index-1][target-arr[index]]
                dp[index][target] = take or nottake
                
        
        ans = float('inf')
        for t in range(sm+1):
            if dp[N-1][t]:
                ans = min(abs(t - (sm-t)),ans)
        return ans