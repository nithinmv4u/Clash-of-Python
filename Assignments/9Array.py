arr=[]
length=int(input('Enter the size of Array 1: '))
print('Enter the values of Array 1:')
for i in range(length):
    x=int(input())
    arr.append(x)
arr2=arr.copy()
print('Array2:',end=' ')
for i in range(length):
    print(arr2[i],end=' ')
while True:
    option=int(input("\nDo you need to add element?\n1.yes\n2.No\nChoose option:"))
    if(option==1):
        x=int(input())
        arr2.append(x)
    elif(option==2):
        break
    else:print('Invalid Entry!')
print('Array1: ',arr)
print('Array2: ',arr2)