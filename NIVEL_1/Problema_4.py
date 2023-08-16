#NOMBRE DEL PROBLEMA: CAMBIO A RETORNAR

def calcular_cambio(cambio:int)->str:
    monedas=[500,200,100,50]
    cantidad_monedas=[0,0,0,0]
    i=0
    while cambio>0 and i<=len(monedas)-1:
        cantidad_monedas[i]=(cambio//monedas[i])
        cambio=cambio-(cantidad_monedas[i]*monedas[i])
        i=i+1
    a,b,c,d=cantidad_monedas
    respuesta=f"{a},{b},{c},{d}"
    return respuesta

print(calcular_cambio(50))
    
