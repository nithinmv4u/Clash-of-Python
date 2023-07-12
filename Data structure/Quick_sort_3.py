def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)
    
arr=[]
size=int(input('Enter size of array: '))
for i in range(size):
    a=int(input())
    arr.append(a)
quick_sort(arr)
print(arr)
