class Solution:

    def kthElement(self, a, b, k):
        
        n1 = len(a)
        n2 = len(b)
        
        if n2 < n1:
            return self.kthElement(b,a,k)
        
        low  = max(0,k-n2)
        high = min(k,n1)
        
        while low <= high:
            
            mid1 = (low + high)//2
            
            mid2 = k - mid1
            
            l1 = a[mid1-1] if mid1-1 >= 0 else float("-inf")
            l2 = b[mid2-1] if mid2-1 >= 0 else float("-inf")
            h1 = a[mid1] if mid1 < n1 else float("inf")
            h2 = b[mid2] if mid2 < n2 else float("inf")
            
            if l1 <= h2 and l2 <= h1:
                return max(l1,l2)
            
            if l2 > h1:
                low = mid1 + 1
            else:
                high = mid1 - 1               