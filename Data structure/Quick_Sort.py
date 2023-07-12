def Partition(arr, start, end):
    pivot = arr[end]
    # print(arr)
    pIndex = start
    for i in range(start,end):
        # print("arr[i]: ",arr[i], "pivot", pivot)
        if arr[i]<pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex+=1
            # print(arr)
    # print(pIndex)
    arr[pIndex], arr[end] = arr[end], arr[pIndex]
    return pIndex

def quickSort(arr, start, end):
    # print("start: ",start, "end: ",end)
    if start < end:
        pIndex = Partition(arr, start, end)
        print("arr: ", arr, "Pindex: ", pIndex)
        quickSort(arr, start, pIndex-1)
        quickSort(arr, pIndex+1, end)

def main():
    arr = list(map(int, input("Enter Array: ").strip().split()))
    # print(arr[:2])
    quickSort(arr, 0, len(arr)-1)
    print(arr)


main()