from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0 #puede crecer
        
    def push(self, data):
        node = Node(data)
        
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
            
        self.size += 1
    
    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            
            if self.top.next:
                self.top = self.top.next
            
            else:
                self.top = None
                
            return data
        
        else: #stack vacio
            return 'stack esta vacio'
        
    #conocer el elemento de top
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "Stack esta vacio"
        
    def clear(self):
        while self.top:
            self.pop()
            
    #reto 2
    def search(self,data):
        top = self.top
        while top != None and data != top.data:
            top = top.next
            
        if top != None:
            return True
        else:
            return False
        
    #yield crea objetos sin guardarlos en la memoria
    def iteracion(self):
        current = self.top;
        
        while current:
            val = current.data
            current = current.next
            yield val