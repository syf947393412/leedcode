dir=[[1,0],[0,1],[-1,0],[0,-1]]
def dfs(visited,grid,x,y):
    global count  #!
    for i in range(4):
        x_next=x+dir[i][0]
        y_next=y+dir[i][1]

        if x_next<0 or x_next>=len(grid) or y_next<0 or y_next>=len(grid[0]):
            continue
        if grid[x_next][y_next]==1 and visited[x_next][y_next]==0:
            count+=1
            visited[x_next][y_next]=1
            dfs(visited, grid, x_next, y_next)



if __name__=="__main__":
    n,m=map(int,input().split())
    grid=[]
    #存储图
    for i in range(n):
        grid.append(list(map(int,input().split())))
    #初始化辅助元素
    visited=[[0 for _ in range(m)] for _ in range(n)]
    result=0
    count=0  #!

    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and visited[i][j]==0:
                count=1
                visited[i][j]=1
                dfs(visited,grid,i,j)
                result=max(result,count)

    print(result)