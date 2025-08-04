class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for item in s:
            if len(stack)!=0 and item==stack[-1]:
                stack.pop()
            elif len(stack)==0:
                stack.append(item)
            elif len(stack)!=0 and item!=stack[-1]:
                stack.append(item)
        return "".join(stack)