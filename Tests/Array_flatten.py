def flaten(flatened_arr, arr):
    print(len(arr))

    for element in arr:
        if isinstance(element, int):
            flatened_arr.append(element)
        else:
            flaten(flatened_arr, element)
    return flatened_arr

arr = [1, 2, 3, [4, 5, [[6]]]]
flatened_arr=[]

print(flaten(flatened_arr, arr))

