
from linked_list import SinglyLinkedList
from node import Node

words = SinglyLinkedList()
words.append('egg')
words.append('milk')
words.append('ham')

current = words.tail
words.add()

while current:
    print(current.data)
    current = current.next
        
# for word in words.iter():
#     print(word)
