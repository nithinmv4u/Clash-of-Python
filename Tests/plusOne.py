def newarray(num,digits=[]):
    rem = num%10
    num=num//10
    if num!=0:
        newarray(num)
    print(rem)
    digits.append(rem)
    print(digits)
    return digits
    

digits = [1, 2, 9]
num=0
for i in range(len(digits)):
    num=num*10+digits[i]
# print(num)
num=num+1
del(digits)
digits=newarray(num)

# for i in range(len(digits)):
#     pass
# sum=digits[i]+1
# del(digits[i])
# j=0
# rem=[]
# while sum!=0:
#     rem.append(sum%10)
#     sum=sum//10
#     j=len(rem)-1
# while True:
#     digits.append(rem[j])
#     i+=1
#     if j<=0:
#         break
#     j-=1
print(digits)