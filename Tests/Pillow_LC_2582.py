def passThePillow(n: int, time: int) -> int:
    i=1
    count=1
    p=1
    while(True):
        i+=p
        print("count: ",count,"  i: ",i)
        if count==time:
            return i
        count+=1
        if i==n:
            p=-1
        elif i==1:
            p=1
        # print("fir: ",i)
        # if(count==time):
        #     return i
        # # print("fir: ",count)
        # i+=1
        # count+=1
        # if(i<n):
        #     continue
        # else:
        #     i-=1
        #     while(i!=0):
        #         # print("sec: ",count)
        #         print("sec: ",i)
        #         if(count==time):
        #             break
        #         i-=1
        #         count+=1

print(passThePillow(4,5))