def hourglassSum(arr):
    max_sum = None
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            current_sum = sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3])
            if max_sum is None or current_sum>max_sum:
                max_sum = current_sum
    return max_sum

def main():
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().strip().split())))

    print(len(arr))
    print(arr)

    result = hourglassSum(arr)
    print(result)

main()