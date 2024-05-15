class Node:
    def __init__(self, thong_tin):
        self.thong_tin = thong_tin
        self.trai = None
        self.phai = None

def laBSTTuanTu(goc):
    if goc is None:
        return True

    # Nếu nút có cả hai con trái và phải, thì không phải là cây tuần tự
    if goc.trai is not None and goc.phai is not None:
        return False

    # Đệ quy kiểm tra cây con bên trái và cây con bên phải
    trai_tuan_tu = laBSTTuanTu(goc.trai)
    phai_tuan_tu = laBSTTuanTu(goc.phai)

    return trai_tuan_tu and phai_tuan_tu

# Hàm tiện ích để in cây theo thứ tự in-order (duyệt trung thứ tự) để kiểm tra kết quả
def duyet_trung_thu_tu(goc):
    if goc:
        duyet_trung_thu_tu(goc.trai)
        print(goc.thong_tin, end=' ')
        duyet_trung_thu_tu(goc.phai)

# Ví dụ sử dụng
if __name__ == "__main__":
    # Tạo một cây nhị phân mẫu là cây tuần tự
    goc1 = Node(1)
    goc1.trai = Node(2)
    goc1.trai.trai = Node(3)
    goc1.trai.trai.trai = Node(4)

    # Tạo một cây nhị phân không phải là cây tuần tự
    goc2 = Node(1)
    goc2.trai = Node(2)
    goc2.phai = Node(3)

    # Kiểm tra xem cây có phải là cây tuần tự hay không
    print("Cây goc1 có phải là cây BST tuần tự không:", laBSTTuanTu(goc1))  # Kết quả mong đợi: True
    print("Cây goc2 có phải là cây BST tuần tự không:", laBSTTuanTu(goc2))  # Kết quả mong đợi: False
