class TuDien:
    def __init__(self):
        self.tu_dien = {}

    def NhapTu(self, tu, cac_dong_nghia=None, cac_trai_nghia=None):
        key = tu[0].lower()  # Sử dụng ký tự đầu tiên của từ làm khóa
        if key not in self.tu_dien:
            self.tu_dien[key] = {}
        self.tu_dien[key][tu] = {
            "dong_nghia": cac_dong_nghia if cac_dong_nghia else [],
            "trai_nghia": cac_trai_nghia if cac_trai_nghia else []
        }

    def DongNghia(self, tu):
        key = tu[0].lower()  # Sử dụng ký tự đầu tiên của từ làm khóa
        if key in self.tu_dien and tu in self.tu_dien[key]:
            return self.tu_dien[key][tu]["dong_nghia"]
        else:
            return []

    def TraiNghia(self, tu):
        key = tu[0].lower()  # Sử dụng ký tự đầu tiên của từ làm khóa
        if key in self.tu_dien and tu in self.tu_dien[key]:
            return self.tu_dien[key][tu]["trai_nghia"]
        else:
            return []

# Ví dụ sử dụng lớp TuDien
td = TuDien()
td.NhapTu("hạnh phúc", ["vui vẻ", "sung sướng"], ["buồn bã", "khổ đau"])
td.NhapTu("buồn bã", ["sầu não", "u sầu"], ["vui vẻ", "hạnh phúc"])

# Tra từ đồng nghĩa
dong_nghia = td.DongNghia("hạnh phúc")
print(f"Từ đồng nghĩa của 'hạnh phúc': {dong_nghia}")

dong_nghia = td.DongNghia("buồn bã")
print(f"Từ đồng nghĩa của 'buồn bã': {dong_nghia}")

# Tra từ trái nghĩa
trai_nghia = td.TraiNghia("hạnh phúc")
print(f"Từ trái nghĩa của 'hạnh phúc': {trai_nghia}")

trai_nghia = td.TraiNghia("buồn bã")
print(f"Từ trái nghĩa của 'buồn bã': {trai_nghia}")
