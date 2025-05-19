class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        if N == k or N == 1:
            return max(nums)
        

        def max_sum(s):
            tsm = 0
            count = 1
            for ele in nums:
                if tsm + ele <= s:
                    tsm += ele
                else:
                    count += 1
                    tsm = ele
            return count
        low = max(nums)  
        high =  sum(nums)+1      
        
        while low <= high:

            mid = (low + high)//2
            x= max_sum(mid)

            if x <= k:
                high = mid - 1
            else:
                low = mid + 1
        
        
        return low