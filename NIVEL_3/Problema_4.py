#COSTO TOTAL CARRITO DE COMPRAS
carrito_compras={"leche":2400,"huevos":4000,"pan":5000}
carrito_compras1={}
def valor_carrito_compras(carrito_compras:dict)->float:
    respuesta=0
    if carrito_compras=={}:
        return respuesta
    for productos in carrito_compras.items():
        respuesta=respuesta+productos[1]
    return respuesta
print(valor_carrito_compras(carrito_compras1))