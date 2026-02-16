class Cliente:
    def __init__(self, id_cliente, nombre, email, direccion, telefono, total_compra):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.total_compra = total_compra

    def mostrar_detalle(self):
        return(f"\nNombre Cliente: {self.nombre}\nTelefono: {self.telefono}\nCorreo: {self.email}\nDireccion: {self.direccion}")
    

    def calcular_pago(self):
        return self.total_compra
    
class ClientePremium(Cliente):
    def __init__(self,descuento=0, **kwargs):
        super().__init__(**kwargs)
        self.descuento = descuento

    def calcular_pago(self):
        return self.total_compra * (1 - self.descuento)
    
    def mostrar_detalle(self):
        return super().mostrar_detalle() + (f"\n[Cliente Premium - {self.descuento*100}% desc.]")
    
class ClienteCorporativo(Cliente):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.descuento = 0.25
    
    def calcular_pago(self):
        return self.total_compra * (1-self.descuento)
    
    def mostrar_detalle(self):
        return super().mostrar_detalle() + (f"\n[Cliente Corporativo - {self.descuento*100}% desc.]")

