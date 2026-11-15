from inventario import registrar_producto, mostrar_inventario
inventario = []
nombre_producto = input ("ingrese el nombre del producto:").strip()
while nombre_producto == "":
            print("el nombre del producto no puede estar vacio")
            nombre_producto = input ("ingrese el nombre del producto:").strip()
stock = int(input("ingrese el stock del producto:"))
while stock <= 0:
            print("el stock no puede ser negativo")
            stock = int (input("ingrese el stock del producto:"))
stock_minimo = int(input ("ingrese el stock minimo del producto:"))
while stock_minimo < 0:
            print ("el stock minimo no puede ser negativo")
            stock_minimo = int (input ("ingrese el stock minimo del producto:"))

agregar_producto = registrar_producto (inventario, nombre_producto, stock, stock_minimo)
mostrar_inventario(inventario)

continuar = True
while continuar:
    respuesta = input("desea agregar otro producto? (si/no):")
    if respuesta.lower().strip() == "si":
        nombre_producto = input ("ingrese el nombre del producto:").strip()
        while nombre_producto == "":
            print("el nombre del producto no puede estar vacio")
            nombre_producto = input ("ingrese el nombre del producto:").strip()
        stock = int (input("ingrese el stock del producto:")) 
        while stock <= 0:
            print("el stock no puede ser negativo")
            stock = int (input("ingrese el stock del producto:"))
        stock_minimo = int (input ("ingrese el stock minimo del producto:"))
        while stock_minimo < 0:
            print ("el stock minimo no puede ser negativo")
            stock_minimo = int (input ("ingrese el stock minimo del producto:"))
        agregar_producto = registrar_producto (inventario, nombre_producto, stock, stock_minimo)
        mostrar_inventario (inventario)
    else:
        continuar = False
        print("los productos fueron registrados correctamente")
        print (f"el inventario hace un total de {len(inventario)} de productos registrados")
