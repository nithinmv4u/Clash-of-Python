arr=[]
size=int(input('Enter size of array: '))
for i in range(size):
    a=int(input())
    arr.append(a)
for i in range(1,size):
    temp=arr[i]
    j=i-1
    while(j>=0 and arr[j]>temp):
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=temp
print(arr)