import json
import os
from cliente import Cliente, ClientePremium, ClienteCorporativo
from utilidades import *

class GestionClientes:
    def __init__(self, archivo="clientes.json"):
        self.archivo = archivo
        self.clientes = []
        self.cargar_datos()

    def generar_siguiente_id(self):
        if not self.clientes:
            return 1
        return max(c.id_cliente for c in self.clientes) + 1

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        self.guardar_datos()
        print(f"✅ Cliente '{cliente.nombre}' guardado y persistido.")

    def listar_clientes(self):
        print("\n--- LISTADO DE CLIENTES ---")
        if not self.clientes:
            print("La lista está vacía.")
        for c in self.clientes:
            print(c.mostrar_detalle(), f"\nTotal a Pagar: {c.calcular_pago()}")


    def actualizar_cliente(self, id_buscado):
        cliente = next((c for c in self.clientes if c.id_cliente == id_buscado), None)

        if not cliente:
            print(f"⚠️ No se encontró el cliente con ID: {id_buscado}")
            return

        print(f"\n--- 📝 Editando a: {cliente.nombre} ---")
        print("(Presione Enter para mantener el valor actual)")

        try:
            
            while True:
                try:
                    v_email = input(f"Email [{cliente.email}]: ")
                    if not v_email: 
                        break
                    cliente.email = validar_email(v_email) 
                    break
                except ValueError as e:
                    print(f"❌ {e}")

            while True:
                v_dir = input(f"Dirección [{cliente.direccion}]: ")
                if not v_dir: 
                    break
                if v_dir.strip():
                    cliente.direccion = v_dir
                    break
                print("❌ La dirección no puede estar vacía si decide cambiarla.")

            
            while True:
                try:
                    v_tel = input(f"Teléfono [{cliente.telefono}]: ")
                    if not v_tel:
                        break
                    cliente.telefono = validar_telefono(v_tel)
                    break
                except ValueError as e:
                    print(f"❌ {e}")
            self.guardar_datos()
            print("✅ Datos actualizados exitosamente.")

        except Exception as e:
            print(f"❌ Error durante la actualización: {e}")

    def eliminar_cliente(self, id_buscado):
        cliente_encontrado = next((c for c in self.clientes if c.id_cliente == id_buscado), None)

        if cliente_encontrado:
            self.clientes.remove(cliente_encontrado)
            
            self.guardar_datos()
            print(f"✅ Cliente '{cliente_encontrado.nombre}' (ID: {id_buscado}) eliminado con éxito.")
        else:
            print(f"⚠️ No se encontró ningún cliente con el ID: {id_buscado}.")

    # --- MÉTODOS DE PERSISTENCIA ---

    def guardar_datos(self):
        datos_dict = []
        for c in self.clientes:
            tipo = ("VIP" if isinstance(c, ClientePremium) else 
            "CORP" if isinstance(c, ClienteCorporativo) else  "Regular")
            item = {
                "tipo": tipo,
                "id_cliente": c.id_cliente,
                "nombre": c.nombre,
                "email": c.email,
                "direccion": c.direccion,
                "telefono": c.telefono,
                "total_compra": c.total_compra
            }
            if tipo == "VIP" or tipo =="CORP":
                item["descuento"] = c.descuento
            datos_dict.append(item)

        with open(self.archivo, 'w') as f:
            json.dump(datos_dict, f, indent=4)

    def cargar_datos(self):
        if not os.path.exists(self.archivo):
            return 

        try:
            with open(self.archivo, 'r') as f:
                datos_dict = json.load(f)
                for item in datos_dict:
                    tipo = item.pop("tipo")
                    if tipo == "VIP":
                        obj = ClientePremium(**item)
                    elif tipo == "CORP":
                        if "descuento" in item:
                            item.pop("descuento")
                        obj = ClienteCorporativo(**item)
                    else:
                        obj = Cliente(**item)
                    self.clientes.append(obj)
        except Exception as e:
            print(f"Error al cargar datos: {e}")


