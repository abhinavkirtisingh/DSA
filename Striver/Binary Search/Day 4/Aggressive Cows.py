class Solution:

    def aggressiveCows(self, stalls, k):
        # your code here
        
        d = 1
        N = len(stalls)
        stalls.sort()
        def placingCows(d):
            count = 0 
            prev = -10**8
            
            for ele in stalls:
                if ele - prev >= d:
                    count += 1
                    prev = ele
            return count
        
        low = 1
        high = stalls[-1] - stalls[0] + 1
        
        while low <= high:
            
            mid = (low + high)//2
            c = placingCows(mid)
            
            if c >= k:
                
                low = mid + 1
            else:
                high = mid - 1
       
        return high