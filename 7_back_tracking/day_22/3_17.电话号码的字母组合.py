from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = [
            "",  # 0
            "",  # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs",  # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        result=[]
        if not digits:    #!
            return []
        self.backtracing(digits,letterMap,0,[],result=result)
        return result



    def backtracing(self,digits:str,letterMap,index,path,result):

        if len(path)==len(digits):
            # result.append(path)
            # result.append(path[:])
            result.append("".join(path))
            return


        digits_int=int(digits[index])
        str=letterMap[digits_int]
        # for s in str:
        for i in range(len(str)):
            s=str[i]
            path.append(s)
            self.backtracing(digits,letterMap,index+1,path,result)
            path.pop()
        return

