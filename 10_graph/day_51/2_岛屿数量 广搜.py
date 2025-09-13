from collections import deque

dir=[[1,0],[0,1],[-1,0],[0,-1]]

def bfs(visited,grid,i,j):
    que=deque()
    # que.append(grid[i][j])
    que.append((i,j))
    visited[i][j]=1

    while que:
        cur=que.popleft()
        for n in range(4):
            x_next=cur[0]+dir[n][0]
            y_next=cur[1]+dir[n][1]

            if x_next<0 or x_next>=len(grid) or y_next<0 or y_next>=len(grid[0]):
                continue
            if grid[x_next][y_next]==1 and visited[x_next][y_next]==0:
                visited[x_next][y_next]=1
                que.append((x_next,y_next))





if __name__=="__main__":
    n,m=map(int,input().split())

    #初始化,存图
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))

    visited=[[0 for _ in range(m)] for _ in range(n)]
    result=0

    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and visited[i][j]==0:
                result+=1
                bfs(visited,grid,i,j)

    print(result)







