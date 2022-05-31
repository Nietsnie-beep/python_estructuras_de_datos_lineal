lista = [0,80,72,21,14,16,90,35,47,6,68,12,10,54]
lista.sort()

print(lista)

def busqueda_binaria(valor):
    inicio = 0;
    final = len(lista) - 1
    
    while inicio <= final:
        puntero = (inicio + final) // 2
        if valor == lista[puntero]:
            return puntero
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            final = puntero -1
        
    return None

def busqueda_valor(valor):
    res_busqueda = busqueda_binaria(valor)
    if res_busqueda is None:
        return(f'El numero {valor} no se encontro')
    else: 
        return(f'El numero {valor} se encontra en la posicion {res_busqueda}')

print(busqueda_valor(72))