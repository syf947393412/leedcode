from collections import deque


def bfs(grid,x,y):
    visit=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    que=deque()
    que.append((x,y))
    visit[x][y]=1  #!

    dir=[(0, 1), (1, 0), (0, -1), (-1, 0)]

    while que:
        (cur_x,cur_y)=que.popleft()  #!
        for i in range(4):
            new_x=cur_x+dir[i][0]
            new_y=cur_y+dir[i][1]

            if new_x<0 or new_x>=len(grid):
                continue
            if new_y<0 or new_y>=len(grid[0]):
                continue

            if visit[new_x][new_y]==1:
                continue
            que.append((new_x,new_y))
            visit[new_x][new_y]=1

