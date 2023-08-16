#NOMBRE DEL PROBLEMA: BOLETAS DE CINE
def calcular_costo_boletas(cantidad_boletas=int,tipo_sala=str,hora_pico=bool,pago_tarjeta_cinema=bool,reserva=bool)->int:
    #PRECIO INICIAL
    Dinamix=18800
    tres_D=15500
    dos_D=11300
    if tipo_sala=="Dinamix":
        precio_inicial=Dinamix
    elif tipo_sala=="3D":
        precio_inicial=tres_D
    else:
        precio_inicial=dos_D
    #DESCUENTO POR HORA PICO
    if hora_pico==False:
        precio_inicial=precio_inicial*0.9
        if cantidad_boletas>=3:
            precio_inicial=precio_inicial-500
    #DESCUENTO POR TARJETA
    if pago_tarjeta_cinema==True:
        if tipo_sala=="Dinamix":
            precio_inicial=precio_inicial-(Dinamix*0.05)
        elif tipo_sala=="3D":
            precio_inicial=precio_inicial-(tres_D*0.05)
        else:
            precio_inicial=precio_inicial-(dos_D*0.05)
    #RECARGO POR RESERVA
    if reserva==True:
        precio_inicial=precio_inicial+2000
    #RECARGO HORA PICO
    if hora_pico==True:
        if tipo_sala=="Dinamix":
            precio_inicial=precio_inicial+Dinamix*0.5
        elif tipo_sala=="3D":
            precio_inicial=precio_inicial+tres_D*0.25                
        else:
            precio_inicial=precio_inicial+dos_D*0.25
    costo_a_pagar=precio_inicial*cantidad_boletas
    return round(costo_a_pagar)

print(calcular_costo_boletas(2,"Dinamix",False,False,False))
        
    
 
    