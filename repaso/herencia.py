# Definimos una clase padre
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie;
        self.edad = edad;
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        pass
    # Método genérico con la misma implementación
    def getNombre(self):
        print(f'');
        return self.especie;

# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    def __init__(self,especie, edad, tamano):
        super().__init__(especie, edad)
        self.tamano = tamano
        self.sonido = None
        
    def ladrar(self):
        print('ladrando', self.sonido)
        return self._sonido
    
    def setladrar(self, sonido):
        self.sonido = sonido

    def print_perro(self):
        #print(self.especie, self.edad, self.tamano);
        if(self.sonido == None):
            self.sonido = ''
        return(self.especie, self.edad, self.tamano, self.sonido);
        

perro1 = Perro('schnauzer','11','estandar');
#perro1.setladrar('wow');

print(perro1.print_perro())
print(perro1.getNombre())
