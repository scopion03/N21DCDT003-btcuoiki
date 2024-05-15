class TuDien:
    def __init__(self):
        self.tu_dien = {}

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        key = tu[0].lower()  # Sử dụng ký tự đầu tiên của từ làm khóa
        if key not in self.tu_dien:
            self.tu_dien[key] = {}
        self.tu_dien[key][tu] = {
            "dong_nghia": dong_nghia,
            "trai_nghia": trai_nghia
        }

    def TraTu(self, tu):
        key = tu[0].lower()  # Sử dụng ký tự đầu tiên của từ làm khóa
        if key in self.tu_dien and tu in self.tu_dien[key]:
            return self.tu_dien[key][tu]
        else:
            return None


# Ví dụ sử dụng lớp TuDien
td = TuDien()
td.NhapTu("hạnh phúc", "vui vẻ", "buồn bã")
td.NhapTu("buồn bã", "sầu não", "vui vẻ")

# Tra từ
ket_qua = td.TraTu("hạnh phúc")
if ket_qua:
    print(f"Từ đồng nghĩa của 'hạnh phúc': {ket_qua['dong_nghia']}")
    print(f"Từ trái nghĩa của 'hạnh phúc': {ket_qua['trai_nghia']}")
else:
    print("Từ cần tra không có trong từ điển.")

ket_qua = td.TraTu("buồn bã")
if ket_qua:
    print(f"Từ đồng nghĩa của 'buồn bã': {ket_qua['dong_nghia']}")
    print(f"Từ trái nghĩa của 'buồn bã': {ket_qua['trai_nghia']}")
else:
    print("Từ cần tra không có trong từ điển.")
