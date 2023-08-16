#NOMBRE DEL PROBLEMA: AREA DE UN POLIGONO REGULAR
import math
def area_poligono_regular(num_lados:int,longitud:float)->float:
    area=round((num_lados*longitud**2)/(4*math.tan(math.pi/num_lados)),2)
    return area


    