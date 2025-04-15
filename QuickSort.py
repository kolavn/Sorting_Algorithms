arr = list(map(int,input("Enter the list to sort\n").split()))

def QuickSort(arr, low, high):
    if low < high:
        #to place pivot in its correct place
        #to tell where pivot is, for that I'm calling function
        partition_index = wherePivot(arr, low, high)
        QuickSort(arr,low, partition_index-1)
        QuickSort(arr, partition_index+1, high)

        
def wherePivot(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        #finding element greater than pivot, and moving i to next index
        while (i<=j and arr[i]<=pivot): 
            i+=1
        #finding element less than pivot, and moving j to next index
        while (i<=j and arr[j]>=pivot):
            j-=1
        #if they dont cross each other, swap
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low],arr[j] = arr[j], arr[low]
    return j
        
QuickSort(arr, 0, len(arr)-1)
print("Sorted List:\n",arr)     

#Best Case	O(n log n), Average Case O(n log n), Worst Case	O(n²)