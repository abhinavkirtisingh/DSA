# Memorization
# https://leetcode.com/problems/longest-increasing-subsequence/
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

# Tabulation
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        N = len(nums)
        mx = max(nums)
        dp = [[0 for i in range(N+1)] for j in range(N+2)]
        
        for index in range(N,-1,-1):
            for prev in range(index-1,-1,-1):
                temp = 0
                if prev == 0 or nums[index-1] > nums[prev-1]:
                    temp = 1 + dp[index+1][index]
                    
                dp[index][prev] = max(dp[index+1][prev], temp)
        # print(dp)
        return dp[1][0]


# Binary search and best complexity approach

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def lowerB(arr,target):
            low = 0
            high = len(arr)-1
            
            while low <= high:
                
                mid = (low + high)//2
                
                if arr[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low
        
        ans = [nums[0]]

        for i in range(1,len(nums)):
            
            if nums[i] <= ans[-1]:
                index = lowerB(ans,nums[i])
                ans[index] = nums[i]
            else:
                ans.append(nums[i])
        return len(ans)



        