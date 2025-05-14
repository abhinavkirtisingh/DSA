class Solution:
    def lowerBound(self, arr, target):
        #code here
        l = 0
        h = len(arr) - 1
        ans = len(arr)
        while l <= h:
            mid = (l + h)//2
            
            if arr[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
                
        
        return l