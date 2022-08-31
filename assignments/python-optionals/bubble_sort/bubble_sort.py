arr = [1,2,3,4,5,6,7,8]

def bubbleSort(arr):
    count = 0
    for j in range(len(arr)-1):
        for i in range(0,len(arr)-1-j):
            # print("\n","*"*80,"\nindex",i,"value",arr[i])
            # print("comparing",arr[i],arr[i+1])
            count+=1
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                # print("swapp",arr[i],arr[i+1])
            # else:
                # print("no need to swap",arr[i],arr[i+1])
                
    print("# iteration:", count)
    return arr


print(bubbleSort(arr))
