def sum_numbers(*args):
    result=0
    li=list(*args)
    for val in li:
        result+=val
    return result

def main():
    numbers=[]
    while True:
        choice=int(input('Enter choice:\n1.Add values\n2.sum of values\n'))
        if(choice==1):
            x=float(input('Enter value: '))
            numbers.append(x)
            print('Numbers are: ',numbers)
        elif(choice==2):
            sum=sum_numbers(numbers)
            print(sum)
        else:print('Invalid Entry !')
main()