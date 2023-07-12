total=0

def sum(a,b):
    total=a+b
    print('Total inside=',total)
    return total

sum(10,20)
print(f'Total outside= {total}')
total=sum(23,32)
print(f'Total after taking return= {total}')