from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        result=[1]*len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                result[i]=result[i-1]+1

        # for i in range(len(ratings)-2,0,-1):
        # #!①len(ratings)-2  ②-1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                result[i]=max(result[i+1]+1,result[i])

        return sum(result)

ratings =[1,0,2]
s=Solution()
print(s.candy(ratings))