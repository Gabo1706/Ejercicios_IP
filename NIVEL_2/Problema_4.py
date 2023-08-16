#NOMBRE DEL PROBLEMA: CARTAS
carta_mano={'numero':"A",'palo':'corazones'}
opcion_1={'numero':"J",'palo':'corazon'}
opcion_2={'numero':"A",'palo':'corazoes'}
def cambio_de_cartas(carta_mano:dict,opcion_1:dict,opcion_2:dict)->int:
    cambio=0
    if carta_mano["numero"]==opcion_1["numero"] or carta_mano["palo"]==opcion_1["palo"]:
        cambio=1
        return cambio
    if carta_mano["numero"]==opcion_2["numero"] or carta_mano["palo"]==opcion_2["palo"]:
        cambio=2
        return cambio
    return cambio

print(cambio_de_cartas(carta_mano,opcion_1,opcion_2))