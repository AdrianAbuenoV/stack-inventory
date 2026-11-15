
def registrar_producto (inventario, nombre_producto, stock , stock_minimo):
    producto = {
        "nombre": nombre_producto,
        "stock": stock,
        "stock_minimo": stock_minimo
    }
    inventario.append(producto)
    return producto

def mostrar_inventario(inventario):
    for producto in inventario:
        print("nombre:", producto["nombre"])
        print('stock:', producto["stock"])
        print('stock minimo:', producto["stock_minimo"])
   