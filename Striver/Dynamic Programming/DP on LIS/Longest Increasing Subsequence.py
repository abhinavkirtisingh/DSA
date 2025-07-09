class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        N = len(nums)
        mx = max(nums)
        dp = [[None for i in range(N)] for j in range(N)]
        def fun(index,prev):
            
            if index == N:
                return 0
            if dp[index][prev] is not None:
                return dp[index][prev]
            temp = 0
            if prev == -1 or nums[index] > nums[prev] :
                temp = 1 + fun(index+1,index)
                
            dp[index][prev] = max(fun(index+1,prev), temp)
            return dp[index][prev]
        
        return fun(0,-1) 