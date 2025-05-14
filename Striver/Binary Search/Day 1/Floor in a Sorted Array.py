def findFloor(self, arr, x):
        #Your code here
        n = len(arr)
        low = 0 
        high = n - 1
        ans = -1
        while low <= high:
            mid = (low + high)//2
            
            if arr[mid] > x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
        return ans