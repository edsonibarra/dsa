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

    def print_list(self, value):
        if self.head is None:
            print('Empty List')
            return
        
        print("######Priting Linked List#######")
        
        current_node = self.head
        while current_node:
            print(current_node.value,end='->')
            current_node = current_node.next
        
        print("None")
