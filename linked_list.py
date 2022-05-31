
from node import Node

class SinglyLinkedList():
    def __init__(self):
        self.tail = None
        self.size = 0
   
    def append(self, data):

        node = Node(data)

        if self.tail == None:
            self.tail = node
            
        else:
            current = self.tail #current == actual

            while current.next:
                current = current.next

            current.next = node
        
        self.size += 1
    
    def add(self):
        #* Agregar un nuevo elemento/nodo por "indice" inverso(Cuenta de Head - Tail)
        new_item = input("Enter new item: ")
        index = int(input("Enter the position to insert the new item: "))
    
        head = self.tail
        
        if head is None or index <= 0:
            head = Node(new_item, head)
        else:
            probe = head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            probe.next = Node(new_item, probe.next)
                        
    def sizer(self):
        return str(self.size)

    def iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
            
                else:
                    previous.next = current.next
                    self.size -=1
                    return current.data

            previous =  current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f'data {data} found!')

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0
        




