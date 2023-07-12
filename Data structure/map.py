def xappend(str):
    print("data: ", str)
    return ("New : "+ str)

string = list(map(xappend, input().strip().split()))
print(string)
print(len(string))
for i in range(len(list(string))):
    print(string[i])