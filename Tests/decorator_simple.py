def deco(odd_or_even):
    def inner(*args):
        n=int(*args)
        if((n%2)==0):
            print('even')
        else:print('odd')
        return odd_or_even(*args)
    return inner

@deco
def typeof_dec(num):
    print("Result is: ",end='')

number=int(input('Enter a number: '))
typeof_dec(number)