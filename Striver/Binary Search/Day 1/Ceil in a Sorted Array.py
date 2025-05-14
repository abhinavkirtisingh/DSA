class Solution:
    def findCeil(self, arr, x):
        # code here
        N = len(arr)
        low = 0
        high = N - 1
        ans = -1
        while low <= high:
            mid = (low + high)//2
            
            if arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
                ans = mid
        return ans