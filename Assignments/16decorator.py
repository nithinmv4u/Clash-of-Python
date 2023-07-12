def deco(printing):
    def inner():
        print('Hello World')
        return printing()
    return inner

@deco
def print_me():None

print_me()