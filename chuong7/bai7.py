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
    
    def SoCungRa(self, dinh):
        if dinh in self.danh_sach_dinh:
            return len(self.danh_sach_dinh[dinh])
        else:
            print(f"{dinh} không tồn tại trong đồ thị.")

# Sử dụng
dt = DoThi()
dt.them_dinh('A')
dt.them_dinh('B')
dt.them_dinh('C')
dt.them_cung('A', 'B')
dt.them_cung('A', 'C')
dt.them_cung('B', 'C')

print("Số cung đi ra từ đỉnh A:", dt.SoCungRa('A'))
print("Số cung đi ra từ đỉnh B:", dt.SoCungRa('B'))
print("Số cung đi ra từ đỉnh C:", dt.SoCungRa('C'))
