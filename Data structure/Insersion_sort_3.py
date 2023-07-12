def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr=[]
size=int(input('Enter size of array: '))
for i in range(size):
    a=int(input())
    arr.append(a)
insertion_sort(arr)
print(arr)