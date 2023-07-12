class OneError(Exception):
    def __init__(self,num):
        print("Exception")
        self.num=num

def main():
    while True:
        number=int(input('Enter a Number'))
        try:
            if number==1:
                raise OneError
        except:print('Input value is 1! try again!')
        else:print('No exception')
        finally:
            x=int(input('Do you need to continue?\n1.Yes\n2.No\n'))
            if x==1:
                continue
            elif x==2:
                break
            else:print('Invalid Entry! Try again')

main()