class Terrestre:
    def desplazar(self):
        print('El animal anda')

class Acuatico:
    def nadar(self):
        print('El animal nada')

class Cocodrilo(Terrestre, Acuatico):
    print('soy un cocodrilo')

c = Cocodrilo()
c.desplazar()
c.nadar()