import modulos.inventario as inv

def menu():
    mi_inventario = {}  
    
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE PRODUCTOS ---")
        print("1. Agregar/Actualizar producto")
        print("2. Ver inventario")
        print("3. Eliminar producto")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ").strip().capitalize()
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                mensaje = inv.agregar_producto(mi_inventario, nombre, cantidad, precio)
                print(mensaje)
            except ValueError:
                print("Error: Cantidad y precio deben ser numéricos.")

        elif opcion == '2':
            print(inv.mostrar_inventario(mi_inventario))

        elif opcion == '3':
            nombre = input("Nombre del producto a eliminar: ").strip().capitalize()
            print(inv.eliminar_producto(mi_inventario, nombre))

        elif opcion == '4':
            print("Saliendo del sistema... ¡Hasta pronto!")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()