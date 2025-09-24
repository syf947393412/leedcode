class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n+1))

    def find(self,u):
        if u==self.parent[u]:
            return u
        root=self.find(self.parent[u])
        self.parent[u]=root
        return root

    def join(self,u,v):
        u_root=self.find(u)
        v_root=self.find(v)
        if u_root==v_root:
            return
        else:
            self.parent[v_root]=u_root

    def isSame(self,u,v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return True
        else:
            return False

class Edge:
    def __init__(self,l,r,val):
        self.l=l
        self.r=r
        self.val=val


if __name__ == "__main__":
    v, e = map(int, input().strip().split())

    edges=[]
    for i in range(e):
        l,r,val=map(int,input().strip().split())
        edges.append(Edge(l,r,val))

    edges.sort(key=lambda x:x.val)

    u=UnionFind(v)
    result=0
    for edge in edges:
        if u.isSame(edge.l,edge.r)==False:
            result+=edge.val
            u.join(edge.l,edge.r)
    print(result)




