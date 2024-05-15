class ToanTuMang:
    def __init__(self, mang):
        self.mang = mang

    def Hop(self, mang_khac):
        tap_a = set(self.mang)
        tap_b = set(mang_khac)
        tap_hop = tap_a.union(tap_b)
        mang_ket_qua = sorted(list(tap_hop))
        return mang_ket_qua

# Ví dụ sử dụng
a = ToanTuMang([1, 5, 3, 7, 9, 4, 2])
b = [9, 6, 2, 3, 8]

c = a.Hop(b)
print(c)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
