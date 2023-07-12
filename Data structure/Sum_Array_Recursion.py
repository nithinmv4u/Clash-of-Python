def sum_array(arr, i = 0):
        
        if(i>=len(arr)):
              print("zero")
              return 0
        else:
              print("add")
              return arr[i] + sum_array(arr, i+1)

def main():
    arr = list(map(int, input("Enter numbers: ").strip().split()))
    # sum = sum_array(arr)
    print(sum_array(arr))

main()