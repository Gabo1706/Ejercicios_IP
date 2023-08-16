#NOMBRE DEEL PROBLEMA:ÁREA DE UN TRIÁNGULO

import math
def area_triangulo(s1:float,s2:float,s3:float)->float:
    s=(s1+s2+s3)/2
    area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    return round(area,1)