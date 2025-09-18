dir=[[1,0],[0,1],[-1,0],[0,-1]]


if __name__=="__main__":
    n,m=map(int,input().split())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))

    result=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                for n in range(4):
                    x_next=i+dir[n][0]
                    y_next=j+dir[n][1]

                    if x_next<0 or x_next>=len(grid) or y_next<0 or y_next>=len(grid[0]) or grid[x_next][y_next]==0:
                        result+=1
    print(result)
