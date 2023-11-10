def main():
    # arr=input('Enter numbers:').strip().split()
    # print(arr)
    arr = []

    for _ in range(3):
        arr.append(list(map(int, input().strip().split())))
    
    print(len(arr))
    print(arr)
    total_sum = sum([num for sublist in arr for num in sublist])
    new_list = [num for x in arr for num in x]
    print(new_list)
    print(total_sum)

main()