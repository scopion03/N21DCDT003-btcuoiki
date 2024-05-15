class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

def SoNutLa(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        # Nếu nút hiện tại là nút lá, trả về 1
        return 1
    else:
        # Đệ quy tính số nút lá của cây con bên trái và cây con bên phải
        so_nut_la_trai = SoNutLa(root.left)
        so_nut_la_phai = SoNutLa(root.right)

        return so_nut_la_trai + so_nut_la_phai

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

print("Số nút lá của cây nhị phân là:", SoNutLa(root))  # Kết quả: 3
