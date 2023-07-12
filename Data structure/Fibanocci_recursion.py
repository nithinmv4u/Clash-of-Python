def fibanocci(n,s=0):
    if n>=0:
        s+=s+1
        fibanocci(n-1,s)
    else:
        return 0
    # s = fibanocci(n,s) + fibanocci(n,s+1)
    print(s)

if __name__ == '__main__':
    n = int(input("Enter the limit of series: ").strip().split()[0])
    fibanocci(n,0)

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# def print_fibonacci_sequence(n):
#     for i in range(n):
#         print(fibonacci(i))

# print_fibonacci_sequence(10)
