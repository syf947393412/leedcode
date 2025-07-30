def transform(s:str):
    s_list=list(s)
    for index,i in enumerate(s_list):
        if (ord(i)-ord('a'))>=0 and (ord(i)-ord('a'))<26:
            continue
        else:
            s_list[index]="number"
    s="".join(s_list)
    return s

s="a1b2c3"
print(transform(s))