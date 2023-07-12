def merge(left, right, arr):
    l,r,i =0,0,0
    print("L: ",left)
    print("R: ",right)
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            arr[i]=left[l]
            i+=1
            l+=1
        else:
            arr[i]=right[r]
            i+=1
            r+=1

    while l<len(left):
        arr[i] = left[l]
        i+=1
        l+=1
    while r<len(right):
        arr[i] = right[r]
        i+=1
        r+=1

    print("Array: ",arr)

def mergeSort(arr):
    if len(arr)<2:return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    print("Left: ",left)
    print("Right: ",right)
    mergeSort(left) 
    mergeSort(right)
    arr = merge(left, right, arr)
    

def main():
    arr = list(map(int, input("Enter Array: ").strip().split()))
    # print(arr[:2])
    mergeSort(arr)
    print(arr)


main()