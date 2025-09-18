class UnionFind():
    def __init__(self,n):
        self.parent=list(range(n+1))

    def find(self,u):
        if u==self.parent[u]:
            return u

        root=self.find(self.parent[u])
        self.parent[u]=root
        return root

    def union(self,u,v):
        u_root=self.find(u)
        v_root=self.find(v)
        if u_root==v_root:
            return
        u_root=self.parent[v_root]

    def is_same(self,u,v):
        return self.find(u)==self.find(v)


if __name__=="__main__":
    data = input().split()

    index=0
    n=int(data[index])
    index+=1
    m=int(data[index])
    index+=1

    u=UnionFind(n)
    for _ in range(m):
        s=int(data[index])
        index+=1
        d=int(data[index])
        index+=1
        u.union(s,d)

    s=int(data[index])
    index+=1
    d=int(data[index])
    index+=1

    if u.is_same(s,d):
        print(1)
    else:
        print(0)







