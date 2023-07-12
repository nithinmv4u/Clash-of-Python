def print_info(value,*vartupple):
    print('value is: ',value)
    for var in vartupple:
        print(var)
        print(id(var))
    return

print_info(10)
print_info(10,'hai',30,30,50)