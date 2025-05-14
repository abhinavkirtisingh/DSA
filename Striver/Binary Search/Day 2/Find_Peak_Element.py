class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1 or nums[0] > nums[1]:
            return 0
        if nums[N-1] > nums[N-2]:
            return N-1
        
        low =  1
        high = N - 2
        
        while low <= high:
            mid = (low + high)//2
            print(mid)
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] < nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid - 1
        return -1