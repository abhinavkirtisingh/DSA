class Solution:
    def countFreq(self, arr, target):
        #code here
        
        N = len(arr)
        
        def last():
            low = 0
            high = N - 1
            ans = -1
            while low <= high:
                mid = (low + high)//2
                
                if arr[mid] <= target:
                    low = mid + 1
                    if arr[mid] == target:
                        ans = mid
                else:
                    high = mid - 1
            return ans
        
        def first():
            low = 0 
            high =  N - 1
            ans = -1
            while low <= high:
                mid = (low+high)//2
                
                if arr[mid] >= target:
                    high = mid - 1
                    if arr[mid] == target:
                        ans = mid
                else:
                    low = mid + 1
            return ans
        
        f = first()
        l = last()
        
        if [-1,-1] == [f,l]:
            return 0
        
        return l - f + 1