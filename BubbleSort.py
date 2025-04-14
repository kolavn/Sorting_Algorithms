#Time complexity - O(n2)
n=list(map(int,input("Enter the elements\n").split()))
def sort(n):
    for i in range(len(n)):
        for j in range(0,len(n)-1):
            if n[j]>n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
sort(n) 
print(n)
  
######################################## 2nd Version ######################### tc - O(n)

n=list(map(int,input("Enter the elements\n").split()))
def sort(n):
    for i in range(len(n)):
        didSwap = 0
        for j in range(0,len(n)-1):
            if n[j]>n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
                didSwap = 1
        if didSwap == 0:
            break;
        print("runs\n")
sort(n) 
print(n)