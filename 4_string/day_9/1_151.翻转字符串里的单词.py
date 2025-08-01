#法一：

#由于Python字符串的不可变性，因此只能转换为列表进行处理
def reverseWords( s: str) -> str:
    s_list=s.split()   #!单词如何拆分
    re_s_list=s_list[::-1]
    s_str=" ".join(re_s_list)
    return s_str






s = "a good   example"
print(reverseWords(s))
