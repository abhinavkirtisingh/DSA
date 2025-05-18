class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        low = 0
        high = n-1
        
        while low <= high:
            mid = (low + high)//2
            x = arr[mid] - (mid+1)
            if x < k:
                low = mid + 1
            else:
                high = mid - 1
        
        return high + k + 1