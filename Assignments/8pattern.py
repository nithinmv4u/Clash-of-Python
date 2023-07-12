limit=int(input('Enter Limit: '))
limit+=1
for i in range(limit):
    for j in range(1,i+1):
        print(j ,end=" ")
    print()