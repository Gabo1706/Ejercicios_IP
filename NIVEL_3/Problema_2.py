#NOMBRE DEL PROBLEMA: SUSECIÓN FIBONACCI
def sucesion_fibonacci(cantidad_numeros:int)->str:
    if cantidad_numeros==0 or cantidad_numeros==1:
        respuesta=[0]
    elif cantidad_numeros==2:
        respuesta=[0,1]
    else:
        respuesta=[0,1]
        while len(respuesta)<cantidad_numeros:
            siguiente_numero=respuesta[-1]+respuesta[-2]
            respuesta.append(siguiente_numero)
    respuesta=str(respuesta)
    respuesta=respuesta.replace("[","")
    respuesta=respuesta.replace("]","")
    respuesta=respuesta.replace(" ","",-1)
    return respuesta

print(sucesion_fibonacci(18))

        
    

    