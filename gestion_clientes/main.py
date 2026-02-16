from gestion import GestionClientes
from cliente import Cliente, ClientePremium, ClienteCorporativo
from utilidades import *



def pedir_datos_comunes():
    datos = {}
    print("\n--- INGRESE DATOS DEL CLIENTE ---")
    while True:
        try:
            nom = input("Ingrese Nombre: ")
            datos['nombre'] = validar_nombre(nom)
            break
        except ValueError as e:
            print(f"❌ {e}")     

    while True:
        try:
            correo = input("Email: ")
            datos['email'] = validar_email(correo)
            break
        except ValueError as e:
            print(f"❌ {e}")
    
    while True:
        try:
            tel = input("Teléfono: ")
            datos['telefono'] = validar_telefono(tel)
            break
        except ValueError as e:
            print(f"❌ {e}")

    while True:
        dir_cli = input("Dirección: ")
        if dir_cli.strip():
            datos['direccion'] = dir_cli
            break
        print("❌ La dirección no puede estar vacía.")
    
    while True:
        try:
            monto = input("Total de compra: ")
            datos['total_compra'] = validar_monto(monto)
            break
        except ValueError as e:
            print(f"❌ {e}")
    return datos

def main():
    sistema = GestionClientes()

    while True:
        print("\n" + "="*35)
        print("  SISTEMA DE GESTIÓN DE CLIENTES")
        print("="*35)
        print("1. Agregar Cliente")
        print("2. Listar todos los clientes")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\n--- ¿QUÉ TIPO DE CLIENTE DESEA AGREGAR? ---")
            print("a. Regular | b. Premium | c. Corporativo")
            tipo = input("Seleccione (a/b/c): ").lower()

            opciones_validas = {'a': Cliente, 'b': ClientePremium, 'c': ClienteCorporativo}
            
            if tipo not in opciones_validas:
                print("⚠️ Tipo no válido. Regresando al menú principal.")
                continue 

            try:
                datos = pedir_datos_comunes()
                datos['id_cliente'] = sistema.generar_siguiente_id()
                cliente_a_crear = opciones_validas[tipo]

                if tipo == "b":
                    while True:
                        try:
                            desc_input = input("Ingrese porcentaje de descuento (ej: 0.15): ")
                            desc = validar_descuento(desc_input)
                            nuevo_cliente = cliente_a_crear(descuento=desc, **datos)
                            break 
                        except ValueError as e:
                            print(f"❌ {e}")
                else:
                    
                    nuevo_cliente = cliente_a_crear(**datos)

                sistema.agregar_cliente(nuevo_cliente)

            except ValueError as e:
                print(f"\n❌ ERROR DE ENTRADA: Verifique los datos numéricos. ({e})")
            except Exception as e:
                print(f"\n❌ ERROR INESPERADO: {e}")

        elif opcion == "2":
            sistema.listar_clientes()

        elif opcion == "3":
            try:
                id_c = int(input("ID del cliente a modificar: "))
                sistema.actualizar_cliente(id_c)
            except ValueError:
                print("❌ Error: El ID debe ser un número válido.")

        elif opcion == "4":
            try:
                id_c = int(input("ID del cliente a eliminar: "))
                sistema.eliminar_cliente(id_c)
            except ValueError:
                print("❌ Error: El ID debe ser un número.")

        elif opcion == "5":
            print("👋 Saliendo del sistema y guardando datos... ¡Hasta pronto!")
            break
        
        else:
            print("⚠️ Opción no válida.")

if __name__ == "__main__":
    main()