def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr=[]
size=int(input('Enter size of array: '))
for i in range(size):
    a=int(input())
    arr.append(a)
selection_sort(arr)
print(arr)