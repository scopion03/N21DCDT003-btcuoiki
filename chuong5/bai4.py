class Nut:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.goc = None

    # Phương thức thêm một nút mới vào cây
    def them(self, giaTri):
        if self.goc is None:
            self.goc = Nut(giaTri)
        else:
            self._them(self.goc, giaTri)

    def _them(self, nut, giaTri):
        if giaTri < nut.info:
            if nut.left is None:
                nut.left = Nut(giaTri)
            else:
                self._them(nut.left, giaTri)
        else:
            if nut.right is None:
                nut.right = Nut(giaTri)
            else:
                self._them(nut.right, giaTri)

    # Phương thức đếm số nút trung gian của cây
    def SoNutTrungGian(self):
        return self._SoNutTrungGian(self.goc)

    def _SoNutTrungGian(self, nut):
        if nut is None:
            return 0
        elif nut.left is not None and nut.right is not None:
            return 1 + self._SoNutTrungGian(nut.left) + self._SoNutTrungGian(nut.right)
        else:
            return self._SoNutTrungGian(nut.left) + self._SoNutTrungGian(nut.right)

# Sử dụng
cay = CayNhiPhan()
cay.them(50)
cay.them(30)
cay.them(70)
cay.them(20)
cay.them(40)
cay.them(60)
cay.them(80)

print("Số nút trung gian của cây:", cay.SoNutTrungGian())
