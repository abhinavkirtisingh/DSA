
arr = [12,345,1,4,234,4,2,42,21]


def algo(arr,low,mid,high):
    i = low
    j = mid+1
    res = []
    while i<=mid and j<=high:

        if arr[i] <= arr[j]:
            res.append(arr[i])
            i+=1
        else:
            res.append(arr[j])
            j+=1
    
    while i <= mid:
        res.append(arr[i])
        i+=1
    while j <= high:
        res.append(arr[j])
        j+=1
    for k in range(low,high+1):
        arr[k] = res[k-low]
    

def mergeSort(arr,low,high):
    
    if low < high:
        mid = (low+high)//2
        mergeSort(arr,low,mid)
        mergeSort(arr,mid+1,high)
        algo(arr,low,mid,high)
        
        
    

mergeSort(arr,0,len(arr)-1)
print(arr)




    