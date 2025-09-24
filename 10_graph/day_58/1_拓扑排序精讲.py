from collections import deque

if __name__=="__main__":
    n,m=map(int,input().strip().split())
    indegree=[0]*(n)
    map_dir=dict()
    for i in range(m):
        s,d=map(int,input().strip().split())
        indegree[d]+=1
        if s in map_dir:
            map_dir[s].append(d)
        else:
            map_dir[s]=[d]

    que=deque()
    result = []
    for i in range(n):
        if indegree[i]==0:
            que.append(i)
            # result.append(i)


    while que:
        cur=que.popleft()
        result.append(cur)   #!
        if cur in map_dir:
            for item in map_dir[cur]:
                indegree[item]-=1
                if indegree[item]==0:
                    que.append(item)
                    # result.append(item)

    # 检查是否所有节点都已访问（如果图中有环，则不会）
    if len(result) == n:
        # 修改点3: 将整数列表转换为字符串列表再 join
        result_str = " ".join(map(str, result))
        print(result_str)
    else:
        print("图中存在环，无法进行拓扑排序")



