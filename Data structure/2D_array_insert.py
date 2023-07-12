def main():
    arr =[[1,2,3,4],[9,5,3,7],[5,3,7,5]]
    print(arr)
    arr.insert(2,[1,2,3,5])
    print(arr)
    arr[2].insert(2,8)
    print(arr)
    del arr[3]
    print(arr)
    del arr[2][1]
    print(arr)

main()