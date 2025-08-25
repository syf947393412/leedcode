from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==0:
            return 0
        result=1 #一定有气球，一定需要箭
        # points.sort(key=lambda x:points[x][0])
        points.sort(key=lambda x:x[0])

        for i in range(1,len(points)):
            if points[i][0]>points[i-1][1]:
                result+=1
            else:
                points[i][1]=min(points[i-1][1],points[i][1])

        return result
