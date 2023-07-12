from this import s


string1= 'ab#c'
string2= 'ad#c'

# string1 = string1.strip().split()
print(len(string1))

# def remStr(s):
#     if s == '#':
#         return 0
#     else:
#         return 1

# for i in len(string1):
#     # print(s)
#     rep = remStr(s)
#     if rep == 0:
#         string1[i]== string1[i+1]
def clrStr(i, str):
    for _ in range(i, len(str)-1):
        str[i]=str[i+1]
    return str

for i in len(string1):
    if string1[i]=='#':
        string1=clrStr(i, string1)

for i in len(string2):
    if string2[i]=='#':
        string2=clrStr(i, string2)

if string1 == string2:
    print("True")
else:print("False")
    