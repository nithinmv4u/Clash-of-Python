def rotateLeft(d, arr):
    # for i in range(d):
    #     a = arr[0]
    #     for j in range(len(arr)-1):
    #         arr[j] = arr[j+1]
    #     arr[j+1] = a
    arr = arr[d:] + arr[:d]
    return arr

def main():
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    print(result)

main()