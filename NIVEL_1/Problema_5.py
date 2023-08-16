#NOMBRE DEL PROBLEMA:CENTRAR TEXTO EN EL TERMINAL

def centrar_texto(cadena:str,ancho_terminal:int)->str:
    cantidad_caracteres=len(cadena)
    espacio_restante=ancho_terminal-cantidad_caracteres
    espacio_inicial=espacio_restante//2
    respuesta=" "*espacio_inicial+cadena
    return respuesta

print(centrar_texto("Gabriel",20))