#-----------FUNCTION PASSING ARGUMENTS DIFFERENT TYPES-----------

# def printme(name,age=35):
#     print('Name: ', name)
#     print('Age: ', age)
#     return

# printme(age=50,name='nithin')
# printme('nithin')

#----------VARIABLE LENGTH ARGUMENTS--------------

# def print_info(value,*vartupple):
#     print('value is: ',value)
#     for var in vartupple:
#         print(var)
#         print(id(var))
#     return

# print_info(10)
# print_info(10,'hai',30,30,50)

#-------LAMBDA FUNCTION------------------

# sum=lambda a,b:a+b
# print('Sum: ',sum(10,20))


#--------------------SCOPE-------------------

total=0

def sum(a,b):
    total=a+b
    print('Total inside=',total)
    return total

sum(10,20)
print(f'Total outside= {total}')
total=sum(23,32)
print(f'Total after taking return= {total}')