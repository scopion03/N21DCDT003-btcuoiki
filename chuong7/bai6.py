class DoThiHuong:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def themCanh(self, u, v):
        self.adj[u].append(v)

    def SoCungVao(self, v):
        count = 0
        for i in range(self.V):
            for j in self.adj[i]:
                if j == v:
                    count += 1
        return count

# Ví dụ sử dụng
dt = DoThiHuong(5)
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(3, 0)
dt.themCanh(4, 2)

dinh = 2
so_cung_vao = dt.SoCungVao(dinh)
print(f"Số cung vào đỉnh {dinh} là {so_cung_vao}")
