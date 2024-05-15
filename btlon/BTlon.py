class NghiaTu:
    def __init__(self, loai_tu, nghia, vi_du):
        self.loai_tu = loai_tu
        self.nghia = nghia
        self.vi_du = vi_du

    def __str__(self):
        return f"{self.loai_tu}: {self.nghia} (ví dụ: {self.vi_du})"

class MucTuDien:
    def __init__(self, tu):
        self.tu = tu
        self.danh_sach_nghia = []

    def them_nghia(self, loai_tu, nghia, vi_du):
        self.danh_sach_nghia.append(NghiaTu(loai_tu, nghia, vi_du))

    def __str__(self):
        danh_sach_nghia_str = "\n".join(str(nghia) for nghia in self.danh_sach_nghia)
        return f"{self.tu}:\n{danh_sach_nghia_str}"

class NodeBST:
    def __init__(self, khoa):
        self.khoa = khoa
        self.trai = None
        self.phai = None

class TuDienBST:
    def __init__(self):
        self.goc = None

    def chen(self, tu, loai_tu, nghia, vi_du):
        muc_tu = MucTuDien(tu)
        muc_tu.them_nghia(loai_tu, nghia, vi_du)
        if self.goc is None:
            self.goc = NodeBST(muc_tu)
        else:
            self._chen_de_quy(self.goc, muc_tu)

    def _chen_de_quy(self, node, muc_tu):
        if muc_tu.tu < node.khoa.tu:
            if node.trai is None:
                node.trai = NodeBST(muc_tu)
            else:
                self._chen_de_quy(node.trai, muc_tu)
        elif muc_tu.tu > node.khoa.tu:
            if node.phai is None:
                node.phai = NodeBST(muc_tu)
            else:
                self._chen_de_quy(node.phai, muc_tu)
        else:
            node.khoa.them_nghia(muc_tu.danh_sach_nghia[0].loai_tu, muc_tu.danh_sach_nghia[0].nghia, muc_tu.danh_sach_nghia[0].vi_du)

    def tim(self, tu):
        return self._tim_de_quy(self.goc, tu)

    def _tim_de_quy(self, node, tu):
        if node is None:
            return None
        if tu < node.khoa.tu:
            return self._tim_de_quy(node.trai, tu)
        elif tu > node.khoa.tu:
            return self._tim_de_quy(node.phai, tu)
        else:
            return node.khoa

    def xoa(self, tu):
        self.goc = self._xoa_de_quy(self.goc, tu)

    def _xoa_de_quy(self, node, tu):
        if node is None:
            return node
        if tu < node.khoa.tu:
            node.trai = self._xoa_de_quy(node.trai, tu)
        elif tu > node.khoa.tu:
            node.phai = self._xoa_de_quy(node.phai, tu)
        else:
            if node.trai is None:
                return node.phai
            elif node.phai is None:
                return node.trai
            node.khoa = self._tim_min(node.phai).khoa
            node.phai = self._xoa_de_quy(node.phai, node.khoa.tu)
        return node

    def _tim_min(self, node):
        hien_tai = node
        while hien_tai.trai is not None:
            hien_tai = hien_tai.trai
        return hien_tai

    def luu_vao_tap_tin(self, ten_tap_tin):
        with open(ten_tap_tin, 'w') as f:
            self._luu_de_quy(self.goc, f)
        print(f"tu dien da duoc luu vao tap tin '{ten_tap_tin}' thanh cong.")    

    def _luu_de_quy(self, node, file):
        if node is not None:
            file.write(str(node.khoa) + "\n")
            self._luu_de_quy(node.trai, file)
            self._luu_de_quy(node.phai, file)

    def nap_tu_tap_tin(self, ten_tap_tin):
        self.goc = None
        with open(ten_tap_tin, 'r') as f:
            cac_dong = f.readlines()
            for dong in cac_dong:
                tu, phan_con_lai = dong.split(':', 1)
                cac_nghia = phan_con_lai.strip().split(';')
                for n in cac_nghia:
                    loai_tu, nghia_vi_du = n.split(':', 1)
                    nghia, vi_du = nghia_vi_du.split('(ví dụ:', 1)
                    vi_du = vi_du.strip().strip(')')
                    self.chen(tu.strip(), loai_tu.strip(), nghia.strip(), vi_du.strip())

def main():
    tu_dien = TuDienBST()
    while True:
        print("\nTrình đơn từ điển")
        print("1. Thêm từ mới")
        print("2. Xóa từ")
        print("3. Tra cứu từ")
        print("4. Lưu từ điển vào tập tin")
        print("5. Nạp từ điển từ tập tin")
        print("6. Thoát")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            tu = input("Nhập từ: ")
            loai_tu = input("Nhập loại từ: ")
            nghia = input("Nhập nghĩa: ")
            vi_du = input("Nhập ví dụ: ")
            tu_dien.chen(tu, loai_tu, nghia, vi_du)
        elif lua_chon == '2':
            tu = input("Nhập từ cần xóa: ")
            tu_dien.xoa(tu)
        elif lua_chon == '3':
            tu = input("Nhập từ cần tra cứu: ")
            muc_tu = tu_dien.tim(tu)
            if muc_tu:
                print(muc_tu)
            else:
                print("Không tìm thấy từ.")
        elif lua_chon == '4':
            ten_tap_tin = input("Nhập tên tập tin để lưu: ")
            tu_dien.luu_vao_tap_tin(ten_tap_tin)
        elif lua_chon == '5':
            ten_tap_tin = input("Nhập tên tập tin để nạp: ")
            tu_dien.nap_tu_tap_tin(ten_tap_tin)
        elif lua_chon == '6':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
