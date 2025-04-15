n=list(map(int,input("Enter the elements\n").split()))
def insertionSort(n):
    for i in range(len(n)): # loop for every element as we are increasing arrary size
        j = i
        while(j>0 and n[j-1]>n[j]): # checking from reverse till the first element
                temp = n[j-1]
                n[j-1] = n[j]
                n[j] = temp
                j-=1
insertionSort(n)
print(n)