def duplicateZeroes(list):
    length = len(list)-1
    i=0
    while i<len(list):
        # print(i)
        if list[i] == 0:
            for j in range(length, i+1, -1):
                # print(list[j])
                list[j] = list[j-1]
                # print(list)
            list[i+1] = 0
            # print(list)
            i+=2
            # print(i)
        i+=1

    print(list)
list = [1,2,0,3,4,0,2,3,4]
duplicateZeroes(list)