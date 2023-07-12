arr=[]
size=int(input('Enter size of array: '))
for i in range(size):
    a=int(input())
    arr.append(a)
for i in range(size-1):
    for j in range(size-1):
        if(arr[j]<arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
print('Array: ',arr)