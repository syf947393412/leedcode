class UnionFind():
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
        self.parent[v_root]=u_root

    def isSame(self,u,v):
        u_root=self.find(u)
        v_root=self.find(v)
        if u_root==v_root:
            return True
        else:
            return False

def main():
    m = int(input())
    n_nodes = 1001
    u = UnionFind(n_nodes)

    for _ in range(m):
        s, d = map(int, input().split())

        if not u.isSame(s, d):
            u.join(s, d)
        else:
            print(f"{s} {d}")
            return

if __name__=="__main__":
    main()



