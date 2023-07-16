x = 1234321
def palindrome(x):
    safe = x
    comp = 0
    while(x!=0):
        rem=x%10
        comp = comp*10 + rem
        # print(f"x: {x} comp: {comp}")
        x = x//10
    if safe == comp:
        return True
    else:return False

bool_val = palindrome(x)
print(bool_val)