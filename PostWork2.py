salida = 0
while(salida == 0):
    nombre = str(input('Nombre completo\n'))
    num_tarjeta = int(input('Numero de tarjeta\n'))
    fecha = int(input('Fecha de vencimiento\n'))
    tasa_int = int(input('Ingrese la tasa de interes:\n'))
    deuda = int(input('Ingrese la deuda\n'))
    pago_rea = int(input('Cantidad del pago a realizar:\n'))
    nuevo_cargo = 0

    if (pago_rea > deuda):
            print('No se puede realizar esta operación')
            print('///////////////////////////////////')
    else:
        def crear_tarjeta():
            datos = {'Nombre':nombre, 'Numero de tarjeta':num_tarjeta, 
                     'fecha de vencimiento':fecha,
                     'Tasa de interes':tasa_int, 'Deuda actual':deuda, 
                     'Pago a realizar' : pago_rea}
            
            def captura_nueva_deuda(nuevo_cargo, datos):
                interes_men = datos['Tasa de interes']/12
                deuda_rec = (datos['Deuda actual']-datos['Pago a realizar'])*(1+interes_men)
                nueva_deuda = deuda_rec + nuevo_cargo
                nuevo_cargo = nueva_deuda
                return nuevo_cargo

            datos['Nuevo cargo'] = captura_nueva_deuda(nuevo_cargo, datos)
            return datos

        def generar_reporte():
            lista_trjetas = []

        def pago_recurrente():
            print()

        print('\n')
        print('Esto es crear tarjeta')
        print(crear_tarjeta())
        
        salida = 1
