#NOMBRE DEL PROBLEMA: POKEMONES
"""pokemon_1={"ataque":100,"defensa":80,"ataque_especial":120,"defensa_especial":90,"velocidad":110,"vida":100}
pokemon_2={"ataque":110,"defensa":90,"ataque_especial":90,"defensa_especial":80,"velocidad":100,"vida":100}
pokemon_3={"ataque":120,"defensa":100,"ataque_especial":100,"defensa_especial":90,"velocidad":110,"vida":100}
pokemon_4={"ataque":90,"defensa":70,"ataque_especial":120,"defensa_especial":100,"velocidad":120,"vida":100}"""
pokemon_1={"nombre":"poke1","ataque":100,"defensa":80,"ataque_especial":120,"defensa_especial":90,"velocidad":110,"vida":100}
pokemon_2={"nombre":"poke2","ataque":110,"defensa":90,"ataque_especial":90,"defensa_especial":80,"velocidad":100,"vida":100}
pokemon_3={"nombre":"poke3","ataque":120,"defensa":100,"ataque_especial":100,"defensa_especial":90,"velocidad":110,"vida":100}
pokemon_4={"nombre":"poke4","ataque":90,"defensa":70,"ataque_especial":120,"defensa_especial":100,"velocidad":120,"vida":100}
pokemones=[pokemon_1,pokemon_2,pokemon_3,pokemon_4]
def construir_equipo_pokemon(cantidad:int,lista_pkmn:list)->list:
    cantidad_comparacion=0
    equipo=[]
    for pokemon in lista_pkmn:
        sumatoria=0
        for caracteristicas in pokemon.items():
            if type(caracteristicas[1]) is str:
                sumatoria=sumatoria
            else:
                sumatoria=sumatoria+caracteristicas[1]
        if sumatoria>=600:
            cantidad_comparacion+=1
            equipo.append(pokemon["nombre"])
        if cantidad_comparacion==cantidad:
            return equipo
    if cantidad_comparacion<cantidad:
        return None

print(construir_equipo_pokemon(2,pokemones))
            
            
            
