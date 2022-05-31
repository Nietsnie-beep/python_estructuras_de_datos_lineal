class Circle:
    def __init__(self, radio):
        self.radio = radio
        
    def diametro(self):
        return 2 * self.radio
    

class Cilindro(Circle):
    def __init__(self, altura):
        # super().__init__(radio)
        self.altura = altura;
    
    def area(self, diametro):
        return diametro * self.altura

circulo = Circle(2)
print(f'Diametro circulo {circulo.diametro()}')

cilindro = Cilindro(2)

#area de cilindro
print(f'Area de cilindro {cilindro.area(circulo.diametro())}')