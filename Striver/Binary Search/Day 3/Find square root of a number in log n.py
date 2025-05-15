class Solution:
    def mySqrt(self, x: int) -> int:
        if x in (0,1):
            return x
        

        low  = 1
        high = x
        
        
        while low < high :

            mid = (low + high)//2

            if (mid*mid) <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid
            
        return ans

print(5**3)
        