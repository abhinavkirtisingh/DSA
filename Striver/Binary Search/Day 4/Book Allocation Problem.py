class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        N = len(arr)
        if k > N:
            return -1
        if k == N:
            return max(arr)
        
        def nchildren(pg):
            sm = 0
            child = 1
            
            for ele in arr:
                
                if sm + ele <=  pg:
                    sm += ele
                else:
                    sm = ele
                    child += 1
            return child
        
        low = max(arr)
        high = sum(arr)
        
        while low <= high:
            
            mid  = (low + high)//2
            x = nchildren(mid)
            if x > k:
                low = mid + 1
            else:
                high = mid - 1
        return low