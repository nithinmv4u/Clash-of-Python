def count_num(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] +=1
        else:
            frequency[num]=1
    return frequency

array = [2,4, 6,7,4,3,5,2,4,3,7,6,8]
freq = count_num(array)
print(freq)
for num in freq:
    if freq[num]>1:
        print(num,end=' ')
        # print(str(num)+" ",end='')