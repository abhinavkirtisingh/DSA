class Solution:
    def upperBound(self, arr, target):
        #code 
        N = len(arr)
        low = 0 
        high = N - 1
        
        while low <= high:
            mid = (low + high)//2
            
            if arr[mid] <= target:
                low = mid + 1
                
            else:
                high = mid - 1
                
        return low