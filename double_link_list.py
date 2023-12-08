class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self) -> bool:
        return self.head is None
        
            
    def prepend(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def append(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    
    def delete(self,data):
        current_node = self.head
        
        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
            
                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
            
                break
            current_node = current_node.next
    
    def insert_after(self,target_data,data):
        current_node = self.head
        while current_node:
            if current_node.data == target_data:
                new_node = Node(data)
                new_node.prev = current_node
                new_node.next = current_node.next
                if current_node.next:
                    current_node.next.prev = new_node
                current_node.next = new_node
                if current_node == self.tail:
                    self.tail = new_node
                break
            current_node = current_node.next
    
    def insert_before(self,target_data,data):
        current_node = self.head
        while current_node:
            if current_node.data == target_data:
                new_node = Node(data)
                new_node.next = current_node
                new_node.prev = current_node.prev
                if current_node.prev:
                    current_node.prev.next = new_node
                current_node.prev = new_node
                if current_node == self.head:
                    self.head = new_node
                break
            current_node = current_node.next
            
    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        print('Double linked list', elements)
        
        

linked_list = Doubly_Linked_List()

linked_list.prepend(5)
linked_list.append(4)
linked_list.display()
linked_list.prepend(10)
linked_list.display()
linked_list.insert_before(5,3)
linked_list.display()
linked_list.insert_after(10,9)
linked_list.display()
linked_list.delete(3)
linked_list.display()