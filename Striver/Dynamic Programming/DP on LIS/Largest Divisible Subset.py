class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        N = len(nums)
        dp = [0 for i in range(N)]
        m = [i for i in range(N)]
        maxi = -1
        for i in range(N):

            for j in range(i-1,-1,-1):

                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    m[i] = j
            if maxi < dp[i]:
                maxi = dp[i]
                maxind = i
        ans = [nums[maxind]]
        while maxind != m[maxind]:
            maxind = m[maxind]
            ans.append(nums[maxind])
            
        return ans[::-1]