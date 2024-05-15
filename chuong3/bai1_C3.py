class Node:
    def __init__(self, heso, somu):
        self.heso = heso
        self.somu = somu
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def them_phan_tu(self, heso, somu):
        new_node = Node(heso, somu)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

# Sử dụng lớp LinkedList
danh_sach = LinkedList()
danh_sach.them_phan_tu(3, 2)
danh_sach.them_phan_tu(5, 1)
# Bạn có thể tiếp tục thêm các phần tử khác theo cùng cách
