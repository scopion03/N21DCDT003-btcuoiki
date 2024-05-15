class DoThi:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def themCanh(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFS(self, v, visited, parent):
        visited[v] = True
        for i in self.adj[v]:
            if not visited[i]:
                if self.DFS(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False

    def ChuTrinh(self):
        visited = [False] * self.V
        for v in range(self.V):
            if not visited[v]:
                if self.DFS(v, visited, -1):
                    return True
        return False

# Ví dụ sử dụng
dt = DoThi(6)
dt.themCanh(0, 1)
dt.themCanh(1, 2)
dt.themCanh(2, 3)
dt.themCanh(3, 4)
dt.themCanh(4, 5)

if dt.ChuTrinh():
    print("Đồ thị chứa chu trình")
else:
    print("Đồ thị không chứa chu trình")
