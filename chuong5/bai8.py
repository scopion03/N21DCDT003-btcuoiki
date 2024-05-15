class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def SoSanh(cay1, cay2):
    # Nếu cả hai cây đều rỗng, chúng giống hệt nhau
    if cay1 is None and cay2 is None:
        return True
    
    # Nếu chỉ một trong hai cây rỗng, chúng không giống nhau
    if cay1 is None or cay2 is None:
        return False
    
    # Kiểm tra giá trị của nút hiện tại và đệ quy kiểm tra các nút con bên trái và bên phải
    return (cay1.info == cay2.info) and SoSanh(cay1.left, cay2.left) and SoSanh(cay1.right, cay2.right)

# Hàm tiện ích để in cây theo thứ tự in-order (duyệt trung thứ tự) để kiểm tra kết quả sao chép
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.info, end=' ')
        inorder_traversal(root.right)

# Ví dụ sử dụng
if __name__ == "__main__":
    # Tạo một cây nhị phân mẫu
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    # Tạo một cây nhị phân khác giống hệt cây trên
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)

    # Tạo một cây nhị phân khác
    root3 = Node(1)
    root3.left = Node(2)
    root3.right = Node(3)
    root3.left.left = Node(4)

    # Kiểm tra xem hai cây có giống hệt nhau không
    print("So sánh root1 và root2: ", SoSanh(root1, root2))  # Kết quả mong đợi: True
    print("So sánh root1 và root3: ", SoSanh(root1, root3))  # Kết quả mong đợi: False
