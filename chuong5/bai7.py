class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def copy_tree(root):
    # Nếu cây gốc rỗng, trả về None
    if root is None:
        return None

    # Tạo một nút mới với cùng giá trị info
    new_node = Node(root.info)

    # Sao chép nút con bên trái và gán vào new_node.left
    new_node.left = copy_tree(root.left)

    # Sao chép nút con bên phải và gán vào new_node.right
    new_node.right = copy_tree(root.right)

    return new_node

# Hàm tiện ích để in cây theo thứ tự in-order (duyệt trung thứ tự) để kiểm tra kết quả sao chép
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.info, end=' ')
        inorder_traversal(root.right)

# Ví dụ sử dụng
if __name__ == "__main__":
    # Tạo một cây nhị phân mẫu
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Cây gốc:")
    inorder_traversal(root)
    print()

    # Sao chép cây
    copied_tree = copy_tree(root)

    print("Cây sao chép:")
    inorder_traversal(copied_tree)
    print()
