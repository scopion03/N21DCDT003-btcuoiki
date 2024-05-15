class DoThi:
    def __init__(self):
        self.danh_sach_dinh = {}

    def them_dinh(self, dinh):
        if dinh not in self.danh_sach_dinh:
            self.danh_sach_dinh[dinh] = []

    def them_cung(self, dinh1, dinh2):
        if dinh1 in self.danh_sach_dinh:
            self.danh_sach_dinh[dinh1].append(dinh2)
        else:
            print(f"{dinh1} không tồn tại trong đồ thị.")

    def DuongDi(self, v1, v2):
        if v1 not in self.danh_sach_dinh or v2 not in self.danh_sach_dinh:
            return False

        visited = set()  # Tập các đỉnh đã duyệt
        stack = [v1]  # Stack để duyệt đồ thị

        while stack:
            dinh = stack.pop()
            visited.add(dinh)

            if dinh == v2:
                return True

            for dinh_ke in self.danh_sach_dinh[dinh]:
                if dinh_ke not in visited:
                    stack.append(dinh_ke)

        return False

# Sử dụng
dt = DoThi()
dt.them_dinh('A')
dt.them_dinh('B')
dt.them_dinh('C')
dt.them_dinh('D')
dt.them_cung('A', 'B')
dt.them_cung('B', 'C')
dt.them_cung('C', 'D')
dt.them_cung('D', 'A')

print("Có đường đi từ A đến C:", dt.DuongDi('A', 'C'))
print("Có đường đi từ B đến D:", dt.DuongDi('B', 'D'))
print("Có đường đi từ C đến A:", dt.DuongDi('C', 'A'))
print("Có đường đi từ D đến B:", dt.DuongDi('D', 'B'))
print("Có đường đi từ A đến D:", dt.DuongDi('A', 'D'))
