x = 123344567
def palindrome(x):
    if not x: return True
    comp = 0
    while(x!=0):
        comp = comp*10 + x%10
        if not comp:break
        # print(f"x: {x} comp: {comp}")
        if (x == comp or x<comp): break
        x = x//10
        # print(f"x: {x} comp: {comp}")
        if (x == comp): break
    if (x==comp): return True
    return False

bool_val = palindrome(x)
print(bool_val)