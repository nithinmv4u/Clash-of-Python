text=input('Enter the string')
length=len(text)
# print(length)
count=0
for i in range(length//2):
    if(text[i]==text[length-1-i]):
        count=count+1
if(count==(length//2)):
    print('Is Palindrome')
else:print('Not Palindrome')