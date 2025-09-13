
dir=[[1,0],[0,1],[-1,0],[0,-1]]

def dfs(visited,grid,x,y):
    #终止条件
    if grid[x][y]==0 or visited[x][y]==1:
        return
    visited[x][y]=1

    for i in range(4):
        next_x=x+dir[i][0]
        next_y=y+dir[i][1]

        #判断是否越界：
        if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
            continue
        dfs(visited,grid,next_x,next_y)

if __name__=="__main__":
    n,m=map(int,input().split())

    #初始化
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))

    visited=[[0 for _ in range(m) for _ in range(n)]]
    result=0

    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and visited[i][j]==0:
                result+=1
                visited[i][j]=1
                dfs(visited,grid,i,j)

    print(result)







