class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

def ChieuCao(root):
    if root is None:
        return 0
    else:
        # Tính chiều cao của cây con bên trái và bên phải
        chieu_cao_trai = ChieuCao(root.left)
        chieu_cao_phai = ChieuCao(root.right)

        # Trả về chiều cao lớn nhất của cây con bên trái và bên phải, cộng thêm 1 cho nút gốc
        return max(chieu_cao_trai, chieu_cao_phai) + 1

def KiemTraAVL(root):
    if root is None:
        return True
    
    # Kiểm tra điều kiện 1: chênh lệch chiều cao của hai cây con không quá 1
    chieu_cao_trai = ChieuCao(root.left)
    chieu_cao_phai = ChieuCao(root.right)
    if abs(chieu_cao_trai - chieu_cao_phai) > 1:
        return False
    
    # Kiểm tra điều kiện 2 và 3: cả hai cây con phải là cây AVL và cây phải là cây nhị phân tương đối cân bằng
    return KiemTraAVL(root.left) and KiemTraAVL(root.right)

# Test
# Xây dựng một cây AVL:
#        1
#       / \
#      2   3
#     / \
#    4   5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Cây nhị phân trên là một cây AVL:", KiemTraAVL(root))  # Kết quả: True
