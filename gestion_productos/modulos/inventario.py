def agregar_producto(inventario, nombre, cantidad, precio):
    if nombre in inventario:
        inventario[nombre]['cantidad'] += cantidad
    else:
        inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
    return f"Producto '{nombre}' procesado con éxito."

def eliminar_producto(inventario, nombre):
    if nombre in inventario:
        del inventario[nombre]
        return f"'{nombre}' ha sido eliminado."
    return "Error: El producto no existe."

def mostrar_inventario(inventario):
    if not inventario:
        return "El inventario está vacío."
    
    reporte = "\n--- Inventario Actual ---\n"
    for nombre, info in inventario.items():
        reporte += f"Producto: {nombre:15} | Stock: {info['cantidad']:5} | Precio: ${info['precio']:.2f}\n"
    return reporte