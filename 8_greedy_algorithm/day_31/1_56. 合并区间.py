from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result=[]
        intervals.sort(key=lambda x:(x[0],x[1]))
        result.append(intervals[0])  #!比较的同时，顺带就修改了result里的边界


        for i in range(1,len(intervals)):
            if intervals[i][0]<=result[-1][1]:
                result[-1][1]=max(result[-1][1],intervals[i][1])

            else:
                result.append(intervals[i])

        return result