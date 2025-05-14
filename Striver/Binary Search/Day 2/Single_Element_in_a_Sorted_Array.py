class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[N-2] != nums[N-1]:
            return nums[-1]
        
        low = 1
        high = N - 2

        while low <= high:
            mid = (low + high)//2
            print(mid)
            if nums[mid-1] != nums[mid] and nums[mid+1] != nums[mid]:
                return nums[mid]
            elif (mid%2 == 0 and nums[mid-1] == nums[mid]) or (mid%2 and nums[mid+1] == nums[mid]):
                high = mid - 1
            else:
                low = mid + 1
        return -1