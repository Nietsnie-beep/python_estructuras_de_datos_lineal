>>> from list_based_queue import ListaQueue
>>> food = ListQueue()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ListQueue' is not defined
>>> food = ListaQueue()
>>> food.push('egg')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'ListaQueue' object has no attribute 'push'
>>> food.push('ham')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'ListaQueue' object has no attribute 'push'
>>> food.enqueue('eggs') 
>>> food.enqueue('ham')  
>>> food.enqueue('spam') 
>>> 
>>> food.dequeue()       
'eggs'
>>> food.traverse()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\Users\OMEN\Desktop\platzi\python-estructuras-de-datos\list_based_queue.py", line 19, in traverse
    for item in total_items:
TypeError: 'int' object is not iterable
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>> exit()
(envplatzipython) PS D:\Users\OMEN\Desktop\platzi\python-estructuras-de-datos> python
Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from list_based_queue import ListaQueue
>>> food = ListQueue()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ListQueue' is not defined
>>> food = ListaQueue() 
>>> food.push('egg')    
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'ListaQueue' object has no attribute 'push'
>>> food.enqueue('eggs') 
>>> food.enqueue('ham')  
>>> food.enqueue('spam') 
>>> food.dequeue()       
'eggs'
>>> food.traverse()
spam
ham
>>>



# * Agregar un nuevo elemento/nodo por "indice" inverso(Cuenta de Head - Tail)
# new_item = input("Enter new item: ")
# index = int(input("Enter the position to insert the new item: "))
new_item = "10"
index = 3

if head is None or index <= 0:
    head = Node(new_item, head)
else:
    probe = head
    while index > 1 and probe.next != None:
        probe = probe.next
        index -= 1
    probe.next = Node(new_item, probe.next)
