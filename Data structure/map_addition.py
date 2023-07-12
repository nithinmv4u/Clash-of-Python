#adds each element to itself by converting string of elements to integer by spliting

def sum(number):
    print(number)
    number=int(number)
    number+=number
    print("result: ",number)
    return number

def main():
    result = list(map(sum, input("Enter numbers: ").strip().split()))
    for i in range(len(result)):
        print(result[i])

main()