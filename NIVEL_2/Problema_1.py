#NOMBRE DEEL PROBLEMA: AÑO BISIESTO
def bisiesto(anio:int)->bool:
    respuesta=False
    if anio%4==0:
        if anio%100!=0:
            respuesta=True
        if anio%100==0 and anio%400!=0:
            respuesta=False
        if anio%100==0 and anio%400==0:
            respuesta=True
    return respuesta

print(bisiesto(1500))

