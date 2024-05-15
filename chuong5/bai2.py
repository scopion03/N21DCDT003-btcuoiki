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

# Test
# Xây dựng cây nhị phân:
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

print("Chiều cao của cây nhị phân là:", ChieuCao(root))  # Kết quả: 3
