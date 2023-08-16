#NOMBRE PROBLEMA: CARACTERES A ENTEROS

def caracteres_a_entero(centenas:str,decenas:str,unidades:str)->int:
    resultado=(int(centenas)*100)+(int(decenas)*10)+(int(unidades))
    return resultado
