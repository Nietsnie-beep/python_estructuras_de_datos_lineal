import random 

def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1): #tamano de la lista menos lo que ya recorrimos - 1 de la longitud

            if lista[j] > lista[j + 1]:
                #intercambiamos (swapping)
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('de que tamano sera la lista? '))

    lista = [random.randint(0,1000) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(f'aqui comienza la lista ordenada {lista_ordenada}  aqui termina la lista ordenada')