def lower_case(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        print("herre")
        return string_lowercase
    return wrapper

@lower_case
def hello():
    return 'Hello WORLD'

h=hello()
print(h)
print(hello())
# calling hello directly invokes 'wrapper' and hence has a return of 'string_lowercase'
# ineffect, hello is initially replaced by wrapper when trying to print hello in single line
# at same time, since hello is replaced, hello seems to be undefined