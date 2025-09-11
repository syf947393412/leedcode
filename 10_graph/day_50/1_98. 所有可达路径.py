def dfs(graph,x,n,path,result):
    if x==n:
        result.append(path[:])
        return

    # for i in range(len(graph)):
    for i in range(1,len(graph)):
        if graph[x][i]==1:
            path.append(i)
            dfs(graph,i,n,path,result)
            path.pop()
    return

def main():
    n,m=map(int,input().split())
    graph=[[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(m):
        s,t=map(int,input().split())
        graph[s][t]=1

    result=[]
    # dfs(graph,1,n,[],result)
    dfs(graph,1,n,[1],result)
    if not result:
        print(-1)
    else:
        for path in result:
            print(' '.join(map(str, path)))

if __name__ == "__main__":
    main()



