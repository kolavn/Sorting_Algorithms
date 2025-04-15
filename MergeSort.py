n = list(map(int,input("Enter the list of nums\n").split()))
def mergeSort(n, low, high):
    if low>=high: #division of array till the last bifuracation
        return
    mid = (low+high)//2
    mergeSort(n, low, mid)
    mergeSort(n,mid+1, high)
    merge(n,low,mid,high)#left lists and right lists

def merge(n, low, mid, high):
    final = []
    left = low
    right = mid+1
    while left<=mid and right<=high:
        if n[left]<=n[right]:
            final.append(n[left])          
            left+=1
        else:
            final.append(n[right])
            right+=1
    while left <= mid:
        final.append(n[left])
        left+=1
    while right<=high:
        final.append(n[right])
        right+=1
    for i in range(len(final)):
        n[low+i]= final[i]


mergeSort(n,0, len(n)-1)
print("Sorted list:\n", n)