head = None

class Node():
    def __init__(self,data, next=None): #el ultimo nodo no lleva a ningun lado
        
        self.data = data
        self.next = next

node1 = Node('c', None)
node2 = Node('A', node1)
node3 = Node('B', node2)

#create Nodes with numbers 1 to 5 in head(id)
for count in range(1,5):
    head = Node(count,head)

while head != None:
    print (head.data)
    head = head.next