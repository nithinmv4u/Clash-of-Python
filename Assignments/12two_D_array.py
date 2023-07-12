def scan(arr):
    for i in range(row):
        col=[]
        for j in range(column):
            p=int(input())
            col.append(p)
        arr.append(col)
        # print(arr)
    return arr
row=int(input('Enter Row size: '))
column=int(input('Enter column size: '))
arr=[]
print('Enter Array 1: ')
arr1=scan(arr)
print(arr1)
arr=[]
print('Enter Array 2: ')
arr2=scan(arr)
print(arr1)
print(arr2)
# print(arr1+arr2)
for i in range(row):
    for j in range(column):
        arr1[i][j]=arr1[i][j]+arr2[i][j]
print(arr1)
