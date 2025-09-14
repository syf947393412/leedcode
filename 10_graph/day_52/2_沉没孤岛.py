dir=[[1,0],[0,1],[-1,0],[0,-1]]
def dfs(grid,x,y):
    grid[x][y]=2
    for i in range(4):
        x_next=x+dir[i][0]
        y_next=y+dir[i][1]

        if x_next<0 or x_next>=len(grid) or y_next<0 or y_next>=len(grid[0]):
            continue
        if grid[x_next][y_next]==1:
            dfs(grid, x_next,y_next)


if __name__=="__main__":
    n,m=map(int,input().split())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))
    for i in range(n):
        if grid[i][0]==1:
            dfs(grid,i,0)
        if grid[i][m-1]==1:
            dfs(grid,i,len(grid[0])-1)

    for j in range(m):
        if grid[0][j]==1:
            dfs(grid,0,j)
        if grid[n-1][j]==1:
            dfs(grid,n-1,j)
    result=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                grid[i][j]=0
            if grid[i][j]==2:
                grid[i][j] = 1
    print(grid)
