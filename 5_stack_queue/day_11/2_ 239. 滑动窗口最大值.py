from collections import deque
from typing import List


class MyQueue:  # 单调队列（从大到小
    def __init__(self):
        self.queue = deque()  # 这里需要使用deque实现单调队列，直接使用list会超时

    def pop(self,value):
        if self.queue and value==self.queue[0]:
            self.queue.pop()

    def push(self,value):
        while self.queue and self.queue[-1]<value:
            self.queue.popleft()
        self.queue.append((value))

    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=MyQueue()
        result=[]
        for i in range(k):
            q.push(nums[i])
        result.append(q.front())
        for i in range(k,len(nums)):
            q.pop(nums[i-k])
            q.push(nums[i])
            result.append(q.front())
        return result


s=Solution()
nums=[1,3,-1,-3,5,3,6,7]
k = 3
result=s.maxSlidingWindow(nums, k)
print(result)



