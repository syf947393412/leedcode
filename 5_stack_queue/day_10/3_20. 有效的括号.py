class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for item in s:
            if item=="(":
                stack.append(")")
            elif item=="[":
                stack.append("]")
            elif item=="{":
                stack.append("}")
            # elif item!=stack.pop() or len(stack)==0: #！如果栈为空就会报错。应该先检查栈是否为空。
            elif len(stack)==0 or item!=stack[-1]:
                return False
            else:
                stack.pop()   #!

        return len(stack)==0
