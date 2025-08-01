def reverse_str(s:str,k:int):
    s_list=list(s)
    s_list[:len(s)-k]=s_list[:len(s)-k][::-1]
    s_list[len(s)-k:]=s_list[len(s)-k:][::-1]
    s_list=s_list[::-1]
    s_str="".join(s_list)
    return s_str

s="abcdefg"
k=2
print(reverse_str(s,k))