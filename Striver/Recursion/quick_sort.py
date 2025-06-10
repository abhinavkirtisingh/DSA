
arr = [4,6,2,5,7,9,1,3]


def algo(arr,low,high):
    pivot = arr[low]

    i = low
    j = high

    while i < j:

        while i <= high and arr[i] <= pivot:
            i+=1
        while j >= low and arr[j] > pivot:
            j-=1
        if i < j:
            arr[i],arr[j] = arr[j], arr[i]
    arr[j], arr[low] = arr[low], arr[j]
    return j

def bSearch(arr,low,high):
    if low < high:
        partition = algo(arr,low,high)
        bSearch(arr,low,partition)
        bSearch(arr,partition+1,high)

bSearch(arr,0,len(arr)-1)
print(arr)