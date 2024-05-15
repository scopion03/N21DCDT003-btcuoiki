class DoThiVoHuong:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def themCanh(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def BacDinh(self, v):
        return len(self.adj[v])

# Ví dụ sử dụng
dt = DoThiVoHuong(5)
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(3, 4)

dinh = 0
bac = dt.BacDinh(dinh)
print(f"Bậc của đỉnh {dinh} là {bac}")
