def split(num):
    while(num!=0):
        digit = num%10
        print(digit)
        num = num//10

def split2(num):
    digit = num%10
    return digit

def split3(num):
    digit = num%10  
    if num//10!=0:
        n=split3(num//10)
        print(n)
    return digit

# num = 345
# split(num)
# while(num!=0):
#     print(split2(num))
#     num = num//10

num = 768
split3(num*10)
