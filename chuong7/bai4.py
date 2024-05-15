class DoThi:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def themCanh(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def ChuaDinh(self, v):
        if v < 0 or v >= self.V:
            return False
        return True

# Ví dụ sử dụng
dt = DoThi(5)
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(3, 4)

dinh = 3
if dt.ChuaDinh(dinh):
    print(f"Đỉnh {dinh} tồn tại trong đồ thị")
else:
    print(f"Đỉnh {dinh} không tồn tại trong đồ thị")
