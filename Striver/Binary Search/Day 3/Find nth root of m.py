class Solution:
	def nthRoot(self, n: int, m: int) -> int:
		# Code here
		if n == 1:
		    return m
		low = 1
		high = m
		
		while low < high:
		    
		    mid = (low + high)//2
		    if (mid**n) <= m:
		        ans = mid
		        low = mid + 1
            else:
                high = mid
            
        return ans if (ans**n) == m else -1