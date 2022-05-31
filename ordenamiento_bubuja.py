def orden(lista):
     for n in range(len(lista) -1, 0, -1):#hasta el 0 con pasos de -1
         for i in range(n):
             if lista[i] > lista[i + 1]:
                 temp = lista[i]
                 lista[i] = lista[i + 1]
                 lista[i + 1] = temp

numeros = [12,5,10,1,4,2]
print (numeros)
orden(numeros)
print(numeros)