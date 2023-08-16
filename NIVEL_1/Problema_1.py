#NOMBRE PROBLEMA: ALTURA DE UNA PERSONA

def altura_en_mts(pies:int,pulgadas:int)->float:
    pies_a_pulgadas=pies*12
    pulgadas_totales=pulgadas+pies_a_pulgadas
    metros=round((pulgadas_totales*2.54)/100,2)
    return metros
print(altura_en_mts(6.4,2))

