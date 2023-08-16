#CONTAR CARACTERES REPETIDOS
def contar_caracteres_repetidos(cadena:str)->int:
    acumulativo=0
    for contador in range(len(cadena)):
        for contador2 in range(len(cadena)):
            if contador2<=contador:
                contador2+=1
            elif cadena[contador2]==" ":
                contador2+=1
            elif cadena[contador]==cadena[contador2]:
                acumulativo+=1
                cadena=cadena.replace(cadena[contador2]," ")
    return acumulativo
print(contar_caracteres_repetidos("g"))
            