
v,e=map(int,input().strip().split())

graph=[[10001 for _ in range(v+1)] for _ in range(v+1) ]

for i in range(e):
    s,d,dis=map(int,input().strip().split())
    graph[s][d]=dis
    graph[d][s]=dis

visited=[False]*(v+1)
minDist=[100001]*(v+1)
#需要的起点：
minDist[1]=0

for i in range(1,v):
    min=1000002
    cur=1
    for j in range(1,v+1):
        if visited[j]==False and minDist[j]<min:
            cur=j
            min=minDist[j]  #!

    visited[cur]=True
    for j in range(1,v+1):
        #需要确保 graph[cur][j] > 0 来排除不存在的边
        if visited[j]==False and graph[cur][j] > 0 and  minDist[j]>graph[cur][j]:
            minDist[j]=graph[cur][j]

result=0
for i in range(2,v+1):
    result+=minDist[i]
print(result)

