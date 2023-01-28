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
            print(f'[{current_node.value}]',end='->')
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
            prev = current_node
            current_node = current_node.next
        
        if current_node:
            prev.next = current_node.next
            current_node = None
            return
        else:
            print(f'Node at pos {pos} not found')

    def reverse(self):
        current_node = self.head
        prev = None

        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        self.head = prev

    def __len__(self):
        count = 0
        if self.head is None:
            return count
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next 
        return count

    def merge(self, second_linked_list):
        p1 = self.head
        p2 = second_linked_list

        if not p1:
            return p2
        if not p2:
            return p1
        
        if p1 and p2:
            if p1.data <= p2.data:
                smallest_number = p1
                p1 = smallest_number.next
            else:
                smallest_number = p2
                p2 = smallest_number.next
            new_head = smallest_number
        
        while p1 and p2:
            if p1.data <= p2.data:
                smallest_number.next = p1
                smallest_number = p1
                p1 = smallest_number.next
            else:
                smallest_number.next = p2
                smallest_number = p2
                p2 = smallest_number.next
        self.head = new_head
