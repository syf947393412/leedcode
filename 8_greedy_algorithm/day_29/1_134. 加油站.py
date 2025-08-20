from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_sum=0
        total_sum=0
        start=0  #cur_sum<0后的起始位置

        for i in range(len(gas)):
            cur_sum+=gas[i]-cost[i]
            total_sum+=gas[i]-cost[i]
            if cur_sum<0:
                cur_sum=0
                start=i+1

        if total_sum<0:
            return -1
        return start

s=Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(s.canCompleteCircuit(gas,cost))