class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        def first():
            low = 0
            high = N - 1
            ans = -1
            while low <=high:
                mid = (low + high)//2

                if nums[mid] >= target:
                    high = mid - 1
                    if nums[mid] == target:
                        ans = mid
                else:
                    low = mid + 1
            return ans 


        def last():
            low = 0
            high = N - 1
            ans = -1
            while low <= high:
                mid = (low + high)//2

                if nums[mid] <= target:
                    low = mid + 1 
                    if nums[mid] == target:
                        ans = mid
                else:
                    high = mid - 1
                    
            return ans
        return [first(),last()]
            
        