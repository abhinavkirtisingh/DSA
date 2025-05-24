class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)
        
        low = 0
        high = n1

        while low <= high:
            mid1 = (low+high)//2
            mid2 = ((n1+n2+1)//2) - mid1
            print(mid2)
            l1 = nums1[mid1-1] if mid1 - 1 >= 0 else float("-inf")
            l2 = nums2[mid2-1] if mid2 - 1 >= 0 else float("-inf")
            h1 = nums1[mid1] if mid1 < n1 else float('inf')
            h2 = nums2[mid2] if mid2 < n2 else float('inf')

            if l1 <= h2 and l2 <= h1:
                if (n1+n2)%2 == 0:
                    return (max(l1,l2) + min(h1,h2))/2
                else:
                    return max(l1,l2)
            elif l1 > h2:
                high = mid1 - 1
            else:
                low = mid1 + 1