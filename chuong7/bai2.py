class DoThi:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def themCanh(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFS(self, v, visited):
        visited[v] = True
        for i in self.adj[v]:
            if not visited[i]:
                self.DFS(i, visited)

    def SoThanhPhan(self):
        visited = [False] * self.V
        count = 0
        for v in range(self.V):
            if not visited[v]:
                self.DFS(v, visited)
                count += 1
        return count

# Ví dụ sử dụng
dt = DoThi(7)
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(3, 4)
dt.themCanh(5, 6)

so_thanh_phan = dt.SoThanhPhan()
print("Số thành phần liên thông của đồ thị là:", so_thanh_phan)
