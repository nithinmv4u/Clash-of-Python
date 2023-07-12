def main():
    print('inside main')
    row=int(input('Enter size of rows: '))
    column=int(input('Enter size of columns: '))
    arr=[]
    array=getArray(arr,row,column)
    displayArray(array)

def getArray(arr,row,column):
    print('inside getarray\nEnter values:')
    for i in range(row):
        col=[]
        for j in range(column):
            p=int(input())
            col.append(p)
        arr.append(col)
        # print(arr)
    return arr

def displayArray(array):
    print('inside display array')
    print(array)

main()