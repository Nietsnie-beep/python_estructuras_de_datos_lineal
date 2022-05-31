# estructuras de datos lineales python

Tags: No

### Nodes y singly linked list

Las estructuras linked consisten en nodos conectados a otros, los más comunes son sencillos o dobles. No se accede por índice sino por recorrido. Es decir se busca en la lista de nodos hasta encontrar un valor.

- **Data**: Será el valor albergado en un nodo.
- **Next**: Es la referencia al siguiente nodo en la lista
- **Previous**: Será el nodo anterior.
- **Head**: Hace referencia al primer nodo en la lista
- **Tail**: Hace referencia al último nodo.

---

**¿Cómo funciona en memoria los Linked Estructures?**

Estas estructuras de datos hablan de `nodos/datos` repartidos en memoria, diferentes a los arrays que son contiguos. Los nodos se conectan a diferentes espacios en memoria, podemos acceder a los datos saltando en memoria, siendo mucho más ágil. Los nodos nos sirven para crear otras estructuras más complejas, como **Stacks, Queues**, las llamadas pilas y colas. Es posible optimizar partes del código usando nodos.

---

### **Double Linked Structure**.

Estos hacen que el nodo haga referencia al siguiente nodo y al anterior, es decir nos va a permitir ir en ambas direcciones. También nos permitirá realizar “formas” y contextos circulares.

- El ejemplo clave aquí será función de `ctrl+z` y `ctrl+y` Estas opciones nos permiten hacer y deshacer un proceso en Windows.
- El historial del navegador también es un buen ejemplo al permitirnos navegar entre el pasado y el presente.

## Pilas (Stacks)

Las pilas (stacks) son una estructura de datos donde tenemos una colección de elementos, y sólo podemos hacer dos cosas:

- añadir un elemento al final de la pila
- sacar el último elemento de la pila

Una manera común de visualizar una pila es imaginando una torre de panqueques, donde una vez que ponemos un panqueque encima de otro, no podemos sacar el anterior hasta que se hayan sacado todos los que están encima.

![https://miro.medium.com/max/700/1*qcjbuSJ4rf7VcFFFoDbc5Q.png](https://miro.medium.com/max/700/1*qcjbuSJ4rf7VcFFFoDbc5Q.png)

A pesar de su simplicidad, las pilas son estructuras relativamente comunes en ciertas áreas de la computación, en especial para implementar o simular evaluación de expresiones, recursión, scope, …

## LIFO (Last In First Out)

Las pilas son estructuras de tipo LIFO, lo cual quiere decir que el último elemento añadido es siempre el primero en salir.

De alguna forma, podemos decir que una pila es como si fuera una lista o array, en el sentido que es una colección, pero a diferencia de los arrays y otras colecciones, en las pilas solo accedemos al elemento que esté “encima de la pila”, el último elemento. Nunca manipulamos ni accedemos a valores por debajo del último elemento.

## Recomendaciones

+linked list = +complejo

cuantos hay en un stack? > true = usar array

pocos elementos nodos

queue

fifo