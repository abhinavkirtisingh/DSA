class Solution:
    def findKRotation(self, arr):
        # code here
        N = len(arr)
        low = 0
        high = N - 1
        
        while low < high:
            mid = (low + high)//2
            
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid 
        
        return low