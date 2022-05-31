num_tarjeta = int(input('Numero de tarjeta\n'))
nombre = str(input('Nombre completo\n'))
fecha = int(input('Fecha de vencimiento\n'))
tasa_int = int(input('Ingrese la tasa de interes:\n'))
deuda = int(input('Ingrese la deuda\n'))
pago_rea = int(input('Cantidad del pago a realizar:\n'))
nuevo_cargo = 0

datos = {}
datos['tarjetas'] = []

def data():

    tarjeta = {
        'Nombre':nombre, 'Numero de tarjeta':num_tarjeta,
                            'fecha de vencimiento':fecha,
                            'Tasa de interes':tasa_int, 'Deuda actual':deuda,
                            'Pago a realizar' : pago_rea     
            }

    datos['tarjetas'].append(tarjeta);
    
    

def captura_nueva_deuda(nuevo_cargo, datos):
    interes_men = datos['Tasa de interes']/12
    deuda_rec = (datos['Deuda actual']-datos['Pago a realizar'])*(1+interes_men)
    nueva_deuda = deuda_rec + nuevo_cargo
    nuevo_cargo = nueva_deuda
    return nuevo_cargo

def generar_reporte():
    print(datos)


def crear_tarjeta():
    data();
    print(datos)
    

salida = int(input('numero '))

app= 1
while(app == 1):
    if(salida == 0):
        crear_tarjeta()
        print(datos)
          