#NOMBRE PROBLEMA: COSTO DE HERVIR AGUA
def costo_hervir_agua(masa_agua:float)->float:
    cantidad_energia=masa_agua*4.186*80
    cantidad_watts=cantidad_energia/3600
    cantidad_kilowatts=cantidad_watts/1000
    costo=cantidad_kilowatts*0.089
    return round(costo,4)

print(costo_hervir_agua(300))