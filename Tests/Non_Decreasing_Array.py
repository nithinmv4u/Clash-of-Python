def test(numbers):
    count=0
    order=0
    noorder=0
    for i in range(len(numbers)-1):
        print("i= ",i)
        value = [numbers[i]<=x for x in numbers[i+1:]]
        print(value)
        count += sum(1 for x in value if x==False)
        print(count)
        if count>=2:
            noorder+=1
            if noorder>=1 and order==1: 
                order=0
                break
            else:order=1
        elif count<=1 and noorder<=0:
            order = 1
        elif count ==1 and noorder>0:
            order = 0
        print(order)
        count=0
    # if order<=1:
    #     return 1
    if order == 1 or len(numbers)==1:
        return True
    else:
        return False


# numbers = [3,4,2,3]
# numbers = [5,7,1,8]
# numbers = [4,2,1]
# numbers = [4,2,3]
# numbers = [1]
# numbers = [1,2,3]
# numbers = [1,1,1]
numbers = [-1,4,2,3]
print(test(numbers))

