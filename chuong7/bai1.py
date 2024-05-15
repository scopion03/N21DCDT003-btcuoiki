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

    def LienThong(self):
        visited = [False] * self.V
        self.DFS(0, visited)

        # Kiểm tra xem tất cả các đỉnh có được duyệt qua không
        for i in range(self.V):
            if not visited[i]:
                return False
        return True

# Ví dụ sử dụng
dt = DoThi(5)
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(3, 4)

if dt.LienThong():
    print("Đồ thị là đồ thị liên thông")
else:
    print("Đồ thị không phải là đồ thị liên thông")
