arr=[]
size=int(input('Enter size of array: '))
for i in range(size):
    a=int(input().strip().split()[0])
    arr.append(a)


for i in range(size):
    min=i
    for j in range(i,size):
        if(arr[min]>arr[j]):
            min=j
    temp=arr[min]
    arr[min]=arr[i]
    arr[i]=temp
    print(arr)
print('Array sorted: ',arr)
