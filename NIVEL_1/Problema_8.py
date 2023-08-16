#NOMBRE PROBLEMA: CAIDA LIBRE
import math
def vel_en_caida_libre(altura:float)->float:
    respuesta=math.sqrt(2*9.8*altura)
    return round(respuesta,2)

