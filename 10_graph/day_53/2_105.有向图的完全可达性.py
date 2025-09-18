from collections import deque


# def dfs(grid,start_index,visited):
#     if visited[start_index]==1:
#         return
#     visited[start_index]=1
#
#     for n in range(len(grid[start_index])):
#         new=grid[start_index][n]
#         dfs(grid, new, visited)
def bfs(grid,start_index,visited):
    que=deque()
    que.append(start_index)
    visited[start_index] = 1  # 优化点：在入队时就标记，避免重复入队

    while que:
        cur=que.popleft()
        # visited[cur] = 1
        # for item in range(grid[cur]):
        for item in grid[cur]:
            if visited[item]==0:
                que.append(item)
                visited[item] =1

    return



def main():
    n, m = map(int, input().split())
    grid =[[] for _ in range(n+1)]

    for _ in range(m):
        start,end=map(int, input().split())
        grid[start].append(end)

    visited=[0]*(n+1)
    bfs(grid,1,visited)
    for i in range(1,n+1):
        if visited[i]==0:
            return -1
    return 1
if __name__=="__main__":
    print(main())
