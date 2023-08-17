def partition(arr,low,high):
    pivot = arr[low]
    i =low+1
    for j in range(low+1,high+1):
        if (arr[j]<pivot):
            arr[i],arr[j] = arr[j],arr[i]
            i=i+1
    pivot_index = i-1
    arr[pivot_index],arr[low] = arr[low],arr[pivot_index]
    return pivot_index

def quick_sort(arr,low,high):
    if low<high:
        pivot = partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)

arr = [4,3,5,6,2,7,9,3]
quick_sort(arr,0,len(arr)-1)
print(arr)