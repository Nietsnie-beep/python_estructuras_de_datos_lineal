from operacionesLinkedList import SinglyListSingle 
from node import Node

def run():
    linked_list = SinglyListSingle()
    linked_list.load_node(1, 6)
    print(linked_list)
    linked_list.add(3, Node('W'))
    print(linked_list)
    linked_list.add(6, Node('Z'))
    print(linked_list)
    linked_list.add(9, Node('CX'))
    print(linked_list)
    linked_list.update(SinglyListSingle.POSITION, 5, 'Actualizar')
    print(linked_list)
    linked_list.update(SinglyListSingle.DATA, 'Actualizar', 'Nuevamente actualziado')
    print(linked_list)

if __name__ == '__main__':
    run()