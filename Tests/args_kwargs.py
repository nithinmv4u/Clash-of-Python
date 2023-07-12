def args_demo(*args):
    for arg in args:
        print(arg)

args_demo(3, 'a', 'kjl', 78)
# demo()

def kwargs_demo(**kwargs):
    for key, value in kwargs.items():
        print(key, " : ", value)

kwargs_demo(name='Matt', age=57, country='Britain')

# kwargs_demo(2, 'ghjjh', 544, 'bhjh')

# def multi_person(**kwargs):
#     persons=[]
#     for key, value in kwargs:
#         persons.append()