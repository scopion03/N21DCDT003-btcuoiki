class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def isIdentical(root1, root2):
    # Nếu cả hai cây đều rỗng, chúng giống hệt nhau
    if root1 is None and root2 is None:
        return True
    
    # Nếu một trong hai cây rỗng, chúng không giống nhau
    if root1 is None or root2 is None:
        return False
    
    # Kiểm tra giá trị của nút hiện tại và đệ quy kiểm tra các nút con bên trái và bên phải
    return (root1.info == root2.info) and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)

def CayCon(root1, root2):
    # Nếu cây con (root2) là rỗng, luôn là cây con của bất kỳ cây nào
    if root2 is None:
        return True
    
    # Nếu cây cha (root1) là rỗng, cây con (root2) không thể là cây con
    if root1 is None:
        return False
    
    # Kiểm tra nếu cây bắt đầu từ nút hiện tại của root1 giống với root2
    if isIdentical(root1, root2):
        return True
    
    # Kiểm tra tiếp ở các nút con của root1
    return CayCon(root1.left, root2) or CayCon(root1.right, root2)

# Ví dụ sử dụng
if __name__ == "__main__":
    # Tạo một cây nhị phân mẫu
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.left = Node(6)
    root1.right.right = Node(7)

    # Tạo một cây nhị phân khác
    root2 = Node(2)
    root2.left = Node(4)
    root2.right = Node(5)

    # Tạo một cây nhị phân khác
    root3 = Node(3)
    root3.left = Node(6)
    root3.right = Node(8)

    # Kiểm tra xem root2 có phải là cây con của root1 không
    print("root2 có phải là cây con của root1 không:", CayCon(root1, root2))  # Kết quả mong đợi: True
    print("root3 có phải là cây con của root1 không:", CayCon(root1, root3))  # Kết quả mong đợi: False
