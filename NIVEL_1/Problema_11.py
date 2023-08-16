#NOMBRE PROBLEMA: DISTANCIA ENTRE DOS PUNTOS DE LA TIERRA
import math
def calcular_distancia_tierra(t1:float,g1:float,t2:float,g2:float)->float:
    d=6371.01*math.acos((math.sin(math.radians(t1))*math.sin(math.radians(t2)))+(math.cos(math.radians(t1))*math.cos(math.radians(t2))*math.cos(math.radians(g1-g2))))
    return round(d,2)   

print(calcular_distancia_tierra(24.5,67.7,23.8,98.7))
 