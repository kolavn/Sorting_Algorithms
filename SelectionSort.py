nums = list(map(int, input("Enter the numbers to sort\n").split()))
def sort(nums):
    for i in range(0, len(nums)-1): #for loop to run
        mini = i # lets assume first element is minimum
        for j in range(i+1, len(nums)): ## for sorting inner elements
            if nums[j] < nums[mini]:
                mini = j
        temp = nums[mini]
        nums[mini] = nums[i]
        nums[i] = temp
sort(nums)
print(nums)
