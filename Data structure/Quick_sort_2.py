def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    left = []
    right = []
    for item in arr:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return quick_sort(left) + [pivot] + quick_sort(right)

arr=[]
size=int(input('Enter size of array: '))
for i in range(size):
    a=int(input())
    arr.append(a)
quick_sort(arr)
print(arr)