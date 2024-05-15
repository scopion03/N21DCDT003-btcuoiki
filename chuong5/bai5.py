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

    # Phương thức kiểm tra xem cây có phải là BST không
    def KiemTraBST(self):
        return self._KiemTraBST(self.goc, float('-inf'), float('inf'))

    def _KiemTraBST(self, nut, gioiHanNho, gioiHanLon):
        if nut is None:
            return True
        
        # Kiểm tra giá trị của nút
        if nut.info <= gioiHanNho or nut.info >= gioiHanLon:
            return False

        # Kiểm tra BST tại cây con bên trái và cây con bên phải
        return (self._KiemTraBST(nut.left, gioiHanNho, nut.info) and
                self._KiemTraBST(nut.right, nut.info, gioiHanLon))

# Sử dụng
cay = CayNhiPhan()
cay.them(50)
cay.them(30)
cay.them(70)
cay.them(20)
cay.them(40)
cay.them(60)
cay.them(80)

print("Cây là BST:", cay.KiemTraBST())
