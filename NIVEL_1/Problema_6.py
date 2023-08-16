#NOMBRE PROBLEMA:ÁNGULO ENTRER AGUJAS DEL RELOJ

def angulo_entre_agujas_reloj(hora:int,minutos:int)->float:
    recorrido_por_minuto=6
    recorrido_por_hora=30
    recorrido_entre_horas=0.5
    angulo_minutero=minutos*recorrido_por_minuto
    angulo_hora=(hora*recorrido_por_hora)+recorrido_entre_horas*minutos
    angulo=abs(round(angulo_minutero-angulo_hora,1))
    return angulo

print(angulo_entre_agujas_reloj(4,15))