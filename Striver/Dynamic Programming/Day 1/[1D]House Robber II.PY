class Solution:
    def rob(self, nums: List[int]) -> int:        
        N = len(nums)
        if N <= 3:
            return max(nums)
        dp1 = [None] * N
        dp2 = [None] * N
        def fun1(index):
            if index == N-2:
                return nums[-2]
            if index >= N-1:
                return 0
            if dp1[index] is not None:
                return dp1[index]
            dp1[index] = max(nums[index] + fun1(index+2),fun1(index+1))            
            return dp1[index]
        def fun2(index):
            if index == N-1:
                return nums[-1]
            if index >= N:
                return 0
            if dp2[index] is not None:
                return dp2[index]
            dp2[index] = max(nums[index] + fun2(index+2),fun2(index+1))            
            return dp2[index]
        
        return max(fun1(0),fun2(1))
        