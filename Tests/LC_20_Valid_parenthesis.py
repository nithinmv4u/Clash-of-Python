# para = "[{()}]"
para = "()[]{}"
# para = "{[]}"


def check(para, i=0):
    print(f"para[i]: {para[i]}  para[i+1]: {para[i+1]}  i: {i}   half length: {len(para)//2} compare: {para[i]!=para[i+1]}")
    c=''
    if para[i]=='[':c=']'
    if para[i]=='{':c='}'
    if para[i]=='(':c=')'
    if c!=para[i+1] and i <= len(para)//2:
        valid = False
        print(f"failed valid: {valid}")
        check(para, i+1)
    elif c==para[i+1] and i <= len(para)//2:
        valid = True
        print(f"success valid: {valid}")

    print(f"len: {len(para) }  c: {c} para[len(para)-(len(para)-(i+1))]: {para[len(para)-(i+1)]}  i: {i}   len(para)-(i+1):{len(para)-(i+1)}")
    if c==para[len(para)-(i+1)]:
        valid = True
        print(f"valid: {valid}")
        try:check(para, i+2)
        except:pass
    else:
        valid = False
        print(f"valid: {valid}")
    return valid

valid = check(para, 0)
print(valid)