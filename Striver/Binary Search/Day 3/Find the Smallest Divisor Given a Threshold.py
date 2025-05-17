class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:


        N = len(nums)
        
        if N == threshold:
            return max(nums)
        if sum(nums)<=threshold:
            return 1
        def div_sum(n):
            ans = 0
            for ele in nums:
                ans += math.ceil(ele/n)
            return ans
        
        low = 1
        high = max(nums)

        while low <= high:
            mid = (low + high)//2
            x = div_sum(mid)
            if x > threshold:
                low = mid + 1
            else:
                high = mid - 1    
          
        return low