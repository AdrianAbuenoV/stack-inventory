nombre_producto = input ("inserte el nombre de el producto:")
stock = int (input ("introduce la cantidad del producto:"))
stock_minimo = int (input ("introduce la cantidad minima de producto:"))
print (f"producto registrado {nombre_producto}, con un stock de {stock} y sus unidades minimas son {stock_minimo}")
producto = {
    "nombre": nombre_producto,
    "stock": stock,
    "stock_minimo": stock_minimo
}
inventario = []
inventario.append(producto)
len (inventario)
print (f"productos agregados:{len (inventario)}")
continuar = True
while continuar:
    respuesta = input ('desea agregar otro prodcto?: ')
    if respuesta.lower() == 'si' or respuesta.lower() =="sí":
        nombre_producto = input ("inserte el nombre de el producto:")
        stock = int(input ("introduce la cantidad del producto = "))
        stock_minimo = int(input ("introduce la cantidad minima del producto:"))
        print (f"producto registrado {nombre_producto}, con un stock de {stock} y sus unidades minimas son {stock_minimo}")
        producto = {
            "nombre": nombre_producto,
            "stock": stock,
            "stock_minimo": stock_minimo
        }
        inventario.append(producto)
        print ( f"productos agregados: {len (inventario)}")
    else:
        continuar = False