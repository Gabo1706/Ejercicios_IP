#NOMBRE PROBLEMA: EDAD DE UNA PERSONA
def calcular_edad(dia_nacio:int,mes_nacio:int,anio_nacio:int,dia_actual:int,mes_actual:int,anio_actual:int)->str:
    total_dias_nacio=((anio_nacio-1)*360)+((mes_nacio-1)*30)+dia_nacio
    total_dias_actual=((anio_actual-1)*360)+((mes_actual-1)*30)+dia_actual
    diferencia_dias=total_dias_actual-total_dias_nacio
    cantidad_anios=diferencia_dias//360
    cantidad_meses=(diferencia_dias%360)//30
    cantidad_dias=(diferencia_dias%360)%30
    respuesta=f"{cantidad_anios},{cantidad_meses},{cantidad_dias}"
    return(respuesta)

print(type(calcular_edad(20,11,1986,16,10,1987)))
