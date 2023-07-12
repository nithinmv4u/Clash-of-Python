class Array_add():
    def __init__(self,row,column):
        self.row=row
        self.column=column
    def getArray(self):
        arr=[]
        for i in range(self.row):
            col=[]
            for j in range(self.column):
                p=int(input())
                col.append(p)
            arr.append(col)
        return arr  

    def addArray(self,arr1,arr2):
        for i in range(self.row):
            for j in range(self.column):
                arr1[i][j]=arr1[i][j]+arr2[i][j]
        self.result=arr1

    def displayArray(self):
        print(self.result)

def main():
    row=int(input('Enter Row size: '))
    column=int(input('Enter column size: '))
    array=Array_add(row,column)
    print('Enter Array 1: ')
    arr1=array.getArray()
    print('Enter Array 2: ')
    arr2=array.getArray()
    array.addArray(arr1,arr2)
    array.displayArray()

main()