def multiply(a, multiplicant):
    a=int(a)
    return str(a) + " x " + str(multiplicant) + " = " + str(a*multiplicant)

def main():
    multiplicant = int(input("Enter the multiplicant: "))
    result = list(map(lambda x: multiply(x, multiplicant), input("Enter numbers: ").strip().split()))
    for i in range(len(result)):
        print(result[i])

main()