from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        new_node.next = current_node
        self.head = new_node

    def print_list(self):
        if self.head is None:
            print('Empty List')
            return
        
        print("######Priting Linked List#######")
        
        current_node = self.head
        while current_node:
            print(current_node.value,end='->')
            current_node = current_node.next
        
        print("None")

    def delete_by_value(self, value):
        if self.head is None:
            print('No delete action on empty List')
            return
        
        current_node = self.head
        prev = None
        
        if current_node.value == value:
            self.head = current_node.next
            current_node = None
            return
        
        while current_node and current_node.value != value:
            prev = current_node
            current_node = current_node.next

        if current_node:
            prev.next = current_node.next
            current_node = None
            return
        else:
            print(f'Node with value {value} not found')

    def delete_by_pos(self, pos):
        if self.head is None:
            print('No delete action on empty List')
            return
        
        current_node = self.head
        prev = None
        count = 0

        if pos == count:
            self.head = current_node.next
            current_node = None
            return
        
        while current_node and count != pos:
            count += 1
            current_node = current_node.next
        
        if current_node:
            prev.next = current_node.next
            current_node = None
            return
        else:
            print(f'Node at pos {pos} not found')