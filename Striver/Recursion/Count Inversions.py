class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, nums):
        # Your Code Here
        res = 0
        def algo(arr,low,mid,high):
            l = low
            r = mid+1
            nonlocal res
            temp = []
            while l <=mid and r <= high:
        
                if arr[l] <= arr[r]:
                    temp.append(arr[l])
                    l+=1
                else:
                    res += ( mid - l + 1)
                    temp.append(arr[r])
                    r+=1
                    
            
            while l <= mid:
                temp.append(arr[l])
                l+=1
            while r <= high:
                temp.append(arr[r])
                r += 1
            
            for i in range(low, high+1):
                arr[i] = temp[i-low]
            
        def mergeSort(arr,low,high):
        
            if low < high:
                mid = (low + high)//2
                mergeSort(arr,low,mid)
                mergeSort(arr,mid+1,high)
                algo(arr,low, mid, high)
        mergeSort(nums,0,len(nums)-1)
        return res