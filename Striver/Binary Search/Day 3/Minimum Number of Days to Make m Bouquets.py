class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        N = len(bloomDay)
        if m*k > N:
            return -1
        if m == 1 and k == 1:
            return min(bloomDay)
        def flower(d):
            count = 0
            c = 0
            for i in range(N):

                if bloomDay[i] <= d:
                    c+=1                    
                else:   
                    count += (c//k)                 
                    c = 0
            if  bloomDay[-1] <= d:
                  count += (c//k)
            
            return count

        low = min(bloomDay)
        high = max(bloomDay)

        while low <= high:
            mid = (low + high)//2
            x = flower(mid)

            if x >= m:
                high = mid - 1
            else:
                low = mid + 1
        print(low,mid,high)
        return low
                    
