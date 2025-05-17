import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        N = len(piles)
        if N == h:
            return max(piles)
        
        def find(n):
            t = 0
            for ele in piles:
                t += math.ceil(ele/n)
            return t
        
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high)//2
             
            x = find(mid)

            if  x > h:
                low = mid + 1
            else:
                high = mid - 1
        
        return low