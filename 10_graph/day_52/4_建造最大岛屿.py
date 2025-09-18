dir=[[1,0],[0,1],[-1,0],[0,-1]]
def dfs(grid,visited,x,y):
    if visited[x][y]==1:
        return
    visited[x][y]=1
    for i in range(4):
        x_next = x + dir[i][0]
        y_next = y + dir[i][1]

        if x_next < 0 or x_next >= len(grid) or y_next < 0 or y_next >= len(grid[0]):
            continue
        if grid[x_next][y_next]>=grid[x][y]:
            dfs(grid, visited, x_next, y_next)




if __name__=="__main__":
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))


