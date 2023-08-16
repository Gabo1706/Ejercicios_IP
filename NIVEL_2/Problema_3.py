#NOMBRE DEL PROBLEMA: MOVIMIENTO ROBÓTICO
def movimiento_robot(orientacion_actual:str,giro:str)->str:
    if orientacion_actual=="N":
        angulo_orientacion=0
    elif orientacion_actual=="E":
        angulo_orientacion=270
    elif orientacion_actual=="W":
        angulo_orientacion=90
    else:
        angulo_orientacion=180
    if giro=="L":
        angulo_orientacion+=90
    elif giro=="R":
        angulo_orientacion-=90
    elif giro=="H":
        angulo_orientacion-=180
    elif giro==".":
        angulo_orientacion=angulo_orientacion
        
    if angulo_orientacion==90 :
        respuesta="W"
    elif angulo_orientacion==0 or angulo_orientacion==360:
        respuesta="N"
    elif angulo_orientacion==270 or angulo_orientacion==-90:
        respuesta="E"
    elif angulo_orientacion==180 or angulo_orientacion==-180:
        respuesta="S"
    return respuesta

print(movimiento_robot("N","H"))