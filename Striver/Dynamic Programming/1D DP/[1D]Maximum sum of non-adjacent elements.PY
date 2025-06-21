
# https://leetcode.com/problems/house-robber/description/

#memorization
class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)
        dp = [None] * N
        def fun(index):
            if index >= N:
                return 0
            if dp[index] is not None:
                return dp[index]
            dp[index] = max(nums[index] + fun(index+2), fun(index+1))
            return dp[index]
        
        return fun(0)

#tabulation 
class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)
        if N < 3:
            return max(nums)
        dp = [0] * N
        dp[0],dp[1] = nums[0], max(nums[0],nums[1])

        for i in range(2,N):
            dp[i] = max(nums[i] + dp[i-2],dp[i-1])
        return dp[-1]
    

#space optimmized
class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)
        if N < 3:
            return max(nums)
        
        p1,p2 = nums[0], max(nums[0],nums[1])

        for i in range(2,N):
            cur = max(nums[i] + p1,p2)
            p1 = p2
            p2 = cur
        return cur
        