from node import Node

class SinglyListSingle:

    POSITION = 1
    DATA = 2

    def __init__(self, node = None):
        self.__node = node

    def load_node(self, init, end):
        node = None
        for count in range(init, end):
            node = Node(count, node)
        self.__node = node

    def __str__(self):
        probe = self.__node
        ret = ""
        if not probe is None:
            position = 1
            while not probe is None:
                ret += f'Posición {position} dato {probe.data}\n\r'
                position += 1
                probe = probe.next
        return ret

    #Agregamos nodos en cualquier posición permitida
    def add(self, position, node):
        if self.__node is None:
            self.__node = node
        elif position <= 0:
            #Se registra al principio
            node.next = self.__node
            self.__node = node
        else:
            try:
                #Obtenemos el nodo en la posición previa a donde insertar
                find_previous_node_position = self.__find_by_position(position - 1)
                assert not find_previous_node_position is None, f'The position {position} is not allowed'
                #Al nuevo nodo le agregamos el siguiente nodo del nodo encontrado, si tiene dato, es decir, no es el último
                node.next = find_previous_node_position.next.next if find_previous_node_position.next != None else None
                #El nodo encontrado, en la posición siguiente, le agregamos el nodo
                find_previous_node_position.next = node
            except AssertionError as ae:
                print(ae)

    def __find_by_position(self, position):
        node_ret = self.__node
        item = 1
        while node_ret != None and item != position:
            node_ret = node_ret.next
            item += 1

        return node_ret

    def __find_by_data(self, data):
        node_ret = self.__node
        while node_ret != None and node_ret.data != data:
            node_ret = node_ret.next
        return node_ret

    def __find_position_by_data(self, data):
        position_ret = 1
        node = self.__node
        while node != None and node.data != data:
            position_ret += 1
            node = node.next
        return position_ret

    def update(self, by, search, data):
        try:
            assert by in (self.POSITION, self.DATA), f'{by} no es un tipo de dato mi_singlylistlinked_simple.mi_singlylistlinked_simple_by'
            if by == self.POSITION:
                node = self.__find_by_position(search)
            if by == self.DATA:
                node = self.__find_by_data(search)
            assert not node is None, f'The node {search} not found'
            node.data = data
        except AssertionError as ae:
            print(ae)


    def remove(self, by, search):
        try:
            assert by in (self.POSITION, self.DATA), f'{by} no es un tipo de dato mi_singlylistlinked_simple.mi_singlylistlinked_simple_by'
            if by == self.POSITION:
                #Si es el primer nodo
                if search == 1:
                    #Movemos una posición
                    self.__node = self.__node.next
                    return True
                #Buscamos el nodo en la posición
                node = self.__find_by_position(search - 1)
            if by == self.DATA:
                #Obtenemos la posición del dato del nodo y llamamos a la misma función
                return self.remove(self.POSITION, self.__find_position_by_data(search))

            assert not node is None, f'The node {search} not found'
            node.next = node.next.next
            return True
        except AssertionError as ae:
            print(ae)
            return False
    