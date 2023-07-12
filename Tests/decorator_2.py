def deco(printing):
    def inner(*args,**kwargs):
        print('hello world')
        return printing(*args,**kwargs)
    return inner

@deco
def print_me():
    print('inside print me')

@deco
def print_data(name,age):
    print(f'Name is {name} & Age is {age}')

print_me()
print_data('kunjan',60)