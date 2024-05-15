class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def rut_gon(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                temp_data = current.data + current.next.data 
                temp_next_next = current.next.next 
                current.data, current.next = temp_data, temp_next_next
            else: 
                current = current.next

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

# Ví dụ sử dụng LinkedList với phương thức rut_gon.
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(2)
llist.append(3)
llist.rut_gon()
llist.print_list() # Kết quả sẽ in ra: 1 4 3 vì nó kết hợp các nút liền kề có giá trị giống nhau.
