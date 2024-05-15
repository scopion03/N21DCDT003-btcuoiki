class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def isBalancedAndCountNodes(root):
    if root is None:
        return (0, True)

    left_count, left_balanced = isBalancedAndCountNodes(root.left)
    right_count, right_balanced = isBalancedAndCountNodes(root.right)

    # Tổng số nút là tổng số nút của cây con bên trái và bên phải cộng với 1 (nút hiện tại)
    total_count = 1 + left_count + right_count

    # Kiểm tra xem cây con hiện tại có cân bằng không
    if abs(left_count - right_count) > 1:
        return (total_count, False)

    # Cây con hiện tại cân bằng nếu cả hai cây con bên trái và bên phải đều cân bằng
    return (total_count, left_balanced and right_balanced)

def CanBangHoanToan(root):
    _, is_balanced = isBalancedAndCountNodes(root)
    return is_balanced

# Hàm tiện ích để in cây theo thứ tự in-order (duyệt trung thứ tự) để kiểm tra kết quả
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.info, end=' ')
        inorder_traversal(root.right)

# Ví dụ sử dụng
if __name__ == "__main__":
    # Tạo một cây nhị phân mẫu cân bằng hoàn toàn
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.left = Node(6)
    root1.right.right = Node(7)

    # Tạo một cây nhị phân không cân bằng
    root2 = Node(1)
    root2.left = Node(2)
    root2.left.left = Node(3)

    # Kiểm tra xem cây có cân bằng hoàn toàn hay không
    print("Cây root1 có cân bằng hoàn toàn không:", CanBangHoanToan(root1))  # Kết quả mong đợi: True
    print("Cây root2 có cân bằng hoàn toàn không:", CanBangHoanToan(root2))  # Kết quả mong đợi: False
