# def outer(message):
#     def inner():
#         print(message)
#     return inner

# one=outer('hi')
# two=outer('hello')
# one()
# two()

def deco(printing):
    def inner():
        print('Hello World')
        return printing()
    return inner

@deco
def print_me():None

# print_fn=deco(print_me)   #-----@deco is alternative to this line-----------
# print_fn()

print_me()